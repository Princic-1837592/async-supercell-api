from urllib.parse import urlencode, quote
from typing import Any, Optional, Tuple, Type
from aiohttp import request
from . import types
from .. import errors
from ..types import Page, SupercellApiResponse


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
            f'{ClashRoyaleAPI.__BASE_URL}/{ClashRoyaleAPI.__VERSION}/{quote(url.lstrip("/"))}{encoded_kwargs}',
            headers = {'authorization': f'Bearer {self.api_key}'},
            debug = self.debug
        )
    
    @staticmethod
    async def __create_object(response: Tuple[int, Any], object_class: Type[SupercellApiResponse] = Page) -> Any:
        status, json_response = response
        if 200 <= status < 300:
            t = type(json_response)
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
                               before: Optional[str] = None) -> Page[types.clans.ClanWarLogEntry]:
        """
        Retrieve clan's clan war log.
        
        `Original method <https://developer.clashroyale.com/api-docs/index.html#!/clans/getClanWarLog>`_.
        
        :param clanTag:
        :param limit:
        :param after:
        :param before:
        :return:
        """
        
        return await ClashRoyaleAPI.__create_object(
            await self.__make_api_request(
                f'/clans/{clanTag}/warlog',
                limit = limit,
                after = after,
                before = before
            )
        )
    
    async def search_clans(self, name: Optional[str] = None, locationId: Optional[int] = None,
                           minMembers: Optional[int] = None, maxMembers: Optional[int] = None,
                           minScore: Optional[int] = None, limit: Optional[int] = None,
                           after: Optional[str] = None, before: Optional[str] = None) -> Page[types.clans.Clan]:
        """
        Search all clans by name and/or filtering the results using various criteria.
        At least one filtering criteria must be defined and if name is used as part of search,
        it is required to be at least three characters long It is not possible to specify ordering for results
        so clients should not rely on any specific ordering as that may change in the future releases of the API.
        
        `Original method <https://developer.clashroyale.com/api-docs/index.html#!/clans/searchClans>`_.
        
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
                '/clans',
                name = name,
                locationId = locationId,
                minMembers = minMembers,
                maxMembers = maxMembers,
                minScore = minScore,
                limit = limit,
                after = after,
                before = before
            )
        )
    
    async def get_river_race_war_log(self, clanTag: str, limit: Optional[int] = None, after: Optional[str] = None,
                                     before: Optional[str] = None) -> Page[types.clans.RiverRaceLogEntry]:
        """
        Retrieve clan's river race log.
        
        `Original method <https://developer.clashroyale.com/api-docs/index.html#!/clans/getRiverRaceWarLog>`_.
        
        :param clanTag:
        :param limit:
        :param after:
        :param before:
        :return:
        """
        
        return await ClashRoyaleAPI.__create_object(
            await self.__make_api_request(
                f'/clans/{clanTag}/riverracelog',
                limit = limit,
                after = after,
                before = before,
            )
        )
    
    async def get_current_war(self, clanTag: str) -> types.clans.CurrentClanWar:
        """
        Retrieve information about clan's current clan war.
        
        `Original method <https://developer.clashroyale.com/api-docs/index.html#!/clans/getCurrentWar>`_.
        
        :param clanTag:
        :return:
        """
        
        return await ClashRoyaleAPI.__create_object(
            await self.__make_api_request(
                f'/clans/{clanTag}/currentwar'
            ),
            types.clans.CurrentClanWar
        )
    
    async def get_clan(self, clanTag: str) -> types.clans.Clan:
        """
        Get information about a single clan by clan tag. Clan tags can be found using clan search operation.
        
        `Original method <https://developer.clashroyale.com/api-docs/index.html#!/clans/getClan>`_.
        
        :param clanTag:
        :return:
        """
        
        return await ClashRoyaleAPI.__create_object(
            await self.__make_api_request(
                f'/clans/{clanTag}'
            ),
            types.clans.Clan
        )
    
    async def get_clan_members(self, clanTag: str, limit: Optional[int] = None, after: Optional[str] = None,
                               before: Optional[str] = None) -> Page[types.clans.ClanMember]:
        """
        List clan members.
        
        `Original method <https://developer.clashroyale.com/api-docs/index.html#!/clans/getClanMembers>`_.
        
        :param clanTag:
        :param limit:
        :param after:
        :param before:
        :return:
        """
        
        return await ClashRoyaleAPI.__create_object(
            await self.__make_api_request(
                f'/clans/{clanTag}/members',
                limit = limit,
                after = after,
                before = before
            )
        )
    
    async def get_current_river_race(self, clanTag: str) -> types.clans.CurrentRiverRace:
        """
        Retrieve information about clan's current river race.
        
        `Original method <https://developer.clashroyale.com/api-docs/index.html#!/clans/getCurrentRiverRace>`_.
        
        :param clanTag:
        :return:
        """
        
        return await ClashRoyaleAPI.__create_object(
            await self.__make_api_request(
                f'/clans/{clanTag}/currentriverrace'
            ),
            types.clans.CurrentRiverRace
        )
    
    # players
    async def get_player(self, playerTag: str) -> types.players.Player:
        """
        Get information about a single player by player tag. Player tags can be found either in game or by from clan member lists.
        
        `Original method <https://developer.clashroyale.com/api-docs/index.html#!/players/getPlayer>`_.
        
        :param playerTag:
        :return:
        """
        
        return await ClashRoyaleAPI.__create_object(
            await self.__make_api_request(
                f'/players/{playerTag}'
            ),
            types.players.Player
        )
    
    async def get_player_upcoming_chests(self, playerTag: str) -> types.players.UpcomingChests:
        """
        Get list of reward chests that the player will receive next in the game.
        
        `Original method <https://developer.clashroyale.com/api-docs/index.html#!/players/getPlayerUpcomingChests>`_.
        
        :param playerTag:
        :return:
        """
        
        return await ClashRoyaleAPI.__create_object(
            await self.__make_api_request(
                f'/players/{playerTag}/upcomingchests'
            ),
            types.players.UpcomingChests
        )
    
    async def get_player_battles(self, playerTag: str) -> Page[types.players.Battle]:
        """
        Get list of recent battles for a player.
        
        `Original method <https://developer.clashroyale.com/api-docs/index.html#!/players/getPlayerBattles>`_.
        
        :param playerTag:
        :return:
        """
        
        return await ClashRoyaleAPI.__create_object(
            await self.__make_api_request(
                f'/players/{playerTag}/battlelog'
            ),
            types.players.Battle
        )
    
    # cards
    async def get_cards(self, limit: Optional[int] = None, after: Optional[str] = None, before: Optional[str] = None) ->\
            Page[types.players.Item]:
        """
        Get list of available cards.
        
        `Original method <https://developer.clashroyale.com/api-docs/index.html#!/cards/getCards>`_.
        
        :param limit:
        :param after:
        :param before:
        :return:
        """
        
        return await ClashRoyaleAPI.__create_object(
            await self.__make_api_request(
                '/cards',
                limit = limit,
                after = after,
                before = before
            )
        )
