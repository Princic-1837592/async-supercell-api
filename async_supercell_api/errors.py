from typing import Any, Dict, Optional


class ClientError(Exception):
    def __init__(self, reason: Optional[str] = None, message: Optional[str] = 'Unknown error',
                 type: Optional[str] = None, detail: Optional[Dict[str, Any]] = None, **kwargs):
        super().__init__(message)
        self.reason = reason
        self.message = message
        self.type = type
        self.detail = detail
        for key, value in kwargs.items():
            setattr(self, key, value)
