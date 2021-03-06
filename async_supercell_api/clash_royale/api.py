from typing import List, Optional
from . import types
from ..api import SupercellAPI
from ..types import Page


class ClashRoyaleAPI(SupercellAPI):
    """
    Class to interact with Clash Royale APIs
    
    :param api_key: 
    :param debug: in case you want the class to print every url and response status. Default (and suggested) False
    :type api_key: str
    :type debug: Optional[bool]
    """
    
    def __init__(self, api_key: str, debug: bool = False):
        super(ClashRoyaleAPI, self).__init__('https://api.clashroyale.com', 'v1', api_key, debug)
    
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
        :type clanTag: str
        :type limit: Optional[int]
        :type after: Optional[str]
        :type before: Optional[str]
        :return:
        :rtype: :class:`Page` [:class:`~types.clans.ClanWarLogEntry`]
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
        :type name: Optional[str]
        :type locationId: Optional[int]
        :type minMembers: Optional[int]
        :type maxMembers: Optional[int]
        :type minScore: Optional[int]
        :type limit: Optional[int]
        :type after: Optional[str]
        :type before: Optional[str]
        :return:
        :rtype: :class:`Page`[:class:`~types.clans.Clan`]
        """
        
        return await self.create_object(
            await self.make_api_request(
                '/clans',
                name = name,
                locationId = locationId,
                minMembers = minMembers,
                maxMembers = maxMembers,
                minScore = minScore,
                limit = limit,
                after = after,
                before = before
            ),
            page_generic_type = types.clans.Clan
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
        :type clanTag: str
        :type limit: Optional[int]
        :type after: Optional[str]
        :type before: Optional[str]
        :return:
        :rtype: :class:`Page`[:class:`~types.clans.RiverRaceLogEntry`]
        """
        
        return await self.create_object(
            await self.make_api_request(
                f'/clans/{clanTag}/riverracelog',
                limit = limit,
                after = after,
                before = before,
            ),
            page_generic_type = types.clans.RiverRaceLogEntry
        )
    
    async def get_current_war(self, clanTag: str) -> types.clans.CurrentClanWar:
        """
        Retrieve information about clan's current clan war.
        
        `Original method <https://developer.clashroyale.com/api-docs/index.html#!/clans/getCurrentWar>`_.
        
        :param clanTag:
        :type clanTag: str
        :return:
        """
        
        return await self.create_object(
            await self.make_api_request(
                f'/clans/{clanTag}/currentwar'
            ),
            types.clans.CurrentClanWar
        )
    
    async def get_clan(self, clanTag: str) -> types.clans.Clan:
        """
        Get information about a single clan by clan tag. Clan tags can be found using clan search operation.
        
        `Original method <https://developer.clashroyale.com/api-docs/index.html#!/clans/getClan>`_.
        
        :param clanTag:
        :type clanTag: str
        :return:
        """
        
        return await self.create_object(
            await self.make_api_request(
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
        :type clanTag: str
        :type limit: Optional[int]
        :type after: Optional[str]
        :type before: Optional[str]
        :return:
        :rtype: :class:`Page`[:class:`~types.clans.ClanMember`]
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
    
    async def get_current_river_race(self, clanTag: str) -> types.clans.CurrentRiverRace:
        """
        Retrieve information about clan's current river race.
        
        `Original method <https://developer.clashroyale.com/api-docs/index.html#!/clans/getCurrentRiverRace>`_.
        
        :param clanTag:
        :type clanTag: str
        :return:
        """
        
        return await self.create_object(
            await self.make_api_request(
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
        :type playerTag: str
        :return:
        """
        
        return await self.create_object(
            await self.make_api_request(
                f'/players/{playerTag}'
            ),
            types.players.Player
        )
    
    async def get_player_upcoming_chests(self, playerTag: str) -> types.players.UpcomingChests:
        """
        Get list of reward chests that the player will receive next in the game.
        
        `Original method <https://developer.clashroyale.com/api-docs/index.html#!/players/getPlayerUpcomingChests>`_.
        
        :param playerTag:
        :type playerTag: str
        :return:
        """
        
        return await self.create_object(
            await self.make_api_request(
                f'/players/{playerTag}/upcomingchests'
            ),
            types.players.UpcomingChests
        )
    
    async def get_player_battles(self, playerTag: str) -> List[types.players.Battle]:
        """
        Get list of recent battles for a player.
        
        `Original method <https://developer.clashroyale.com/api-docs/index.html#!/players/getPlayerBattles>`_.
        
        :param playerTag:
        :type playerTag: str
        :return:
        :rtype: List[:class:`~types.players.Battle`]
        """
        
        return await self.create_object(
            await self.make_api_request(
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
        :type limit: Optional[int]
        :type after: Optional[str]
        :type before: Optional[str]
        :return:
        :rtype: :class:`Page`[:class:`~types.players.Item`]
        """
        
        return await self.create_object(
            await self.make_api_request(
                '/cards',
                limit = limit,
                after = after,
                before = before
            ),
            page_generic_type = types.players.Item
        )
    
    # tournaments
    async def search_tournaments(self, name: Optional[str] = None, limit: Optional[int] = None,
                                 after: Optional[str] = None, before: Optional[str] = None) -> Page[
        types.tournaments.TournamentHeader]:
        """
        Search all tournaments by name. It is not possible to specify ordering for results
        so clients should not rely on any specific ordering as that may change in the future releases of the API.
        
        `Original method <https://developer.clashroyale.com/api-docs/index.html#!/tournaments/searchTournaments>`_.
        
        :param name:
        :param limit:
        :param after:
        :param before:
        :type name: Optional[str]
        :type limit: Optional[int]
        :type after: Optional[str]
        :type before: Optional[str]
        :return:
        :rtype: :class:`Page`[:class:`~types.tournaments.TournamentHeader`]
        """
        
        return await self.create_object(
            await self.make_api_request(
                '/tournaments',
                name = name,
                limit = limit,
                after = after,
                before = before
            ),
            page_generic_type = types.tournaments.TournamentHeader
        )
    
    async def get_tournament(self, tournamentTag: str) -> types.tournaments.Tournament:
        """
        Get information about a single tournament by a tournament tag.
        
        `Original method <https://developer.clashroyale.com/api-docs/index.html#!/tournaments/getTournament>`_.
        
        :param tournamentTag:
        :type tournamentTag: str
        :return:
        """
        
        return await self.create_object(
            await self.make_api_request(
                f'/tournaments/{tournamentTag}'
            ),
            types.tournaments.Tournament
        )
    
    # locations
    async def get_clan_ranking(self, locationId: str, limit: Optional[int] = None, after: Optional[str] = None,
                               before: Optional[str] = None) -> Page[types.locations.ClanRanking]:
        """
        Get clan rankings for a specific location.
        
        `Original method <https://developer.clashroyale.com/api-docs/index.html#!/locations/getClanRanking>`_.
        
        :param locationId:
        :param limit:
        :param after:
        :param before:
        :type locationId: str
        :type limit: Optional[int]
        :type after: Optional[str]
        :type before: Optional[str]
        :return:
        :rtype: :class:`Page`[:class:`~types.locations.ClanRanking`]
        """
        
        return await self.create_object(
            await self.make_api_request(
                f'/locations/{locationId}/rankings/clans',
                limit = limit,
                after = after,
                before = before
            ),
            page_generic_type = types.locations.ClanRanking
        )
    
    async def get_player_ranking(self, locationId: str, limit: Optional[int] = None, after: Optional[str] = None,
                                 before: Optional[str] = None) -> Page[types.locations.PlayerRanking]:
        """
        Get player rankings for a specific location.
        
        `Original method <https://developer.clashroyale.com/api-docs/index.html#!/locations/getPlayerRanking>`_.
        
        :param locationId:
        :param limit:
        :param after:
        :param before:
        :type locationId: str
        :type limit: Optional[int]
        :type after: Optional[str]
        :type before: Optional[str]
        :return:
        :rtype: :class:`Page`[:class:`~types.locations.PlayerRanking`]
        """
        
        return await self.create_object(
            await self.make_api_request(
                f'/locations/{locationId}/rankings/players',
                limit = limit,
                after = after,
                before = before
            ),
            page_generic_type = types.locations.PlayerRanking
        )
    
    async def get_clan_wars_ranking(self, locationId: str, limit: Optional[int] = None, after: Optional[str] = None,
                                    before: Optional[str] = None) -> Page[types.locations.ClanRanking]:
        """
        Get clan war rankings for a specific location.
        
        `Original method <https://developer.clashroyale.com/api-docs/index.html#!/locations/getClanWarsRanking>`_.
        
        :param locationId:
        :param limit:
        :param after:
        :param before:
        :type locationId: str
        :type limit: Optional[int]
        :type after: Optional[str]
        :type before: Optional[str]
        :return:
        :rtype: :class:`Page`[:class:`~types.locations.ClanRanking`]
        """
        
        return await self.create_object(
            await self.make_api_request(
                f'/locations/{locationId}/rankings/clanwars',
                limit = limit,
                after = after,
                before = before
            ),
            page_generic_type = types.locations.ClanRanking
        )
    
    async def get_top_player_league_season_handler(self, seasonId: str) -> types.locations.LeagueSeason:
        """
        Get top player league season.
        
        ``IMPORTANT`` I don't know how this endpoint works since the documentation is missing.
        
        `Original method <https://developer.clashroyale.com/api-docs/index.html#!/locations/getTopPlayerLeagueSeasonHandler>`_.
        
        :param seasonId:
        :type seasonId: str
        :return:
        """
        
        return await self.create_object(
            await self.make_api_request(
                f'/locations/global/seasons/{seasonId}',
            ),
            types.locations.LeagueSeason
        )
    
    async def get_top_player_league_season_rankings(self, seasonId: str, limit: Optional[int] = None,
                                                    after: Optional[str] = None, before: Optional[str] = None) -> Page[
        types.locations.PlayerRanking]:
        """
        Get top player rankings for a season.
        
        `Original method <https://developer.clashroyale.com/api-docs/index.html#!/locations/getTopPlayerLeagueSeasonRankings>`_.
        
        :param seasonId:
        :param limit:
        :param after:
        :param before:
        :type seasonId: str
        :type limit: Optional[int]
        :type after: Optional[str]
        :type before: Optional[str]
        :return:
        :rtype: :class:`Page`[:class:`~types.locations.PlayerRanking`]
        """
        
        return await self.create_object(
            await self.make_api_request(
                f'/locations/global/seasons/{seasonId}/rankings/players',
                limit = limit,
                after = after,
                before = before
            ),
            page_generic_type = types.locations.PlayerRanking
        )
    
    async def list_top_player_league_seasons_handler(self, limit: Optional[int] = None, after: Optional[str] = None,
                                                     before: Optional[str] = None) -> Page[
        types.locations.LeagueSeason]:
        """
        Lists top player league seasons.
        
        `Original method <https://developer.clashroyale.com/api-docs/index.html#!/locations/listTopPlayerLeagueSeasonsHandler>`_.
        
        :param limit:
        :param after:
        :param before:
        :type limit: Optional[int]
        :type after: Optional[str]
        :type before: Optional[str]
        :return:
        :rtype: :class:`Page`[:class:`~types.locations.LeagueSeason`]
        """
        
        return await self.create_object(
            await self.make_api_request(
                f'/locations/global/seasons',
                limit = limit,
                after = after,
                before = before
            ),
            page_generic_type = types.locations.LeagueSeason
        )
    
    async def get_locations(self, limit: Optional[int] = None, after: Optional[str] = None,
                            before: Optional[str] = None) -> Page[types.locations.Location]:
        """
        List locations.
        
        `Original method <https://developer.clashroyale.com/api-docs/index.html#!/locations/getLocations>`_.
        
        :param limit:
        :param after:
        :param before:
        :type limit: Optional[int]
        :type after: Optional[str]
        :type before: Optional[str]
        :return:
        :rtype: :class:`Page`[:class:`~types.locations.Location`]
        """
        
        return await self.create_object(
            await self.make_api_request(
                f'/locations',
                limit = limit,
                after = after,
                before = before
            ),
            page_generic_type = types.locations.Location
        )
    
    async def get_location(self, locationId: int) -> types.locations.Location:
        """
        Get information about specific location.
        
        `Original method <https://developer.clashroyale.com/api-docs/index.html#!/locations/getLocation>`_.
        
        :param locationId:
        :type locationId: str
        :return:
        """
        
        return await self.create_object(
            await self.make_api_request(
                f'/locations/{locationId}'
            ),
            types.locations.Location
        )
    
    async def get_global_tournament_ranking(self, tournamentTag: str, limit: Optional[int] = None,
                                            after: Optional[str] = None, before: Optional[str] = None) -> Page[
        types.locations.LadderTournamentRanking]:
        """
        Get global tournament rankings.
        
        `Original method <https://developer.clashroyale.com/api-docs/index.html#!/locations/getGlobalTournamentRanking>`_.
        
        :param tournamentTag:
        :param limit:
        :param after:
        :param before:
        :type tournamentTag: str
        :type limit: Optional[int]
        :type after: Optional[str]
        :type before: Optional[str]
        :return:
        :rtype: :class:`Page`[:class:`~types.locations.LadderTournamentRanking`]
        """
        
        return await self.create_object(
            await self.make_api_request(
                f'/locations/global/rankings/tournaments/{tournamentTag}',
                limit = limit,
                after = after,
                before = before
            ),
            page_generic_type = types.locations.LadderTournamentRanking
        )
    
    # globaltournaments
    async def get_global_tournaments(self) -> List[types.global_tournaments.LadderTournament]:
        """
        Get list of global tournaments.
        
        `Original method <https://developer.clashroyale.com/api-docs/index.html#!/globaltournaments/getGlobalTournaments>`_.
        
        :return:
        :rtype: List[:class:`~types.global_tournaments.LadderTournament`]
        """
        
        return await self.create_object(
            await self.make_api_request(
                f'/globaltournaments'
            ),
            types.global_tournaments.LadderTournament
        )
