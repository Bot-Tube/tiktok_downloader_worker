import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from tiktok_downloader_worker.request import RequestWithKeyword


def test_hashag_request():
    request = RequestWithKeyword("funny", "hashtag")
    request.send_request()
test_hashag_request()