import asyncio

from langchain.output_parsers import (
    CommaSeparatedListOutputParser,
)

from .analysis_manager import AnalysisManager
from ..prompt import PromptTemplateService
from ..actions import (RiotHandler, LLMHandler)
from ..utils.query import QueryWrapper
from ..tasks import get_all_available_tasks

class TaskManager:
    
    def __init__(self, agent):
        self.analysis_manager: AnalysisManager = agent.analysis_manager
        self.riot_handler: RiotHandler = agent.riot_handler
        self.query: QueryWrapper = agent.query
        self.llm: LLMHandler = agent.llm
        self.available_tasks = get_all_available_tasks()


    async def plan_main_tasks(self):
        
        """

        Plan the action based on the intent analysis.
        These below actions are very base of the plan.

        Intent 1 (Get Summoner):
            Get the summoner's name from the query. (llm)
            if summoner's name is not found ->
                find if that name is well known
                    if it is, get his/her summoner name.
                    else, raise Exeption. (llm)
                    
            Get the summoner's recent match history. (riot_interface)
            Get the summoner's most played champion. (riot_interface)

        Intent 2 (Get Champion):
            Get the champion's name from the query. (llm)
            Get the champion's stats. (riot_interface)
            Get the champoin's abilities. (riot_interface)
            Get the champion's advantage/disadvantage. (riot_interface)

        Intent 3 (Get Match):
            Get the match data from the query. (llm)
            Get the match timeline. (riot_interface)
            Get the match outcome. (riot_interface)

        Intent 4 (Get Ranking):
            Get the ranking data from riot interface (riot_interface)

        Intent 5 (Get Item):
            Get the item's name from the query. (llm)
            Get the item's stats. (riot_interface)
            Get the item's effects. (riot_interface)

        """
        print(f"📝 Planning the action based on the intent analysis.")

        tasks = []

        if 1 in self.query.intents:
            print("📝 Intent 1 (Get Summoner)")
            tasks.append(self._process_summoner())

        if 2 in self.query.intents:
            print("📝 Intent 2 (Get Champion)")
            tasks.append(self._get_champion())

        if 3 in self.query.intents:
            print("📝 Intent 3 (Get Match)")
            tasks.append(self._get_match())

        if 4 in self.query.intents:
            print("📝 Intent 4 (Get Ranking)")
            tasks.append(self._get_ranking())

        if 5 in self.query.intents:
            print("📝 Intent 5 (Get Item)")
            tasks.append(self._get_item())

        return tasks

    async def execute(self, tasks):
        """Do Jobs concurrently"""
        return await asyncio.gather(*tasks)
    

    async def plan_sub_tasks(self):
        """
        Plan sub tasks by using dynamic task planning
        Read the docs from agent.actions.__init__.py for more information.
        """
        print(f"📝 Planning the sub tasks based on the intent analysis.")

        parser = CommaSeparatedListOutputParser()
        prompt = PromptTemplateService.generate_sub_tasks_prompt(
            parser=parser
        )

        sub_tasks: list[str] = await self.llm.chat_complete(
            prompt=prompt,
            parser=parser,
            input_dict = {
                'query': self.query.query,
                'sub_tasks': self.available_tasks
            }
        )

        return sub_tasks


    async def _process_summoner(self):
        summoners_candidate = await self.analysis_manager.guess_summoners_from_query()
        if len(summoners_candidate) > 0:

            for summoner_candidate in summoners_candidate:
                try:
                    await self.riot_handler.get_summoner(
                        name=summoner_candidate.name,
                        tagline=summoner_candidate.tag
                    )

                    self.query.target_summoners.append(summoner_candidate)
                except:
                    self.query.target_summoners.append(None)
                    print("🚨 Summoner not found.")

        await self.plan_sub_tasks()


    async def _get_champion(self):
        await self.plan_sub_tasks()

    async def _get_match(self):
        await self.plan_sub_tasks()

    async def _get_ranking(self):
        await self.plan_sub_tasks()

    async def _get_item(self):
        await self.plan_sub_tasks()
        
