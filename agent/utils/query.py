from typing import Tuple

from ..utils.knowledge import Intents, GameModes, Regions
from ..dto import Summoner, Champion
from ..actions.riot import RiotHandler

class QueryWrapper:

    __all_champions=RiotHandler.get_all_champions()

    def __init__(
        self, 
        query: str, 
        game_mode: str, 
        region: str
    ):
        """
        Args:
            query (str): The user query to be analyzed.
            intent (Enum.Intents.code): The intent of the query.
        
        """

        self.query: str = query
        self.game_mode: str = game_mode
        self.region: str = region

        self.keywords: list[str] = []
        self.meanings: dict[str, str] = {}
        
        self.intents: Tuple[Intents.code, Intents.code] = (None, None)
        self.summoner: Summoner = None

        self.target_api = None

        @property
        def champions(self):
            return QueryWrapper.__all_champions