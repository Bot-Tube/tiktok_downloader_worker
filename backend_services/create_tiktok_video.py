import json
import requests
import logging
from typing import Union, Tuple
from backend_services.backend_base import BackendBase


class CreateTiktokVideo(BackendBase):
    def __init__(self):
        super().__init__()

    def create_tiktok_video(self, tiktok_video_id: str, video_url: str) -> Tuple[bool, Union[dict, str]]:
        body = {
            "tiktok_video_id": tiktok_video_id,
            "video_url": video_url
        }
        json_data = json.dumps(body)
        response = requests.post(self.backend_api_url + "create_tiktok_video", json=json_data,
                                 headers=BackendBase.get_headers())
        response_dict = json.loads(response.text)
        if response_dict["status"] == "OK":
            return True, response_dict["data"]

        logging.error("create_tiktok_video service failed. Error: %s.\nstatus_code: %s",
                     response_dict["message"],
                     response_dict["status_code"])
        return False, response_dict["message"]
