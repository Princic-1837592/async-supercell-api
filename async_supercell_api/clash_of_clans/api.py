from typing import List, Optional
from . import types
from ..api import SupercellAPI
from ..types import Page


class ClashOfClansAPI(SupercellAPI):
    """
    Class to interact with Clash of Clans APIs
    
    :param api_key:
    :param debug: in case you want the class to print every url and response status. Default (and suggested) False
    :type api_key: str
    :type debug: Optional[bool]
    """
    
    def __init__(self, api_key: str, debug: bool = False):
        super(ClashOfClansAPI, self).__init__('https://api.clashofclans.com', 'v1', api_key, debug)
    
    # clans
    async def get_clan_war_league_group(self, clanTag: str) -> types.clans.ClanWarLeagueGroup:
        """
        Retrieve information about clan's current clan war league group.
        
        `Original method <https://developer.clashofclans.com/api-docs/index.html#!/clans/getClanWarLeagueGroup>`_.
        
        :param clanTag:
        :type clanTag: str
        :return:
        :rtype: :class:`~types.clans.ClanWarLeagueGroup`
        """
        
        return await self.create_object(
            await self.make_api_request(
                f'/clans/{clanTag}/currentwar/leaguegroup',
            ),
            types.clans.ClanWarLeagueGroup
        )
    
    async def get_clan_war_league_war(self, warTag: str) -> types.clans.ClanWarLeagueGroup:
        """
        Retrieve information about individual clan war league war.
        
        `Original method <https://developer.clashofclans.com/api-docs/index.html#!/clans/getClanWarLeagueWar>`_.
        
        :param warTag:
        :type warTag: str
        :return:
        :rtype: :class:`~types.clans.ClanWarLeagueGroup`
        """
        
        return await self.create_object(
            await self.make_api_request(
                f'/clanwarleagues/wars/{warTag}',
            ),
            types.clans.ClanWarLeagueGroup
        )
    
    async def get_clan_war_log(self, clanTag: str, limit: Optional[int] = None, after: Optional[str] = None,
                               before: Optional[str] = None) -> Page[types.clans.ClanWarLogEntry]:
        """
        Retrieve clan's clan war log.
        
        `Original method <https://developer.clashofclans.com/api-docs/index.html#!/clans/getClanWarLog>`_.
        
        :param clanTag:
        :param limit:
        :param after:
        :param before:
        :type clanTag: str
        :type limit: Optional[int]
        :type after: Optional[str]
        :type before: Optional[str]
        :return:
        :rtype: :class:`Page` [:class:`~types.clans.ClanWarLeagueGroup`]
        """
        
        return await self.create_object(
            await self.make_api_request(
                f'/clans/{clanTag}/warlog',
                limit = limit,
                after = after,
                before = before
            ),
            page_generic_type = types.clans.ClanWarLogEntry
        )
    
    async def search_clans(self, name: Optional[str] = None, warFrequency: Optional[str] = None,
                           locationId: Optional[int] = None, minMembers: Optional[int] = None,
                           maxMembers: Optional[int] = None, minClanPoints: Optional[int] = None,
                           minClanLevel: Optional[int] = None, limit: Optional[int] = None, after: Optional[str] = None,
                           before: Optional[str] = None, labelIds: Optional[str] = None) -> Page[types.clans.Clan]:
        """
        Search all clans by name and/or filtering the results using various criteria.
        At least one filtering criteria must be defined and if name is used as part of search,
        it is required to be at least three characters long. It is not possible to specify ordering for results
        so clients should not rely on any specific ordering as that may change in the future releases of the API.
        
        `Original method <https://developer.clashofclans.com/api-docs/index.html#!/clans/searchClans>`_.
        
        :param name:
        :param warFrequency:
        :param locationId:
        :param minMembers:
        :param maxMembers:
        :param minClanPoints:
        :param minClanLevel:
        :param limit:
        :param after:
        :param before:
        :param labelIds:
        :type name: str
        :type warFrequency: str
        :type locationId: int
        :type minMembers: int
        :type maxMembers: int
        :type minClanPoints: int
        :type minClanLevel: int
        :type limit: int
        :type after: str
        :type before: str
        :type labelIds: str
        :return:
        :rtype: :class:`Page` [:class:`~types.clans.Clan`]
        """
        
        return await self.create_object(
            await self.make_api_request(
                f'/clans',
                name = name,
                warFrequency = warFrequency,
                locationId = locationId,
                minMembers = minMembers,
                maxMembers = maxMembers,
                minClanPoints = minClanPoints,
                minClanLevel = minClanLevel,
                limit = limit,
                after = after,
                before = before,
                labelIds = labelIds
            ),
            page_generic_type = types.clans.Clan
        )
    
    async def get_current_war(self, clanTag: str) -> types.clans.ClanWar:
        """
        Retrieve information about clan's current clan war.

        `Original method <https://developer.clashofclans.com/api-docs/index.html#!/clans/getCurrentWar>`_.

        :param clanTag:
        :type clanTag: str
        :return:
        :rtype: :class:`~types.clans.ClanWar`
        """
        
        return await self.create_object(
            await self.make_api_request(
                f'/clans/{clanTag}/currentwar',
            ),
            types.clans.ClanWar
        )
    
    async def get_clan(self, clanTag: str) -> types.clans.Clan:
        """
        Get information about a single clan by clan tag. Clan tags can be found using clan search operation.

        `Original method <https://developer.clashofclans.com/api-docs/index.html#!/clans/getClan>`_.

        :param clanTag:
        :type clanTag: str
        :return:
        :rtype: :class:`~types.clans.Clan`
        """
        
        return await self.create_object(
            await self.make_api_request(
                f'/clans/{clanTag}',
            ),
            types.clans.Clan
        )
    
    async def get_clan_members(self, clanTag: str, limit: Optional[int] = None, after: Optional[str] = None,
                               before: Optional[str] = None) -> Page[types.clans.ClanMember]:
        """
        List clan members.
        
        `Original method <https://developer.clashofclans.com/api-docs/index.html#!/clans/getClanMembers>`_.
        
        :param clanTag:
        :param limit:
        :param after:
        :param before:
        :type clanTag: str
        :type limit: Optional[int]
        :type after: Optional[str]
        :type before: Optional[str]
        :return:
        :rtype: :class:`Page` [:class:`~types.clans.ClanMember`]
        """
        
        return await self.create_object(
            await self.make_api_request(
                f'/clans/{clanTag}/members',
                limit = limit,
                after = after,
                before = before
            ),
            page_generic_type = types.clans.ClanMember
        )
    
    # players
    
    # leagues
    
    # lications
    
    # goldpass
    
    # labels
