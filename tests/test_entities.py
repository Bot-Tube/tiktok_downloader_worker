import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from entities import tiktok_video


def test_tiktok_video_from_dict():
    d = {
        "id": 1,
        "tiktok_video_id": "123456789",
        "insert_date": "2020-01-01 00:00:00",
        "video_create_date": "2020-01-01 00:00:00",
        "video_url": "https://www.tiktok.com/@user/video/123456789"
    }
    video = tiktok_video.TiktokVideo.from_dict(d)
    assert video.id == 1
    assert video.tiktok_video_id == "123456789"
    assert video.insert_date == "2020-01-01 00:00:00"
    assert video.video_create_date == "2020-01-01 00:00:00"
    assert video.video_url == "https://www.tiktok.com/@user/video/123456789"

def test_tiktok_video_to_json():
    d = {
        "id": 1,
        "tiktok_video_id": "123456789",
        "insert_date": "2020-01-01 00:00:00",
        "video_create_date": "2020-01-01 00:00:00",
        "video_url": "https://www.tiktok.com/@user/video/123456789"
    }
    video = tiktok_video.TiktokVideo.from_dict(d)
    json_str = tiktok_video.TiktokVideo.to_json(video)
    assert json_str == '{"id": 1, "tiktok_video_id": "123456789", "insert_date": "2020-01-01 00:00:00", "video_create_date": "2020-01-01 00:00:00", "video_url": "https://www.tiktok.com/@user/video/123456789"}'


if __name__ == "__main__":
    test_tiktok_video_from_dict()
    test_tiktok_video_to_json()