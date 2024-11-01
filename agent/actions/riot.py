import os

import cassiopeia as cass

class RiotHandler:

    def __init__(self, region: str = "NA"):
        
        if os.getenv("RIOT_API_KEY") is None:
            raise ValueError("RIOT_API_KEY is not set.")
        
        self.riot_api_key = os.getenv("RIOT_API_KEY")
        cass.set_riot_api_key(self.riot_api_key)
        
        self.region = region


    def get_summoner(
        self,
        name: str,
        tagline: str,
    ):
        
        target_account = cass.get_account(
            name = name,
            tagline = tagline.capitalize(),
            region = self.region
        )

        return target_account.summoner
    

if __name__ == "__main__":
    riot = RiotHandler(region="KR")
    faker = riot.get_summoner("BuLLDoG", "kr1")

    level=faker.level
    print(level)