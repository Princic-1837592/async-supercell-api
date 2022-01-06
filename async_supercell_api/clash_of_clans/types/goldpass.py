from typing import Optional
from ...types import SupercellApiResponse


class GoldPassSeason(SupercellApiResponse):
    def __init__(self, startTime: Optional[str] = None, endTime: Optional[str] = None, **kwargs):
        super().__init__(**kwargs)
        self.startTime = startTime
        self.endTime = endTime
