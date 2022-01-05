from typing import Any, Dict, List, Optional
from .clans import Arena, Location
from ...types import SupercellApiResponse


class ClanRanking(SupercellApiResponse):
    def __init__(self, clanScore: Optional[int] = None, badgeId: Optional[int] = None, location: Optional[dict] = None,
                 members: Optional[int] = None, tag: Optional[str] = None, name: Optional[str] = None,
                 rank: Optional[int] = None, previousRank: Optional[int] = None,
                 badgeUrls: Optional[Dict[str, Any]] = None, **kwargs):
        super().__init__(**kwargs)
        self.clanScore = clanScore
        self.badgeId = badgeId
        self.location = None if location is None else Location(**location)
        self.members = members
        self.tag = tag
        self.name = name
        self.rank = rank
        self.previousRank = previousRank
        self.badgeUrls = badgeUrls


class PlayerRanking(SupercellApiResponse):
    def __init__(self, clan: Optional[dict] = None, arena: Optional[dict] = None, tag: Optional[str] = None,
                 name: Optional[str] = None, expLevel: Optional[int] = None, rank: Optional[int] = None,
                 previousRank: Optional[int] = None, trophies: Optional[int] = None, **kwargs):
        super().__init__(**kwargs)
        self.clan = None if clan is None else PlayerRankingClan(**clan)
        self.arena = None if arena is None else Arena(**arena)
        self.tag = tag
        self.name = name
        self.expLevel = expLevel
        self.rank = rank
        self.previousRank = previousRank
        self.trophies = trophies


class PlayerRankingClan(SupercellApiResponse):
    def __init__(self, badgeId: Optional[int] = None, tag: Optional[str] = None, name: Optional[str] = None,
                 badgeUrls: Optional[Dict[str, Any]] = None, **kwargs):
        super().__init__(**kwargs)
        self.badgeId = badgeId
        self.tag = tag
        self.name = name
        self.badgeUrls = badgeUrls


class LeagueSeason(SupercellApiResponse):
    def __init__(self, id: Optional[str] = None, **kwargs):
        super().__init__(**kwargs)
        self.id = id


class LadderTournamentRanking(SupercellApiResponse):
    def __init__(self, clan: Optional[dict] = None, wins: Optional[int] = None, losses: Optional[int] = None,
                 tag: Optional[str] = None, name: Optional[str] = None, rank: Optional[int] = None,
                 previousRank: Optional[int] = None, **kwargs):
        super().__init__(**kwargs)
        self.clan = None if clan is None else PlayerRankingClan(**clan)
        self.wins = wins
        self.losses = losses
        self.tag = tag
        self.name = name
        self.rank = rank
        self.previousRank = previousRank
