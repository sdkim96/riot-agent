from typing import Tuple

from ..utils.knowledge import Intents, GameModes, Regions

class QueryWrapper:

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

        self.query_background_knowledge: str = None
        
        self.intents: Tuple[Intents.code, Intents.code] = (None, None)
        self.summoner: str = None

        self.target_api = None
        
    def parent_query(self):
       f"I want to {self.intent}"