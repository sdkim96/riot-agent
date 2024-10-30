import os

class RiotAPIManager:
    def __init__(self):
        self.api_key = os.getenv("RIOT_API_KEY")
        self.base_url = "https://na1.api.riotgames.com"

    def get_summoner_by_name(self, summoner_name: str) -> dict:
        url = f"{self.base_url}/lol/summoner/v4/summoners/by-name/{summoner_name}"
        headers = {"X-Riot-Token": self.api_key}