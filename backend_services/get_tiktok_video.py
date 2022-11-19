import json
import requests
import logging
from typing import Union, Tuple
from backend_services.backend_base import BackendBase


class GetTiktokVideo(BackendBase):
    def __init__(self) -> None:
        super().__init__()

    def get_tiktok_video(self, tiktok_video_id: str) -> Tuple[bool, Union[dict, str]]:
        response = requests.get(self.backend_api_url + "get_tiktok_video/" + tiktok_video_id)
        response_dict = json.loads(response.text)
        if response_dict["status"] == "OK":
            return True, response_dict["data"]

        logging.error("get_task service failed. Error: %s.\nstatus_code: %s",
                     response_dict["message"],
                     response_dict["status_code"])
        return False, response_dict["message"]
