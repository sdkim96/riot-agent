import asyncio
import inspect  

from langchain.output_parsers import (
    CommaSeparatedListOutputParser,
)

from .analysis_manager import AnalysisManager
from ..prompt import PromptTemplateService
from ..actions import (RiotHandler, LLMHandler)
from ..utils.query import QueryWrapper
from ..tasks import get_all_available_tasks

class TaskManager:

    # TODO: self.query is shared by all the tasks.
    # We must think about how to manage the query object.
    # Either we can pass the query object to each task or we can make the query object as a class variable.
    
    def __init__(self, agent):
        self.analysis_manager: AnalysisManager = agent.analysis_manager
        self.riot_handler: RiotHandler = agent.riot_handler
        self.query: QueryWrapper = agent.query
        self.llm: LLMHandler = agent.llm
        self.available_tasks = None


    async def execute(self, tasks):
        """Do Jobs concurrently, ensuring all tasks are coroutines or awaitable."""
        
        awaitable_tasks = []
        for task in tasks:
            if inspect.iscoroutine(task) or inspect.isawaitable(task):
                awaitable_tasks.append(task)
            elif callable(task):                
                awaitable_tasks.append(asyncio.ensure_future(task(agent=self)))
            else:
                raise TypeError(f"Task {task} is neither awaitable nor callable.")
        
        return await asyncio.gather(*awaitable_tasks)

    async def plan_main_tasks(self) -> list[asyncio.Task]:
        
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

        if '1' in self.query.intents:
            print("📝 Intent 1 (Get Summoner)")
            tasks.append(self._process_summoner())

        if '2' in self.query.intents:
            print("📝 Intent 2 (Get Champion)")
            tasks.append(self._get_champion())

        if '3' in self.query.intents:
            print("📝 Intent 3 (Get Match)")
            tasks.append(self._get_match())

        if '4' in self.query.intents:
            print("📝 Intent 4 (Get Ranking)")
            tasks.append(self._get_ranking())

        if '5' in self.query.intents:
            print("📝 Intent 5 (Get Item)")
            tasks.append(self._get_item())

        return tasks
    

    async def plan_sub_tasks(self) -> list[asyncio.Task]:
        """
        Plan sub tasks by using dynamic task planning
        Read the docs from agent.actions.__init__.py for more information.
        """
        print(f"📝 Planning the sub tasks based on the intent analysis.")
        self.available_tasks = await get_all_available_tasks()

        parser = CommaSeparatedListOutputParser()
        prompt = PromptTemplateService.generate_sub_tasks_prompt(
            parser=parser
        )

        sub_tasks_candidates: list[str] = await self.llm.chat_complete(
            prompt=prompt,
            parser=parser,
            input_dict = {
                'query': self.query.query,
                # 'intents': self.query.intents, #TODO : We have to insert the essential information for the sub tasks.
                'sub_tasks': self.available_tasks
            }
        )

        print(f"📝 Sub tasks: {sub_tasks_candidates}")

        sub_tasks = []
        for candidates in sub_tasks_candidates:
            if candidates in self.available_tasks:
                real_function = self.available_tasks[candidates]["function"]
                sub_tasks.append(real_function)
                
            else:
                print(f"🚨 Sub task: {candidates} is not available in the available tasks")

        return sub_tasks


    # Each Main task do the pre-required tasks to do the sub tasks.
    # targets for each main task are getting essential information for query.
    # For example, If query contains summoner's name, then the main task is to get the summoner's name.

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



    async def _get_champion(self):
        
        all_champions = await self.riot_handler.get_all_champions()
        self.query.all_champions = all_champions


    async def _get_match(self):
        pass

    async def _get_ranking(self):
        pass

    async def _get_item(self):
        pass
        
