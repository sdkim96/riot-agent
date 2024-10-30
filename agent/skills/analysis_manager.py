from langchain_core.embeddings import Embeddings

from ..utils.query import QueryWrapper
from ..utils.enum import Intents

class AnalysisManager:
    def __init__(self, agent):
        self.embedding: Embeddings = agent.llm.embedding
        self.query: QueryWrapper = agent.query
        self.game_mode = agent.game_mode

    async def do_job(self):
        await self._get_intent()
        
    async def _get_intent(
        self,
    ):
        print(f"🔍 Getting intent from the query: {self.query.query}")

        embedded_query = await self.embedding.aembed_query(self.query.query)
        embedded_query
        

