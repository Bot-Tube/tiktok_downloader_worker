import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from backend_services.get_tiktok_video import GetTiktokVideo
from backend_services.create_tiktok_video import CreateTiktokVideo



def test_get_tiktok_video():
    get_tiktok_task = GetTiktokVideo()
    status, data = get_tiktok_task.get_tiktok_video("6915209978188428038")
    assert status
    assert data["tiktok_video_id"] == "69152123178188428038"
    assert data["video_url"] == "https://www.tiktok.com/@tiktok/video/6915209978188428038"


def test_create_tiktok_video():
    create_tiktok_video = CreateTiktokVideo()
    status, data = create_tiktok_video.create_tiktok_video("69152091231321388428038", "https://www.tiktok.com/@tiktok/video/6915209978188428038")
    assert status
    assert data["tiktok_video_id"] == "69152091231321388428038"
    assert data["video_url"] == "https://www.tiktok.com/@tiktok/video/6915209978188428038"

test_create_tiktok_video()