import cassiopeia as cass

from ..schemas import (
    Summoner,
    Champion,
    Item,
    Skills,
    Skill,
    Map
)

class Converter:

    async def convert(self, cass_dto):
        """
        Convert cass type to our schema type.
        """
        match type(cass_dto):
            case cass.Champion:
                return await self.convert_champion(cass_dto)
            case cass.Champions:
                return await self.convert_champions(cass_dto)
            case cass.Item:
                return await self.convert_item(cass_dto)
            case cass.Items:
                return await self.convert_items(cass_dto)
            case cass.Summoner:
                return await self.convert_summoner(cass_dto)
            case cass.Map:
                return await self.convert_map(cass_dto)
            case cass.Maps:
                return await self.convert_maps(cass_dto)
            case _:
                return 'string'
            
    async def convert_maps(self, maps: cass.Maps):
        return [await self.convert_map(m) for m in maps]
            
    async def convert_map(self, map: cass.Map):
        return Map(
            id=map.id,
            name=map.name,
        )

    async def convert_champion(self, champion):
        return Champion(
            id=champion.id,
            name=champion.name,
            skills=await self.convert_skills(champion)
        )

    async def convert_champions(self, champions):
        return [await self.convert_champion(c) for c in champions]

    async def convert_item(self, item):
        return Item(
            id=item.id,
            name=item.name
        )

    async def convert_items(self, items):
        return [await self.convert_item(i) for i in items]

    async def convert_summoner(self, summoner):
        return Summoner(
            id=summoner.id,
            name=summoner.name
        )

    async def convert_skills(self, champion):
        return Skills(
            passive=Skill(
                name=champion.passive.name,
                description=champion.passive.description
            ),
            q=Skill(
                name=champion.spells[0].name,
                description=champion.spells[0].description
            ),
            w=Skill(
                name=champion.spells[1].name,
                description=champion.spells[1].description
            ),
            e=Skill(
                name=champion.spells[2].name,
                description=champion.spells[2].description
            ),
            r=Skill(
                name=champion.spells[3].name,
                description=champion.spells[3].description
            )
        )