from abc import abstractmethod, ABC


TIKTOK_BASE_URL = "https://www.tiktok.com"

class Format(ABC):
    def build(self, *args):
        raise NotImplementedError
    
class HashagRequest(Format):
    def build(self, hashtag):
        return f"{  TIKTOK_BASE_URL}/tag/{hashtag}"