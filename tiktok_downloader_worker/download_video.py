from TikTokApi import TikTokApi


class DownloadVideo():
    def download(self, video_id):
        with TikTokApi() as api:
            video_bytes = api.video(id=video_id).bytes()
            with open(f'{str(video_id)}.mp4', 'wb') as output:
                output.write(video_bytes)