from typing import Optional
from tiktok_downloader_worker.request import RequestWithKeyword
from tiktok_downloader_worker.parse_response import parse_response
from utilities.utilities import find_between
from TikTokApi import TikTokApi


class TiktokDownloaderWorker:
    def __init__(self, keyword) -> None:
        self.keyword = [keyword, keyword + " video",
                        keyword + " videos",
                        keyword + " " + keyword,
                        keyword + " " + keyword + " video",
                        keyword + " " + keyword + " videos",
                        "video" + " " + keyword,
                        "videos" + " " + keyword,]
        self.search_types = ["hashtag", "discover"] * 2

    def execute(self) -> None:
        video_id_list = self.get_video_ids()
        if video_id_list:
            self.download_tiktok_videos(video_id_list)

    def get_video_ids(self) -> Optional[list]:
        """
        video_id_list > 40 means that i need more than 40 video_id
        to make a compilation of minimum 10 minutes.
        video length * video count = 600 seconds = 10 mins
        15 * 40 = 600 seconds = 10 mins
        """
        video_id_list = list()
        for search_type in self.search_types:
            for keyword in self.keyword:
                request = RequestWithKeyword(keyword, search_type)
                response = request.send_request()
                pretty_response = parse_response(response)
                counter = 0
                last_index = pretty_response.rindex("</html>")
                while last_index > counter:
                    video_id, index = find_between('/video/', '">', pretty_response[counter:])
                    counter += index
                    if video_id and video_id not in video_id_list:
                        video_id_list.append(video_id)
                    else:
                        break
        video_id_list if len(video_id_list) >= 40 else None

    def download_tiktok_videos(self, video_id_list: list) -> None:
        video_id_set = {}
        for video_id in video_id_list:
            # check_video_id_in_db(video)  Bunu ekleyeceğiz. Video id veritabanında varsa indirmeyecek yapmayacak.
            # Eğer video id dbde varsa ve 2 month check i geçmişse de tekrar dahil edebilir.
            # Backend servisi yazılacak ve buradan cagırılacak.
            with TikTokApi() as api:
                video_bytes = api.video(id=str(video_id)).bytes()
                video_info = api.video(id=str(video_id)).info()
                print(video_info)
                unique_user_id = video_info.get("author").get("uniqueId")
                video_url = "https://www.tiktok.com/@{}/video/{}".format(unique_user_id, video_id)

                with open(f'{video_id}.mp4', 'wb') as output:
                    output.write(video_bytes)
