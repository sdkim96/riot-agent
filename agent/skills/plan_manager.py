import os

from .analysis_manager import AnalysisManager

class PlanManager:
    
    def __init__(self, agent):
        self.analysis_manager: AnalysisManager = agent.analysis_manager
        self.riot_handler = agent.riot_handler
        self.query = agent.query


    async def plan(self):
        
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

        if 1 in self.query.intents:
            print("📝 Intent 1 (Get Summoner)")
            summoner_candidate = await self.analysis_manager.guess_summoner_name_from_query()
            
            try:
                summoner = self.riot_handler.get_summoner(
                    name=summoner_candidate.name,
                    tagline=summoner_candidate.tag
                )

                match_history = self.riot_handler.get_summnoner_match_history(
                    summoner
                )
                champion_masteries = self.riot_handler.get_summoner_most_played_champion(
                    summoner
                )
            except:
                print("🚨 Summoner not found.")

        if 2 in self.query.intents:
            print("📝 Intent 2 (Get Champion)")
            await self._get_champion()

        
        if 3 in self.query.intents:
            print("📝 Intent 3 (Get Match)")
            await self._get_match()


        if 4 in self.query.intents:
            print("📝 Intent 4 (Get Ranking)")
            await self._get_ranking()


        if 5 in self.query.intents:
            print("📝 Intent 5 (Get Item)")
            await self._get_item()


        
