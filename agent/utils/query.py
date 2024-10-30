class QueryWrapper:

    def __init__(self, query):
        self.query: str = query
        self.intent = None
        self.goal = None

        self.target_api = None
        
