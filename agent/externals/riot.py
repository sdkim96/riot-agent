import os
import arrow
import datetime
import asyncio
import cassiopeia as cass

from typing import Optional, Union

from ..utils.knowledge import (
    Lane
)

class RiotHandler:

    def __init__(self, region: str = "NA"):
        if os.getenv("RIOT_API_KEY") is None:
            raise ValueError("RIOT_API_KEY is not set.")
        
        self.riot_api_key = os.getenv("RIOT_API_KEY")
        cass.set_riot_api_key(self.riot_api_key)
        
        self.region = region

    ############
    # Summoner #
    ############

    async def get_summoner(
        self,
        name: str,
        tagline: str,
    ) -> cass.Summoner:
        """
        get summoner object
        
        Args:
            name (str): summoner name
            tagline (str): tagline

        Returns:
            cass.Summoner: summoner object
        """
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
        match = summoner.match_history[0]
        for p in match.participants:
            print(f"{p.champion.name}: {p.runes.keystone.name}, ({', '.join([r.name for r in p.stat_runes])})")


    async def get_summoner_most_played_champion(
        self,
        summoner: cass.Summoner
    ):
        return await asyncio.to_thread(lambda: summoner.champion_masteries)

    
    ############
    # Champion #
    ############


    async def get_all_champions(
        self,
        region: Optional[str] = None
    ) -> cass.Champions:
        if region is None:
            region = self.region
        return await asyncio.to_thread(cass.get_champions, region=region)


    async def get_champion_by_name(
        self,
        name: str
    ) -> cass.Champion:
        return await asyncio.to_thread(cass.get_champion, key=name, region=self.region)
        

    async def get_champions_by_lane(
            self, 
            # date: Optional[str] = None,
            lane: str = Lane.ALL.value
        )-> list[cass.Champion]:
        # if date is None:
        #     version = await self._get_patch_version()
        # else:
        #     version = await self._get_patch_version(date)

        all_champions = await self.get_all_champions()

        champions = []

        for champion in all_champions:
            all_lanes_per_champion = champion.play_rates

            for l, play_rate in all_lanes_per_champion.items():
                if (lane == Lane.ALL.value) and (float(play_rate) > 0.0):
                    champions.append(champion)

                elif (lane == l.value) and (float(play_rate) > 0.0):
                    print(f"{champion.name}: {l}, {play_rate}")
                    champions.append(champion)

        return champions
    

    async def get_op_champions(
            self,
            lane: str = Lane.ALL.value
        ):
        champions = await self.get_champions_by_lane(lane=lane)
        
        print(f"OP Champions in {lane}:")
        for champion in champions:
            print(champion.name)


    #########
    # Match #
    #########

    async def get_all_match():
        pass



    ##########
    # League #
    ##########

    async def get_grandmaster_league(
            self,
            queue: str = "RANKED_SOLO_5x5"
    )-> cass.GrandmasterLeague:
        return await asyncio.to_thread(cass.get_grandmaster_league, queue=queue, region=self.region)


    ##########
    # Item   #
    ##########

    async def get_all_items(
        self,
    ) -> cass.Items:
        return await asyncio.to_thread(cass.get_items, region=self.region)

    ##########
    # Maps   #
    ##########


    async def get_all_maps(
        self,
        region: Optional[str] = None
    ) -> cass.Maps:
        if region is None:
            region = self.region
        return await asyncio.to_thread(cass.get_maps, region=region)


    ########
    # Util #
    ########

    #XXX: Don't use this method
    async def _get_patch_version(self, target_date: Optional[Union[str, datetime.date]] = None) -> str:
        """Date format: %y%m%d"""
        
        if target_date is None:
            target_date = datetime.date.today()
        elif isinstance(target_date, str):
            try:
                target_date = datetime.datetime.strptime(target_date, "%y%m%d").date()
            except ValueError:
                raise ValueError("Date format should be YYMMDD, e.g., '240508' for 2024-05-08.")
        
        target_date_arrow = arrow.get(target_date)
        return await asyncio.to_thread(cass.get_version, region=self.region)

        

if __name__ == "__main__":
    async def main():
        
        riot = RiotHandler(region="KR")
        items = await riot.get_all_items()

        print(items)

        # this_patch_version = await RiotHandler()._get_this_patch_version()
        # print(this_patch_version)
        
        # champion= "Jinx"
        # jinx = await RiotHandler(region='KR').get_champion_by_name(champion)

        # print(jinx)


        # riot = RiotHandler(region="KR")
        # faker = await riot.get_summoner("Hide on Bush", "kr1")
        
        # level = faker.level
        # # most_played_champions = await riot.get_summoner_most_played_champion(faker)
        # # print(most_played_champions)

        # match_history = await riot.get_summoner_match_history(faker)
        # print(match_history)

        # print(level)

    asyncio.run(main())