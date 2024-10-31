from langchain.output_parsers import PydanticOutputParser
from langchain_core.embeddings import Embeddings

from ..utils.query import QueryWrapper
from ..utils.knowledge import Intents
from ..llm import LLMWrapper
from ..data_models.parser_using import Intent

from ..prompt import PromptTemplateService

class AnalysisManager:
    def __init__(self, agent):
        self.query: QueryWrapper = agent.query
        self.game_mode = agent.game_mode
        self.llm: LLMWrapper = agent.llm

    async def do_job(self):
        await self._get_intent()
        
    async def _get_intent(
        self,
    ):
        print(f"🔍 Getting intent from the query: {self.query.query}")

        intents_list = Intents.get_all_intents()
        parser = PydanticOutputParser(pydantic_object=Intent)
        prompt = PromptTemplateService.generate_intent_prompt(
            parser=parser
        )

        this_intent: Intent = await self.llm.chat_complete(
            prompt=prompt,
            parser=parser,
            input_dict = {
                'query': self.query.query,
                'intents': intents_list
            }
        )
        
        print("🎯 Intent analysis completed.")
        print(f"🎯 Rank1 >>> Intent: {this_intent.rank_1_code}, Description: {this_intent.rank_1_description}")
        print(f"🎯 Rank2 >>> Intent: {this_intent.rank_2_code}, Description: {this_intent.rank_2_description}")
        
        self.query.intents = (this_intent.rank_1_code, this_intent.rank_2_code)

