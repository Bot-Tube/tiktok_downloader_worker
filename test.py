from TikTokApi import TikTokApi

with TikTokApi() as api:
    video_bytes = api.video(id='6915785138202758401').info()
    # print(video_bytes)
    for key, value in video_bytes.items():
        print(key, " - ", value, "\n")
    # Saving The Video
    # with open('saved_video.mp4', 'wb') as output:
    #     output.write(video_bytes)


    # for video in tag.videos():
    #     print(video.id)
