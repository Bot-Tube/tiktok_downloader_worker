
import json
import datetime
import dataclasses


@dataclasses.dataclass
class TiktokVideo:
    id: int                     # may remove
    tiktok_video_id: str
    insert_date: datetime.date = dataclasses.field()
    video_create_date: datetime.date = dataclasses.field()
    video_url: str

    @classmethod
    def from_dict(cls, d: dict) -> "TiktokVideo":
        return cls(**d)

    @classmethod
    def to_json(cls, video: "TiktokVideo") -> str:
        return json.dumps(dataclasses.asdict(video))
