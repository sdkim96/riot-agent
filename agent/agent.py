import os
from dotenv import load_dotenv

from .skills import RiotAPIScrapper, AnalysisManager
from .utils import QueryWrapper
from .utils.knowledge import (GameModes, LLM)
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

    query0 = "지금 픽창인데 우리팅 조합이 미드 신드라 탑 렝가고, 상대는 미드 빅토르 탑 갱플랭크야. 난 원딜인데 어떤 챔피언이 젤 좋아?"
    query1 = "페이커선수 전적궁금해. 무슨 챔피언을 젤 많이하지?"

    riot = RiotAgent(
        query=query1,
        llm=LLM.OPENAI.value,
        game_mode=GameModes.ARAM.value
    )

    await riot.run()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())