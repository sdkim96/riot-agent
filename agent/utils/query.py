from typing import Tuple, Optional

from ..utils.knowledge import Intents, GameModes, Regions
from ..dto import Summoner, Champion
from ..actions import RiotHandler


class QueryWrapper:

    def __init__(
        self, 
        query: str, 
        game_mode: str, 
        region: str,
        riot_handler: RiotHandler
    ):
        """
        Args:
            query (str): The user query to be analyzed.
            intent (Enum.Intents.code): The intent of the query.
        
        """

        self.query: str = query
        self.game_mode: str = game_mode
        self.region: str = region
        self.riot_handler: RiotHandler = riot_handler

        self.keywords: list[str] = []
        self.meanings: dict[str, str] = {}
        
        self.intents: Tuple[Intents.code, Intents.code] = (None, None)

        self.all_champions = None
        
        self.target_summoners: list[Optional[Summoner]] = []
        self.target_champions: list[Champion] = []
        self.searched_knowledges: dict[str, str] = {}


    async def initalize_asyncs(self):
        champions = await self.riot_handler.get_all_champions()
        self.all_champions = champions