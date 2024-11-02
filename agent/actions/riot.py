import os
import asyncio
import cassiopeia as cass

class RiotHandler:

    def __init__(self, region: str = "NA"):
        if os.getenv("RIOT_API_KEY") is None:
            raise ValueError("RIOT_API_KEY is not set.")
        
        self.riot_api_key = os.getenv("RIOT_API_KEY")
        cass.set_riot_api_key(self.riot_api_key)
        
        self.region = region

    async def get_summoner(
        self,
        name: str,
        tagline: str,
    ) -> cass.Summoner:
        target_account = await asyncio.to_thread(
            cass.get_account,
            name=name,
            tagline=tagline.capitalize(),
            region=self.region
        )
        return target_account.summoner

    async def get_summoner_match_history(
        self,
        summoner: cass.Summoner
    ):
        return await asyncio.to_thread(lambda: summoner.match_history)

    async def get_summoner_most_played_champion(
        self,
        summoner: cass.Summoner
    ):
        return await asyncio.to_thread(lambda: summoner.champion_masteries)

if __name__ == "__main__":
    async def main():
        riot = RiotHandler(region="KR")
        faker = await riot.get_summoner("Hide on Bush", "kr1")
        
        level = faker.level
        most_played_champions = await riot.get_summoner_most_played_champion(faker)
        print(most_played_champions)

        match_history = await riot.get_summoner_match_history(faker)
        print(match_history)

        print(level)

    asyncio.run(main())