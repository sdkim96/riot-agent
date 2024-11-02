import enum

class LLM(enum.Enum):
    OPENAI = "openai"
    ANTHROPIC = "anthropic"

class GameModes(enum.Enum):
    RIFT = "summoners_rift"
    ARAM = "aram"

class Regions(enum.Enum):
    KOREA = "KR"
    NORTH_AMERICA = "NA"
    EUROPE = "EUW"
    LATIN_AMERICA = "LAN"
    BRAZIL = "BR"
    JAPAN = "JP"

class Intents(enum.Enum):
    GET_SUMMONER = (
        1, 
        """
        Retrieve detailed information about a specific summoner or specific pro player, including their current level, rank, and recent gameplay statistics.
        Summoner names are usually in the format `SummonerName#Tag`, where `SummonerName` is the player's name and `Tag` identifies their region or account.
        Pro players are well-known professional gamers who compete in high-level tournaments and leagues.
        """
    )
    GET_CHAMPION = (
        2, 
        "Retrieve specific details about a champion, including their abilities, stats, and background information, suited for in-depth champion analysis."
    )
    GET_MATCH = (
        3, 
        "Retrieve comprehensive data about a specific match, including participant details, match timeline, and outcome, for a full match summary."
    )
    GET_RANKING = (
        4, 
        "Access the current ranked standings, statistics, and achievements for the user or other players in competitive play."
    )
    GET_ITEM = (
        5, 
        "Fetch detailed information about an in-game item, covering stats, cost, and effects, for item-specific analysis or comparison."
    )

    def __init__(self, code, description):
        self.code = code
        self.description = description

    @classmethod
    def get_all_intents(cls):
        return [(intent.code, intent.description) for intent in cls]

class Champions(enum.Enum):
    MASTER_YI = "master_yi"
    JAX = "jax"

