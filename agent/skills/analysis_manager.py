from langchain.output_parsers import (
    PydanticOutputParser, 
    CommaSeparatedListOutputParser,
    RetryOutputParser
)
from langchain_core.exceptions import OutputParserException

from ..utils.query import QueryWrapper
from ..utils.knowledge import Intents
from ..actions import LLMHandler, CrawlingHandler, WebAgentHandler
from ..dto.parser_using import Intent, Summoner

from ..prompt import PromptTemplateService

class AnalysisManager:
    def __init__(self, agent):
        self.query: QueryWrapper = agent.query
        self.llm: LLMHandler = agent.llm
        self.web_agent: WebAgentHandler = agent.web_agent
        self.crawler_agent: CrawlingHandler = agent.crawler_agent


    async def analyze_intent(self):
        keywords = await self._find_keywords()
        await self._get_intent(keywords)


    async def _find_keywords(self):
        print(f"🔍 Finding keywords from the query: {self.query.query}")

        parser = CommaSeparatedListOutputParser()
        prompt = PromptTemplateService.generate_keywords_prompt(
            parser=parser
        )

        keywords: list[str] = await self.llm.chat_complete(
            prompt=prompt,
            parser=parser,
            input_dict = {
                'query': self.query.query,
                'intents': Intents.get_all_intents()
            }
        )
        print(f"🎯 Keywords found: {keywords}")
        return keywords
        

    async def _get_intent(
        self,
        keywords: list[str]
    ):
        print(f"🔍 Getting intent from the query: {self.query.query}")

        parser = PydanticOutputParser(pydantic_object=Intent)
        # retry_parser = RetryOutputParser(
        #     parser=parser
        #     retry_chain=
        # )
        prompt = PromptTemplateService.generate_intent_prompt(
            parser=parser
        )

        this_intent: Intent = await self.llm.chat_complete(
            prompt=prompt,
            parser=parser,
            input_dict = {
                'query': self.query.query,
                'intents': Intents.get_all_intents(),
                'keywords': keywords
            }
        )
        
        print("🎯 Intent analysis completed.")
        print(f"🎯 Rank1 >>> Intent: {this_intent.rank_1_code}, Description: {this_intent.rank_1_description}")
        print(f"🎯 Rank2 >>> Intent: {this_intent.rank_2_code if this_intent.rank_2_code else None}, Description: {this_intent.rank_2_description if this_intent.rank_2_code else None}")
        
        self.query.intents = (this_intent.rank_1_code, this_intent.rank_2_code)


    async def guess_summoner_name_from_query(self) -> Summoner:
        print(f"🔍 Getting summoner name from the query: {self.query.query}")

        parser = PydanticOutputParser(pydantic_object=Summoner)
        prompt = PromptTemplateService.generate_summoner_prompt(
            parser=parser
        )
        # if user query contains a '#' character, we can assume the user is providing the tag and name
        if '#' in self.query.query:
            maybe = ''
        else:
            web_results = self.web_agent.do_web_search(
               web_query=f"""
                - query: {self.query.query}
                - given the query, guess the summoner name and riot tag.
                """
            )

            maybe = ""
            for r in web_results.get('results', []):
                maybe += r.get('content', '')

        try:
            this_summoner: Summoner = await self.llm.chat_complete(
                prompt=prompt,
                parser=parser,
                input_dict = {
                    'query': self.query.query,
                    'maybe': maybe,
                    'known_players': self.crawler_agent.crawl_pros(self.query.region),
                }
            )
        except OutputParserException:
            this_summoner = Summoner(name=None, tag=None)

        print("🎯 Summoner name analysis completed.")
        print(f"🎯 Name: {this_summoner.name}, Tag: {this_summoner.tag}")

        return this_summoner