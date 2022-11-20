import requests
from abc import abstractmethod, ABC


TIKTOK_BASE_URL = "https://www.tiktok.com"


class Format(ABC):
    @abstractmethod
    def build(self, *args):
        raise NotImplementedError

    @abstractmethod
    def get_useragent(self):
        raise NotImplementedError


class RequestWithKeyword(Format):
    def __init__(self, keyword: str, search_type: str) -> None:
        self.keyword = keyword
        self.search_type = search_type

    def build(self) -> str:
        search_map = {
            "hashtag": f"/tag/{self.keyword}",
            "search": f"/search?q={self.keyword}",
            "discover": f"/discover/{self.keyword}"
        }
        return f"{TIKTOK_BASE_URL}{search_map[self.search_type]}"
    
    def get_useragent(self) -> dict:
        return {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}

    def send_request(self) -> str:
        response = requests.get(url=self.build(),
                                headers=self.get_useragent(),
                                timeout=30)
        with open("response.html", "w", encoding="utf-8") as output:
            output.write(response.text)
        return response.text
