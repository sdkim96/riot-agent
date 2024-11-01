import os
from dotenv import load_dotenv

from .skills import PlanManager, AnalysisManager
from .utils import QueryWrapper
from .utils.knowledge import (GameModes, LLM, Regions)
from .actions import LLMHandler, WebAgentHandler, RiotHandler, CrawlingHandler
from .vectorstore import VectorStore


class RiotAgent:
    
    def __init__(
        self,
        query: str,
        llm: LLM.OPENAI.value,
        game_mode: GameModes.RIFT.value,
        region: Regions.KOREA.value

        ) -> None:
        
        self.web_agent = WebAgentHandler()
        self.riot_handler = RiotHandler()
        self.crawler_agent = CrawlingHandler()
        
        self.query = QueryWrapper(query, game_mode, region)
        self.llm = LLMHandler(llm)
        self.analysis_manager = AnalysisManager(self)
        self.plan_manager = PlanManager(self)
        self.vectorstore = VectorStore(self)
        

    async def run(self):
        await self._conduct_research()
        await self._recommend()
    

    async def _conduct_research(self):
        await self.analysis_manager.analyze_intent()
        await self.plan_manager.plan()

    async def _recommend(self):
        pass



async def main():

    load_dotenv()

    query0 = "지금 픽창인데 우리팅 조합이 미드 신드라 탑 렝가고, 상대는 미드 빅토르 탑 갱플랭크야. 난 원딜인데 어떤 챔피언이 젤 좋아?"
    query1 = "내가 좋아하는 선수인 룰러 선수가 자주가는 템트리를 알려줘"
    query2 = "캬하하가 트타로 자주가는 템트리?"

    riot = RiotAgent(
        query=query2,
        llm=LLM.OPENAI.value,
        game_mode=GameModes.ARAM.value,
        region=Regions.KOREA.value
    )

    await riot.run()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())