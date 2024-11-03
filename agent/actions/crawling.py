import requests
from bs4 import BeautifulSoup

class CrawlingHandler:

    # Private class variable for headers
    __headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    def __init__(self):
        self.pros_data = None
            
    def crawl_pros(self, region: str):
        if self.pros_data is not None:
            return self.pros_data
        
        processed_data = []
        added_summoners = set()

        try:
            base_url = f"https://www.op.gg/spectate/list/pro-gamer?region={region}"
            response = requests.get(base_url, headers=self.__headers)
            response.raise_for_status()  # HTTP 에러 발생 시 예외 처리
            
            soup = BeautifulSoup(response.text, "html.parser")
            summoner_name_divs = soup.find_all("div", class_="summoner-info")
            
            for div in summoner_name_divs:
                summoner_name_span = div.find_all('span')[0]
                summoner_name = summoner_name_span.get_text(strip=True) if summoner_name_span else None
                
                tag_span = div.find_all('span')[1] if len(div.find_all('span')) > 1 else None
                tag = tag_span.get_text(strip=True) if tag_span else None
                
                pro_nickname_span = div.find('span', class_='name')
                pro_nickname = pro_nickname_span.get_text(strip=True) if pro_nickname_span else None
                
                # 중복 체크: pro_nickname이 이미 추가된 경우 생략
                if pro_nickname and pro_nickname not in added_summoners:
                    if summoner_name and tag:
                        info = {
                            'summoner_name': summoner_name,
                            'tag': tag,
                            'pro_nickname': pro_nickname
                        }
                        processed_data.append(info)
                        added_summoners.add(pro_nickname)  # 추가된 pro_nickname 기록

            self.pros_data = processed_data

        except Exception as e:
            print(f"An error occurred: {e}")
            processed_data = None

        return processed_data


    # TODO: I'm not sure if i can crawl the data from the target URL
    def crawl_champions_data(self, region: str = None, game_mode: str = None) -> dict:
        """Crawl champions data from the target URL."""
        target_url = "https://www.fow.lol/stats"
        response = requests.get(target_url, headers=self.__headers)
        
        if response.status_code != 200:
            print("Failed to retrieve data")
            return {}

        soup = BeautifulSoup(response.text, "html.parser")
        
        # Find the table with id "sort_stats"
        table = soup.find("table", {"id": "sort_stats"})
        
        if not table:
            print("Table not found")
            return {}
        
        # Extract headers
        headers = [th.get_text(strip=True) for th in table.find("thead").find_all("th")]
        
        # Extract rows
        data = []
        for row in table.find("tbody").find_all("tr"):
            columns = [td.get_text(strip=True) for td in row.find_all("td")]
            if columns:
                data.append(dict(zip(headers, columns)))
        
        return data

    

if __name__ == "__main__":
    crawler = CrawlingHandler()
    summoner_name_html = crawler.crawl_champions_data()
    print(summoner_name_html)