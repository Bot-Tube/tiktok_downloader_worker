from config import get_backend_api_url


class BackendBase:
    def __init__(self):
        self.backend_api_url = get_backend_api_url()

    @staticmethod
    def get_headers() -> dict:
        return {"Content-Type": "application/json",
                "Accept": "application/json"}
