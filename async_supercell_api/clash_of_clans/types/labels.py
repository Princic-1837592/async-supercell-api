from typing import Any, Dict, Optional
from ...types import SupercellApiResponse


class Label(SupercellApiResponse):
    def __init__(self, name: Optional[str] = None, id: Optional[int] = None, iconUrls: Optional[Dict[str, Any]] = None,
                 **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.id = id
        self.iconUrls = iconUrls
