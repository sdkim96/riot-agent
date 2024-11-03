import os
from dotenv import load_dotenv

from .skills import TaskManager, AnalysisManager
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
        self.riot_handler = RiotHandler(region=region)
        self.crawler_agent = CrawlingHandler()
        
        self.query = QueryWrapper(
            query, 
            game_mode, 
            region,
            riot_handler=self.riot_handler
        )
        self.llm = LLMHandler(llm)
        self.analysis_manager = AnalysisManager(self)
        self.task_manager = TaskManager(self)
        self.vectorstore = VectorStore(self)
        

    async def run(self):
        await self._conduct_research()
        await self._recommend()
    

    async def _conduct_research(self):
        
        await self.analysis_manager.analyze_intent()
        
        main_plans = await self.task_manager.plan_main_tasks()
        await self.task_manager.execute(main_plans)

    async def _recommend(self):
        pass



async def main():

    load_dotenv()

    query0 = "지금 픽창인데 우리팅 조합이 미드 신드라 탑 렝가고, 상대는 미드 빅토르 탑 갱플랭크야. 난 원딜인데 어떤 챔피언이 젤 좋아?"
    query1 = "내가 좋아하는 선수인 룰러 선수가 자주가는 템트리를 알려줘"
    query2 = "Item build for Jinx in ARAM"
    query3 = "챔피언 티어 리스트"
    query4 = "엄준식제자#KR1 이 자주 하는 챔피언을 알려줘"

    difficult_query = "원딜중 왕귀형 챔프를 추천해줘"

    riot = RiotAgent(
        query=difficult_query,
        llm=LLM.OPENAI.value,
        game_mode=GameModes.ARAM.value,
        region=Regions.KOREA.value
    )

    await riot.run()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())