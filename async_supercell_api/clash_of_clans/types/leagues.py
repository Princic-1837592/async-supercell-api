from typing import Any, Dict, Optional
from ...types import SupercellApiResponse


class League(SupercellApiResponse):
    def __init__(self, name: Optional[str] = None, id: Optional[int] = None, iconUrls: Optional[Dict[str, Any]] = None,
                 **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.id = id
        self.iconUrls = iconUrls


class PlayerRanking(SupercellApiResponse):
    def __init__(self, league: Optional[dict] = None, clan: Optional[dict] = None, attackWins: Optional[int] = None,
                 defenseWins: Optional[int] = None, tag: Optional[str] = None, name: Optional[str] = None,
                 expLevel: Optional[int] = None, rank: Optional[int] = None, previousRank: Optional[int] = None,
                 trophies: Optional[int] = None, **kwargs):
        super().__init__(**kwargs)
        self.league = None if league is None else League(**league)
        self.clan = None if clan is None else PlayerRankingClan(**clan)
        self.attackWins = attackWins
        self.defenseWins = defenseWins
        self.tag = tag
        self.name = name
        self.expLevel = expLevel
        self.rank = rank
        self.previousRank = previousRank
        self.trophies = trophies


class PlayerRankingClan(SupercellApiResponse):
    def __init__(self, tag: Optional[str] = None, name: Optional[str] = None,
                 badgeUrls: Optional[Dict[str, Any]] = None, **kwargs):
        super().__init__(**kwargs)
        self.tag = tag
        self.name = name
        self.badgeUrls = badgeUrls


class LeagueSeason(SupercellApiResponse):
    def __init__(self, id: Optional[str] = None, **kwargs):
        super().__init__(**kwargs)
        self.id = id


class WarLeague(SupercellApiResponse):
    def __init__(self, name: Optional[str] = None, id: Optional[int] = None, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.id = id
