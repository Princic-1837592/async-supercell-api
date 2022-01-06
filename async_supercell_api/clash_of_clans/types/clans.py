from typing import Any, Dict, List, Optional
from ...types import SupercellApiResponse
from .locations import Location
from .leagues import League, WarLeague
from .labels import Label


class ClanWarLeagueGroup(SupercellApiResponse):
    def __init__(self, tag: Optional[str] = None, state: Optional[str] = None, season: Optional[str] = None,
                 clans: Optional[List[dict]] = None, rounds: Optional[List[dict]] = None, **kwargs):
        super().__init__(**kwargs)
        self.tag = tag
        self.state = state
        self.season = season
        self.clans = None if clans is None else list(map(lambda x: ClanWarLeagueClan(**x), clans))
        self.rounds = None if rounds is None else list(map(lambda x: ClanWarLeagueRound(**x), rounds))


class ClanWarLeagueClan(SupercellApiResponse):
    def __init__(self, tag: Optional[str] = None, clanLevel: Optional[int] = None, name: Optional[str] = None,
                 members: Optional[List[dict]] = None, badgeUrls: Optional[Dict[str, Any]] = None, **kwargs):
        super().__init__(**kwargs)
        self.tag = tag
        self.clanLevel = clanLevel
        self.name = name
        self.members = None if members is None else list(map(lambda x: ClanWarLeagueClanMember(**x), members))
        self.badgeUrls = badgeUrls


class ClanWarLeagueRound(SupercellApiResponse):
    def __init__(self, warTags: Optional[List[str]] = None, **kwargs):
        super().__init__(**kwargs)
        self.warTags = warTags


class ClanWarLeagueClanMember(SupercellApiResponse):
    def __init__(self, tag: Optional[str] = None, townHallLevel: Optional[int] = None, name: Optional[str] = None,
                 **kwargs):
        super().__init__(**kwargs)
        self.tag = tag
        self.townHallLevel = townHallLevel
        self.name = name


class ClanWarLogEntry(SupercellApiResponse):
    def __init__(self, clan: Optional[dict] = None, teamSize: Optional[int] = None,
                 attacksPerMember: Optional[int] = None, opponent: Optional[dict] = None, endTime: Optional[str] = None,
                 result: Optional[str] = None, **kwargs):
        super().__init__(**kwargs)
        self.clan = None if clan is None else WarClan(**clan)
        self.teamSize = teamSize
        self.attacksPerMember = attacksPerMember
        self.opponent = None if opponent is None else WarClan(**opponent)
        self.endTime = endTime
        self.result = result


class WarClan(SupercellApiResponse):
    def __init__(self, destructionPercentage: Optional[float] = None, tag: Optional[str] = None,
                 name: Optional[str] = None, badgeUrls: Optional[Dict[str, Any]] = None,
                 clanLevel: Optional[int] = None, attacks: Optional[int] = None, stars: Optional[int] = None,
                 expEarned: Optional[int] = None, members: Optional[List[dict]] = None, **kwargs):
        super().__init__(**kwargs)
        self.destructionPercentage = destructionPercentage
        self.tag = tag
        self.name = name
        self.badgeUrls = badgeUrls
        self.clanLevel = clanLevel
        self.attacks = attacks
        self.stars = stars
        self.expEarned = expEarned
        self.members = None if members is None else list(map(lambda x: ClanWarMember(**x), members))


class ClanWarMember(SupercellApiResponse):
    def __init__(self, tag: Optional[str] = None, name: Optional[str] = None, mapPosition: Optional[int] = None,
                 townhallLevel: Optional[int] = None, opponentAttacks: Optional[int] = None,
                 bestOpponentAttack: Optional[dict] = None, attacks: Optional[List[dict]] = None, **kwargs):
        super().__init__(**kwargs)
        self.tag = tag
        self.name = name
        self.mapPosition = mapPosition
        self.townhallLevel = townhallLevel
        self.opponentAttacks = opponentAttacks
        self.bestOpponentAttack = None if bestOpponentAttack is None else ClanWarAttack(**bestOpponentAttack)
        self.attacks = None if attacks is None else list(map(lambda x: ClanWarAttack(**x), attacks))


class ClanWarAttack(SupercellApiResponse):
    def __init__(self, order: Optional[int] = None, attackerTag: Optional[str] = None,
                 defenderTag: Optional[str] = None, stars: Optional[int] = None,
                 destructionPercentage: Optional[int] = None, duration: Optional[int] = None, **kwargs):
        super().__init__(**kwargs)
        self.order = order
        self.attackerTag = attackerTag
        self.defenderTag = defenderTag
        self.stars = stars
        self.destructionPercentage = destructionPercentage
        self.duration = duration


class Clan(SupercellApiResponse):
    def __init__(self, warLeague: Optional[dict] = None, memberList: Optional[List[dict]] = None,
                 tag: Optional[str] = None, requiredVersusTrophies: Optional[int] = None,
                 requiredTownhallLevel: Optional[int] = None, warLosses: Optional[int] = None,
                 clanPoints: Optional[int] = None, warFrequency: Optional[str] = None,
                 warWinStreak: Optional[int] = None, clanLevel: Optional[int] = None, warTies: Optional[int] = None,
                 warWins: Optional[int] = None, clanVersusPoints: Optional[int] = None,
                 chatLanguage: Optional[dict] = None, isWarLogPublic: Optional[bool] = None,
                 requiredTrophies: Optional[int] = None, labels: Optional[List[dict]] = None,
                 name: Optional[str] = None, location: Optional[dict] = None, type: Optional[str] = None,
                 members: Optional[int] = None, description: Optional[str] = None,
                 badgeUrls: Optional[Dict[str, Any]] = None, **kwargs):
        super().__init__(**kwargs)
        self.warLeague = None if warLeague is None else WarLeague(**warLeague)
        self.memberList = None if memberList is None else list(map(lambda x: ClanMember(**x), memberList))
        self.tag = tag
        self.requiredVersusTrophies = requiredVersusTrophies
        self.requiredTownhallLevel = requiredTownhallLevel
        self.warLosses = warLosses
        self.clanPoints = clanPoints
        self.warFrequency = warFrequency
        self.warWinStreak = warWinStreak
        self.clanLevel = clanLevel
        self.warTies = warTies
        self.warWins = warWins
        self.clanVersusPoints = clanVersusPoints
        self.chatLanguage = None if chatLanguage is None else Language(**chatLanguage)
        self.isWarLogPublic = isWarLogPublic
        self.requiredTrophies = requiredTrophies
        self.labels = None if labels is None else list(map(lambda x: Label(**x), labels))
        self.name = name
        self.location = None if location is None else Location(**location)
        self.type = type
        self.members = members
        self.description = description
        self.badgeUrls = badgeUrls


class ClanWar(SupercellApiResponse):
    def __init__(self, clan: Optional[dict] = None, teamSize: Optional[int] = None,
                 attacksPerMember: Optional[int] = None, opponent: Optional[dict] = None,
                 startTime: Optional[str] = None, state: Optional[str] = None, endTime: Optional[str] = None,
                 preparationStartTime: Optional[str] = None, **kwargs):
        super().__init__(**kwargs)
        self.clan = None if clan is None else WarClan(**clan)
        self.teamSize = teamSize
        self.attacksPerMember = attacksPerMember
        self.opponent = None if opponent is None else WarClan(**opponent)
        self.startTime = startTime
        self.state = state
        self.endTime = endTime
        self.preparationStartTime = preparationStartTime


class Language(SupercellApiResponse):
    def __init__(self, name: Optional[str] = None, id: Optional[int] = None, languageCode: Optional[str] = None,
                 **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.id = id
        self.languageCode = languageCode


class ClanMember(SupercellApiResponse):
    def __init__(self, league: Optional[dict] = None, tag: Optional[str] = None, name: Optional[str] = None,
                 role: Optional[str] = None, expLevel: Optional[int] = None, clanRank: Optional[int] = None,
                 previousClanRank: Optional[int] = None, donations: Optional[int] = None,
                 donationsReceived: Optional[int] = None, trophies: Optional[int] = None,
                 versusTrophies: Optional[int] = None, **kwargs):
        super().__init__(**kwargs)
        self.league = None if league is None else League(**league)
        self.tag = tag
        self.name = name
        self.role = role
        self.expLevel = expLevel
        self.clanRank = clanRank
        self.previousClanRank = previousClanRank
        self.donations = donations
        self.donationsReceived = donationsReceived
        self.trophies = trophies
        self.versusTrophies = versusTrophies
