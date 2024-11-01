import os
from tavily import TavilyClient

class WebAgentHandler:
    
    def __init__(self):
        self.tavily_client = TavilyClient(os.getenv("TAVILY_API_KEY"))

    def _concat_results_to_string(self, results: list):
        result_str = ""
        for r in results.get('results', []):
            result_str += r.get('content', '')

        return result_str


    def do_web_search(self, web_query: str):
        return self.tavily_client.search(web_query)
    
    def search_background_knowledge_of_query(self, web_query: str):
        query = f"""
        Notice keywords of the given query, 
        and search the keyword in the web.

        - query: {web_query}
        """

        backgrounds = self._concat_results_to_string(self.tavily_client.search(query))
        return backgrounds