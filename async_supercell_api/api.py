from urllib.parse import urlencode, quote
from typing import Any, Optional, Tuple, Type
from aiohttp import request
from . import errors
from .types import Page, SupercellApiResponse


class SupercellAPI:
    """
    Superclass for Supercell APIs. Should not be used, use subclasses instead.
    
    :param base_url:
    :param version:
    :param api_key:
    :param debug:
    :type base_url: str
    :type version: str
    :type api_key: str
    :type debug: bool
    """
    
    def __init__(self, base_url: str, version: str, api_key: str, debug: bool = False):
        self.base_url = base_url.strip('/')
        self.version = version.strip('/')
        self.api_key = api_key
        self.debug = debug
    
    @staticmethod
    async def make_request(url: str, method: str = 'GET', headers: dict = None, json: dict = None,
                           debug: bool = False) -> Tuple[int, Any]:
        async with request(method, url, headers = headers, json = json) as response:
            if debug:
                print(response.status, url)
            return response.status, await response.json()
    
    async def make_api_request(self, url: str, **kwargs: Any) -> Tuple[int, Any]:
        kwargs = {n: v for n, v in kwargs.items() if v is not None}
        encoded_kwargs = f'?{urlencode(kwargs)}' if kwargs else ''
        return await SupercellAPI.make_request(
            f'{self.base_url}/{self.version}/{quote(url.lstrip("/"))}{encoded_kwargs}',
            headers = {'Authorization': f'Bearer {self.api_key}'},
            debug = self.debug
        )
    
    @staticmethod
    async def create_object(response: Tuple[int, Any], object_class: Type[SupercellApiResponse] = Page,
                            page_generic_type: Optional[Type[SupercellApiResponse]] = None) -> Any:
        status, json_response = response
        if 200 <= status < 300:
            t = type(json_response)
            if object_class is not None:
                if t == dict:
                    return object_class(**json_response, _page_generic_type = page_generic_type)
                if t == list:
                    return list(map(lambda x: object_class(**x), json_response))
            return json_response
        else:
            raise errors.ClientError(**(json_response or {}))
