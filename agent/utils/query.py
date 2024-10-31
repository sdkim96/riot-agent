from typing import Tuple

from ..utils.knowledge import Intents

class QueryWrapper:

    def __init__(self, query):
        """
        Args:
            query (str): The user query to be analyzed.
            intent (Enum.Intents.code): The intent of the query.
        
        """

        self.query: str = query
        self.intents: Tuple[Intents.code, Intents.code] = None
        self.goal = None

        self.target_api = None
        
    def parent_query(self):
       f"I want to {self.intent}"