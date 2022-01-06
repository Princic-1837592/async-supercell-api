from typing import Any, Dict, Optional


class ClientError(Exception):
    """
    Generic exception. contains all the information about the error response.
    
    :param reason:
    :param message:
    :param type:
    :param detail:
    :type reason: Optional[str]
    :type message: Optional[str]
    :type type: Optional[str]
    :type detail: Optional[Dict[str, Any]]
    """
    
    def __init__(self, reason: Optional[str] = None, message: Optional[str] = 'Unknown error',
                 type: Optional[str] = None, detail: Optional[Dict[str, Any]] = None, **kwargs):
        super().__init__(f'Message: {message}. Reason: {reason}')
        self.reason = reason
        self.message = message
        self.type = type
        self.detail = detail
        for key, value in kwargs.items():
            setattr(self, key, value)
