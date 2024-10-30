import os
from dotenv import load_dotenv

from .skills import RiotAPIScrapper, AnalysisManager
from .utils import QueryWrapper
from .utils.enum import (GameModes, LLM)
from .llm import LLMWrapper
from .vectorstore import VectorStore


class RiotAgent:
    
    def __init__(
        self,
        query: str,
        llm: LLM.OPENAI.value,
        game_mode: GameModes.ARAM.value

        ) -> None:
        load_dotenv()
        self.query = QueryWrapper(query)
        self.llm = LLMWrapper(llm)
        self.game_mode = game_mode
        

        """
        1. 주어진 쿼리에 대해 어떤 걸 수행해야 하는지 분석
        2. 

        
        """
        self.analysis_manager = AnalysisManager(self)
        self.api_scrapper = RiotAPIScrapper(self)
        self.vectorstore = VectorStore(self)

    async def run(self):
        await self._conduct_research()
        await self._recommend()
    

    async def _conduct_research(self):
        await self.analysis_manager.do_job()
        await self.api_scrapper.scrap()

    async def _recommend(self):
        pass



async def main():
    riot = RiotAgent(
        query="I want to play a game",
        llm=LLM.OPENAI.value,
        game_mode=GameModes.ARAM.value
    )

    await riot.run()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())