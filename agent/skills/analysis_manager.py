import re
from typing import Optional

from langchain.output_parsers import (
    PydanticOutputParser, 
    CommaSeparatedListOutputParser,
)
from langchain_core.output_parsers import StrOutputParser
from langchain_core.exceptions import OutputParserException

from ..utils.query import QueryWrapper
from ..utils.knowledge import Intents
from ..externals import LLMHandler, CrawlingHandler, WebAgentHandler
from ..schemas import Intent, Summoner, Champion
from ..vectorstore import VectorStore
from ..prompt import PromptTemplateService

class AnalysisManager:
    def __init__(self, agent):
        self.query_wrapper: QueryWrapper = agent.query_wrapper
        self.llm: LLMHandler = agent.llm
        self.vectorstore: VectorStore = agent.vectorstore
        self.web_agent: WebAgentHandler = agent.web_agent
        self.crawler_agent: CrawlingHandler = agent.crawler_agent
        self.summoner_regrex = r'(?P<name>.+)#(?P<tag>.+)'


    async def analyze_intent(self, query: str = None):
        """
        Analyze the intent of the user query.
        
        Steps:
            1. Find keywords from the query.
            2. Get the intent from the query.
        """        
        if query is None:
            target_query = self.query_wrapper.query

        await self._find_keywords_and_meaning(target_query=target_query)
        await self._get_intent()


    #TODO: If user's query can be regularized, ex) " Word#Tag " -> This is a summoner name, then we can use this information to improve the summoner name extraction. 
    async def _find_keywords_and_meaning(
            self, 
            target_query: Optional[str] = None
        ) -> list[str]:

        if target_query is None:
            target_query = self.query_wrapper.query

        print(f"🔍 Finding keywords from the query: {target_query}")

        parser = CommaSeparatedListOutputParser()
        prompt = PromptTemplateService.generate_keywords_prompt(
            parser=parser
        )

        keywords: list[str] = await self.llm.chat_complete(
            prompt=prompt,
            parser=parser,
            input_dict = {
                'query': target_query,
                'intents': Intents.get_all_intents()
            }
        )
        print(f"🎯 Keywords found: {keywords}")

        self.query_wrapper.keywords = keywords
        keywords_information = await self._find_keyword_information(keywords)

        return keywords_information
    

    async def _find_keyword_information(self, keywords: Optional[list[str]]) -> list[dict[str, str]]:
        
        if keywords is None:
            keywords = self.query_wrapper.keywords

        print(f"🔍 Finding domain knowledge from the keywords: {keywords}")

        parser = StrOutputParser()
        prompt = PromptTemplateService.generate_domain_knowlege_from_keyword()
        keyword_information = []

        for k in keywords:
            information: str = await self.llm.chat_complete(
                prompt=prompt,
                parser=parser,
                input_dict = {
                    'keywords': k
                }
            )

            print(f"🎯 Keywords {k} means: {information[:30]}...")

            keyword_information.append({
                k: information
            })

        self.query_wrapper.meanings = keyword_information       
        return keyword_information
        

    async def _get_intent(
        self,
        keywords: Optional[list[dict[str, str]]] = None
    ):
        print(f"🔍 Getting intent from the query: {self.query_wrapper.query}")

        parser = PydanticOutputParser(pydantic_object=Intent)

        prompt = PromptTemplateService.generate_intent_prompt(
            parser=parser
        )

        try:
            this_intent: Intent = await self.llm.chat_complete(
                prompt=prompt,
                parser=parser,
                input_dict = {
                    'query': self.query_wrapper.query,
                    'intents': Intents.get_all_intents(),
                    'keywords': keywords
                }
            )
        except OutputParserException:
            #XXX : Not implemented yet.
            print("⚠️ Could not parse the intent, Do similarity search.")
            this_intent = Intent(
                rank_1_code = '2',
                rank_2_code = '3',
                rank_3_code = '5'
            )

            assert True, "Not implemented yet."
            response = await self.vectorstore.do_similarity_search(
                query = self.query_wrapper.query,
                compare_with = Intents.get_all_intents(),
                kwargs={
                    'keywords': keywords
                }
            )
        
        print("🎯 Intent analysis completed.")
        print(f"🎯 Rank1 >>> Intent: {this_intent.rank_1_code}")
        print(f"🎯 Rank2 >>> Intent: {this_intent.rank_2_code if this_intent.rank_2_code else None}")
        print(f"🎯 Rank3 >>> Intent: {this_intent.rank_3_code if this_intent.rank_3_code else None} \n")
        
        self.query_wrapper.intents = (this_intent.rank_1_code, this_intent.rank_2_code, this_intent.rank_3_code)


    async def guess_summoners_from_query(self) -> list[Summoner] | list[None]:
        print(f"🔍 Getting summoner name from the query: {self.query_wrapper.query}")

        summoners= []

        matches = re.finditer(self.summoner_regrex, self.query_wrapper.query)
        for match in matches:
            name = match.group('name')
            tag = match.group('tag')
            summoners.append(Summoner(name=name, tag=tag))

        if not summoners:
            #TODO: We must think about how to handle multiple summoner names.
            parser = PydanticOutputParser(pydantic_object=Summoner)
            prompt = PromptTemplateService.generate_summoner_prompt(
                parser=parser
            )

            web_results = self.web_agent.do_web_search(
                web_query=f"""
                - query: {self.query_wrapper.query}
                - given the query, guess the summoner name and riot tag.
                """
            )

            maybe = ""
            for r in web_results.get('results', []):
                maybe += r.get('content', '')

            try:
                summoner_list: list[Summoner] = await self.llm.chat_complete(
                    prompt=prompt,
                    parser=parser,
                    input_dict = {
                        'query': self.query_wrapper.query,
                        'maybe': maybe,
                        'known_players': self.crawler_agent.crawl_pros(self.query_wrapper.region),
                    }
                )

                summoners.extend(summoner_list)

                print("🎯 Summoner name analysis completed.")
                for s in summoners:
                    print(f"🎯 Summoner Name: {s.name}#{s.tag}")

            except OutputParserException:
                print("⚠️ Could not parse multiple summoner names.")

        return summoners
    

    async def guess_champion_from_query(self):
        print(f"🔍 Getting champion name from the query: {self.query_wrapper.query}")

        parser = CommaSeparatedListOutputParser()
        prompt = PromptTemplateService.generate_champion_prompt(
            parser=parser
        )

        hints = self.query_wrapper.meanings

        these_champions = []
        for champion in self.query_wrapper.target_champions:
            these_champions.append(champion.name)

        try:
            champions_candidate: list[str] = await self.llm.chat_complete(
                prompt=prompt,
                parser=parser,
                input_dict = {
                    'query': self.query_wrapper.query,
                    'hints': hints,
                    'all_champions': these_champions
                }
            )

            print("🎯 Champion name analysis completed.")
            print(f"🎯 Champion Name: {champions_candidate}")

        except OutputParserException:
            print("⚠️ Could not parse the champion name.")
            champions_candidate = None

        return champions_candidate