from typing import Tuple, Optional

from ..utils.knowledge import Intents, GameModes, Regions
from ..schemas import Summoner, Champion, Map
from ..externals import RiotHandler


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
        self.meanings: list[dict[str, str]] = []
        
        self.intents: Tuple[Intents.code, Intents.code] = (None, None)

        

        ########## MAIN TASKS ##########
        self.all_champions = None
        self.all_maps = None
        self.all_items = None
        self.target_lane: Optional[str] = None
        self.target_summoners: list[Optional[Summoner]] = []
        self.target_champions: list[Champion] = []

        ########## SUB TASKS ##########
        self.searched_knowledges: dict[str, str] = {}