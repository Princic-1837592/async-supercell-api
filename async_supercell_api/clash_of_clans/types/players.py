from typing import Any, Dict, List, Optional
from ...types import SupercellApiResponse
from .leagues import League
from .labels import Label


class Player(SupercellApiResponse):
    def __init__(self, league: Optional[dict] = None, clan: Optional[dict] = None, role: Optional[str] = None,
                 warPreference: Optional[str] = None, attackWins: Optional[int] = None,
                 defenseWins: Optional[int] = None, townHallLevel: Optional[int] = None,
                 townHallWeaponLevel: Optional[int] = None, versusBattleWins: Optional[int] = None,
                 legendStatistics: Optional[dict] = None, troops: Optional[List[dict]] = None,
                 heroes: Optional[List[dict]] = None, spells: Optional[List[dict]] = None,
                 labels: Optional[List[dict]] = None, tag: Optional[str] = None, name: Optional[str] = None,
                 expLevel: Optional[int] = None, trophies: Optional[int] = None, bestTrophies: Optional[int] = None,
                 donations: Optional[int] = None, donationsReceived: Optional[int] = None,
                 builderHallLevel: Optional[int] = None, versusTrophies: Optional[int] = None,
                 bestVersusTrophies: Optional[int] = None, warStars: Optional[int] = None,
                 achievements: Optional[List[dict]] = None, versusBattleWinCount: Optional[int] = None, **kwargs):
        super().__init__(**kwargs)
        self.league = None if league is None else League(**league)
        self.clan = None if clan is None else PlayerClan(**clan)
        self.role = role
        self.warPreference = warPreference
        self.attackWins = attackWins
        self.defenseWins = defenseWins
        self.townHallLevel = townHallLevel
        self.townHallWeaponLevel = townHallWeaponLevel
        self.versusBattleWins = versusBattleWins
        self.legendStatistics = None if legendStatistics is None else PlayerLegendStatistics(**legendStatistics)
        self.troops = None if troops is None else list(map(lambda x: PlayerItemLevel(**x), troops))
        self.heroes = None if heroes is None else list(map(lambda x: PlayerItemLevel(**x), heroes))
        self.spells = None if spells is None else list(map(lambda x: PlayerItemLevel(**x), spells))
        self.labels = None if labels is None else list(map(lambda x: Label(**x), labels))
        self.tag = tag
        self.name = name
        self.expLevel = expLevel
        self.trophies = trophies
        self.bestTrophies = bestTrophies
        self.donations = donations
        self.donationsReceived = donationsReceived
        self.builderHallLevel = builderHallLevel
        self.versusTrophies = versusTrophies
        self.bestVersusTrophies = bestVersusTrophies
        self.warStars = warStars
        self.achievements = None if achievements is None else list(
            map(lambda x: PlayerAchievementProgress(**x), achievements)
        )
        self.versusBattleWinCount = versusBattleWinCount


class PlayerClan(SupercellApiResponse):
    def __init__(self, tag: Optional[str] = None, clanLevel: Optional[int] = None, name: Optional[str] = None,
                 badgeUrls: Optional[Dict[str, Any]] = None, **kwargs):
        super().__init__(**kwargs)
        self.tag = tag
        self.clanLevel = clanLevel
        self.name = name
        self.badgeUrls = badgeUrls


class PlayerLegendStatistics(SupercellApiResponse):
    def __init__(self, legendTrophies: Optional[int] = None, previousVersusSeason: Optional[dict] = None,
                 previousSeason: Optional[dict] = None, bestSeason: Optional[dict] = None,
                 currentSeason: Optional[dict] = None, bestVersusSeason: Optional[dict] = None, **kwargs):
        super().__init__(**kwargs)
        self.legendTrophies = legendTrophies
        self.previousVersusSeason = None if previousVersusSeason is None else LegendLeagueTournamentSeasonResult(
            **previousVersusSeason
        )
        self.previousSeason = None if previousSeason is None else LegendLeagueTournamentSeasonResult(**previousSeason)
        self.bestSeason = None if bestSeason is None else LegendLeagueTournamentSeasonResult(**bestSeason)
        self.currentSeason = None if currentSeason is None else LegendLeagueTournamentSeasonResult(**currentSeason)
        self.bestVersusSeason = None if bestVersusSeason is None else LegendLeagueTournamentSeasonResult(
            **bestVersusSeason
        )


class LegendLeagueTournamentSeasonResult(SupercellApiResponse):
    def __init__(self, trophies: Optional[int] = None, id: Optional[str] = None, rank: Optional[int] = None, **kwargs):
        super().__init__(**kwargs)
        self.trophies = trophies
        self.id = id
        self.rank = rank


class PlayerItemLevel(SupercellApiResponse):
    def __init__(self, level: Optional[int] = None, name: Optional[str] = None, maxLevel: Optional[int] = None,
                 village: Optional[str] = None, superTroopIsActive: Optional[bool] = None, **kwargs):
        super().__init__(**kwargs)
        self.level = level
        self.name = name
        self.maxLevel = maxLevel
        self.village = village
        self.superTroopIsActive = superTroopIsActive


class PlayerAchievementProgress(SupercellApiResponse):
    def __init__(self, stars: Optional[int] = None, value: Optional[int] = None, name: Optional[str] = None,
                 target: Optional[int] = None, info: Optional[str] = None, completionInfo: Optional[str] = None,
                 village: Optional[str] = None, **kwargs):
        super().__init__(**kwargs)
        self.stars = stars
        self.value = value
        self.name = name
        self.target = target
        self.info = info
        self.completionInfo = completionInfo
        self.village = village


class VerifyTokenResponse(SupercellApiResponse):
    def __init__(self, tag: Optional[str] = None, token: Optional[str] = None, status: Optional[str] = None, **kwargs):
        super().__init__(**kwargs)
        self.tag = tag
        self.token = token
        self.status = status
