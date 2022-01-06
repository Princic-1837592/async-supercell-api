from typing import Any, Dict, Optional
from ...types import SupercellApiResponse
from .leagues import PlayerRankingClan


class ClanRanking(SupercellApiResponse):
    def __init__(self, clanPoints: Optional[int] = None, clanLevel: Optional[int] = None,
                 location: Optional[dict] = None, members: Optional[int] = None, tag: Optional[str] = None,
                 name: Optional[str] = None, rank: Optional[int] = None, previousRank: Optional[int] = None,
                 badgeUrls: Optional[Dict[str, Any]] = None, **kwargs):
        super().__init__(**kwargs)
        self.clanPoints = clanPoints
        self.clanLevel = clanLevel
        self.location = None if location is None else Location(**location)
        self.members = members
        self.tag = tag
        self.name = name
        self.rank = rank
        self.previousRank = previousRank
        self.badgeUrls = badgeUrls


class Location(SupercellApiResponse):
    def __init__(self, localizedName: Optional[str] = None, id: Optional[int] = None, name: Optional[str] = None,
                 isCountry: Optional[bool] = None, countryCode: Optional[str] = None, **kwargs):
        super().__init__(**kwargs)
        self.localizedName = localizedName
        self.id = id
        self.name = name
        self.isCountry = isCountry
        self.countryCode = countryCode


class ClanVersusRanking(SupercellApiResponse):
    def __init__(self, clanPoints: Optional[int] = None, clanVersusPoints: Optional[int] = None, **kwargs):
        super().__init__(**kwargs)
        self.clanPoints = clanPoints
        self.clanVersusPoints = clanVersusPoints


class PlayerVersusRanking(SupercellApiResponse):
    def __init__(self, clan: Optional[dict] = None, versusBattleWins: Optional[int] = None, tag: Optional[str] = None,
                 name: Optional[str] = None, expLevel: Optional[int] = None, rank: Optional[int] = None,
                 previousRank: Optional[int] = None, versusTrophies: Optional[int] = None, **kwargs):
        super().__init__(**kwargs)
        self.clan = None if clan is None else PlayerRankingClan(**clan)
        self.versusBattleWins = versusBattleWins
        self.tag = tag
        self.name = name
        self.expLevel = expLevel
        self.rank = rank
        self.previousRank = previousRank
        self.versusTrophies = versusTrophies
