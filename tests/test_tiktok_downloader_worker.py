import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from tiktok_downloader_worker.worker import TiktokDownloaderWorker

def test_hashag_request():
    worker_object = TiktokDownloaderWorker("funny")
    # worker_object.execute()
    worker_object.download_tiktok_videos(["6915785138202758401"])
test_hashag_request()


"""
şuanki keyword yapısında hashtag ve discovery'den yaklasık 123 video_id dönüyor.
"""