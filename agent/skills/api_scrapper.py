import os

class RiotAPIScrapper:
    
    def __init__(
        self, 
        agent
    ):
        self.riot_api_key = os.getenv("RIOT_API_KEY")

    async def _get_recommendation(self):
        pass


    async def scrap(self):
        pass