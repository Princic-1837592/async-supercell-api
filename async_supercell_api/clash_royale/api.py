from urllib.parse import urlencode
from typing import Any, Optional, Tuple
from aiohttp import request
from .types.clans import Clan, ClanWarLogEntry
from .. import errors
from ..types import Page


class ClashRoyaleAPI:
    """
    
    """
    __BASE_URL: str = 'https://api.clashroyale.com'
    __VERSION: str = 'v1'
    
    def __init__(self, api_key: str, debug: bool = False):
        self.api_key = api_key
        self.debug = debug
    
    @staticmethod
    async def __make_request(url: str, method: str = 'GET', headers: dict = None, debug: bool = False) -> Tuple[
        int, Any]:
        if headers is None:
            headers = {}
        async with request(method, url, headers = headers) as response:
            if debug:
                print(response.status, url)
            return response.status, await response.json()
    
    async def __make_api_request(self, url: str, **kwargs: Any) -> Tuple[int, Any]:
        kwargs = {n: v for n, v in kwargs.items() if v is not None}
        encoded_kwargs = f'?{urlencode(kwargs)}' if kwargs else ''
        return await ClashRoyaleAPI.__make_request(
            f'{ClashRoyaleAPI.__BASE_URL}/{ClashRoyaleAPI.__VERSION}/{url.lstrip("/")}{encoded_kwargs}',
            headers = {'authorization': f'Bearer {self.api_key}'},
            debug = self.debug
        )
    
    @staticmethod
    async def __create_object(response: Tuple[int, Any], object_class = None) -> Any:
        status, json_response = response
        if 200 <= status < 300:
            t = type(json_response)
            print(json_response)
            if object_class is not None:
                if t == dict:
                    return object_class(**json_response)
                if t == list:
                    return list(map(lambda x: object_class(**x), json_response))
            return json_response
        else:
            raise errors.ClientError(**(json_response or {}))
    
    # clans
    async def get_clan_war_log(self, clanTag: str, limit: Optional[int] = None, after: Optional[str] = None,
                               before: Optional[str] = None) -> Page[ClanWarLogEntry]:
        """
        
        :param clanTag:
        :param limit:
        :param after:
        :param before:
        :return:
        """
        
        return await ClashRoyaleAPI.__create_object(
            await self.__make_api_request(f'/clans/{clanTag}/warlog', limit = limit, after = after, before = before),
            Page
        )
    
    async def search_clan(self, name: Optional[str] = None, locationId: Optional[int] = None,
                          minMembers: Optional[int] = None, maxMembers: Optional[int] = None,
                          minScore: Optional[int] = None, limit: Optional[int] = None,
                          after: Optional[str] = None, before: Optional[str] = None) -> Page[Clan]:
        """
        
        :param name:
        :param locationId:
        :param minMembers:
        :param maxMembers:
        :param minScore:
        :param limit:
        :param after:
        :param before:
        :return:
        """
        
        return await ClashRoyaleAPI.__create_object(
            await self.__make_api_request(
                f'/clans',
                name = name,
                locationId = locationId,
                minMembers = minMembers,
                maxMembers = maxMembers,
                minScore = minScore,
                limit = limit,
                after = after,
                before = before
            ),
            Page
        )
