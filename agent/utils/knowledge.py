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

class Lane(enum.Enum):
    TOP = "TOP"
    JUNGLE = "JUNGLE"
    MIDDLE = "MIDDLE"
    BOTTOM = "BOTTOM"
    UTILITY = "UTILITY"
    ALL = "ALL"


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

champions = {
    266: ("Aatrox", "아트록스"),
    103: ("Ahri", "아리"),
    84: ("Akali", "아칼리"),
    166: ("Akshan", "아크샨"),
    12: ("Alistar", "알리스타"),
    32: ("Amumu", "아무무"),
    34: ("Anivia", "애니비아"),
    1: ("Annie", "애니"),
    523: ("Aphelios", "아펠리오스"),
    22: ("Ashe", "애쉬"),
    136: ("Aurelion Sol", "아우렐리온 솔"),
    893: ("Aurora", "오로라"),
    268: ("Azir", "아지르"),
    432: ("Bard", "바드"),
    200: ("Bel'Veth", "벨베스"),
    53: ("Blitzcrank", "블리츠크랭크"),
    63: ("Brand", "브랜드"),
    201: ("Braum", "브라움"),
    233: ("Briar", "브라이어"),
    51: ("Caitlyn", "케이틀린"),
    164: ("Camille", "카밀"),
    69: ("Cassiopeia", "카시오페아"),
    31: ("Cho'Gath", "초가스"),
    42: ("Corki", "코르키"),
    122: ("Darius", "다리우스"),
    131: ("Diana", "다이애나"),
    119: ("Draven", "드레이븐"),
    36: ("Dr. Mundo", "문도 박사"),
    245: ("Ekko", "에코"),
    60: ("Elise", "엘리스"),
    28: ("Evelynn", "이블린"),
    81: ("Ezreal", "이즈리얼"),
    9: ("Fiddlesticks", "피들스틱"),
    114: ("Fiora", "피오라"),
    105: ("Fizz", "피즈"),
    3: ("Galio", "갈리오"),
    41: ("Gangplank", "갱플랭크"),
    86: ("Garen", "가렌"),
    150: ("Gnar", "나르"),
    79: ("Gragas", "그라가스"),
    104: ("Graves", "그레이브즈"),
    887: ("Gwen", "그웬"),
    120: ("Hecarim", "헤카림"),
    74: ("Heimerdinger", "하이머딩거"),
    910: ("Hwei", "흐웨이"),
    420: ("Illaoi", "일라오이"),
    39: ("Irelia", "이렐리아"),
    427: ("Ivern", "아이번"),
    40: ("Janna", "잔나"),
    59: ("Jarvan IV", "자르반 4세"),
    24: ("Jax", "잭스"),
    126: ("Jayce", "제이스"),
    202: ("Jhin", "진"),
    222: ("Jinx", "징크스"),
    145: ("Kai'Sa", "카이사"),
    429: ("Kalista", "칼리스타"),
    43: ("Karma", "카르마"),
    30: ("Karthus", "카서스"),
    38: ("Kassadin", "카사딘"),
    55: ("Katarina", "카타리나"),
    10: ("Kayle", "케일"),
    141: ("Kayn", "케인"),
    85: ("Kennen", "케넨"),
    121: ("Kha'Zix", "카직스"),
    203: ("Kindred", "킨드레드"),
    240: ("Kled", "클레드"),
    96: ("Kog'Maw", "코그모"),
    897: ("K'Sante", "크산테"),
    7: ("LeBlanc", "르블랑"),
    64: ("Lee Sin", "리 신"),
    89: ("Leona", "레오나"),
    876: ("Lillia", "릴리아"),
    127: ("Lissandra", "리산드라"),
    236: ("Lucian", "루시안"),
    117: ("Lulu", "룰루"),
    99: ("Lux", "럭스"),
    54: ("Malphite", "말파이트"),
    90: ("Malzahar", "말자하"),
    57: ("Maokai", "마오카이"),
    11: ("Master Yi", "마스터 이"),
    902: ("Milio", "밀리오"),
    21: ("Miss Fortune", "미스 포츈"),
    62: ("Wukong", "오공"),
    82: ("Mordekaiser", "모데카이저"),
    25: ("Morgana", "모르가나"),
    950: ("Naafiri", "나피리"),
    267: ("Nami", "나미"),
    75: ("Nasus", "나서스"),
    111: ("Nautilus", "노틸러스"),
    518: ("Neeko", "니코"),
    76: ("Nidalee", "니달리"),
    895: ("Nilah", "닐라"),
    56: ("Nocturne", "녹턴"),
    20: ("Nunu & Willump", "누누와 윌럼프"),
    2: ("Olaf", "올라프"),
    61: ("Orianna", "오리아나"),
    516: ("Ornn", "오른"),
    80: ("Pantheon", "판테온"),
    78: ("Poppy", "뽀삐"),
    555: ("Pyke", "파이크"),
    246: ("Qiyana", "키아나"),
    133: ("Quinn", "퀸"),
    497: ("Rakan", "라칸"),
    33: ("Rammus", "람머스"),
    421: ("Rek'Sai", "렉사이"),
    526: ("Rell", "렐"),
    888: ("Renata Glasc", "레나타 글라스크"),
    58: ("Renekton", "레넥톤"),
    107: ("Rengar", "렝가"),
    92: ("Riven", "리븐"),
    68: ("Rumble", "럼블"),
    13: ("Ryze", "라이즈"),
    360: ("Samira", "사미라"),
    113: ("Sejuani", "세주아니"),
    235: ("Senna", "세나"),
    147: ("Seraphine", "세라핀"),
    875: ("Sett", "세트"),
    35: ("Shaco", "샤코"),
    98: ("Shen", "쉔"),
    102: ("Shyvana", "쉬바나"),
    27: ("Singed", "신지드"),
    14: ("Sion", "사이온"),
    15: ("Sivir", "시비르"),
    72: ("Skarner", "스카너"),
    901: ("Smolder", "스몰더"),
    37: ("Sona", "소나"),
    16: ("Soraka", "소라카"),
    50: ("Swain", "스웨인"),
    517: ("Sylas", "사일러스"),
    134: ("Syndra", "신드라"),
    223: ("Tahm Kench", "탐 켄치"),
    163: ("Taliyah", "탈리야"),
    91: ("Talon", "탈론"),
    44: ("Taric", "타릭"),
    17: ("Teemo", "티모"),
    412: ("Thresh", "쓰레쉬"),
    18: ("Tristana", "트리스타나"),
    48: ("Trundle", "트런들"),
    23: ("Tryndamere", "트린다미어"),
    4: ("Twisted Fate", "트위스티드 페이트"),
    29: ("Twitch", "트위치"),
    77: ("Udyr", "우디르"),
    6: ("Urgot", "우르곳"),
    110: ("Varus", "바루스"),
    67: ("Vayne", "베인"),
    45: ("Veigar", "베이가"),
    161: ("Vel'Koz", "벨코즈"),
    711: ("Vex", "벡스"),
    254: ("Vi", "바이"),
    234: ("Viego", "비에고"),
    112: ("Viktor", "빅토르"),
    8: ("Vladimir", "블라디미르"),
    106: ("Volibear", "볼리베어"),
    19: ("Warwick", "워윅"),
    498: ("Xayah", "자야"),
    101: ("Xerath", "제라스"),
    5: ("Xin Zhao", "신 짜오"),
    157: ("Yasuo", "야스오"),
    777: ("Yone", "요네"),
    83: ("Yorick", "요릭"),
    350: ("Yuumi", "유미"),
    154: ("Zac", "자크"),
    238: ("Zed", "제드"),
    221: ("Zeri", "제리"),
    115: ("Ziggs", "직스"),
    26: ("Zilean", "질리언"),
    142: ("Zoe", "조이"),
    143: ("Zyra", "자이라")
}
