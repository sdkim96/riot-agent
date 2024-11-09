import os
from tavily import AsyncTavilyClient

class WebAgentHandler:
    
    def __init__(self):
        self.tavily_client = AsyncTavilyClient(os.getenv("TAVILY_API_KEY"))

    def _concat_results_to_string(self, results: list):
        result_str = ""
        for r in results.get('results', []):
            result_str += r.get('content', '')

        return result_str


    async def do_web_search(self, web_query: str):
        return await self.tavily_client.search(web_query)
    
    async def search_background_knowledge_of_query(
            self, 
            web_query: str,
            limit: int = 2
        ):
        query = f"""
        search the keyword in the web.
        You must Search on 'League of Legends' domain.
        Because this is a query about League of Legends or Riot games.

        - keyword: {web_query}
        """
        web_result = await self.tavily_client.search(
            query=query,
            max_results=limit
        )
        backgrounds = self._concat_results_to_string(web_result)
        return backgrounds