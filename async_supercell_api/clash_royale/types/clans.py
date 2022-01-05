from typing import Any, Dict, List, Optional
from ...types import SupercellApiResponse


class ClanWarLogEntry(SupercellApiResponse):
    def __init__(self, standings: Optional[List[dict]] = None, seasonId: Optional[int] = None,
                 participants: Optional[List[dict]] = None, createdDate: Optional[str] = None, **kwargs):
        super().__init__(**kwargs)
        self.standings = None if standings is None else list(map(lambda x: ClanWarStanding(**x), standings))
        self.seasonId = seasonId
        self.participants = None if participants is None else list(map(lambda x: ClanWarParticipant(**x), participants))
        self.createdDate = createdDate


class ClanWarStanding(SupercellApiResponse):
    def __init__(self, trophyChange: Optional[int] = None, clan: Optional[dict] = None, **kwargs):
        super().__init__(**kwargs)
        self.trophyChange = trophyChange
        self.clan = None if clan is None else ClanWarClan(**clan)


class ClanWarParticipant(SupercellApiResponse):
    def __init__(self, tag: Optional[str] = None, name: Optional[str] = None, cardsEarned: Optional[int] = None,
                 battlesPlayed: Optional[int] = None, wins: Optional[int] = None,
                 collectionDayBattlesPlayed: Optional[int] = None,
                 numberOfBattles: Optional[int] = None, **kwargs):
        super().__init__(**kwargs)
        self.tag = tag
        self.name = name
        self.cardsEarned = cardsEarned
        self.battlesPlayed = battlesPlayed
        self.wins = wins
        self.collectionDayBattlesPlayed = collectionDayBattlesPlayed
        self.numberOfBattles = numberOfBattles


class ClanWarClan(SupercellApiResponse):
    def __init__(self, crowns: Optional[int] = None, tag: Optional[str] = None, clanScore: Optional[int] = None,
                 badgeId: Optional[int] = None,
                 name: Optional[str] = None, participants: Optional[int] = None, battlesPlayed: Optional[int] = None,
                 wins: Optional[int] = None,
                 **kwargs):
        super().__init__(**kwargs)
        self.crowns = crowns
        self.tag = tag
        self.clanScore = clanScore
        self.badgeId = badgeId
        self.name = name
        self.participants = participants
        self.battlesPlayed = battlesPlayed
        self.wins = wins


class Clan(SupercellApiResponse):
    def __init__(self, memberList: Optional[List[dict]] = None, tag: Optional[str] = None,
                 clanWarTrophies: Optional[int] = None,
                 requiredTrophies: Optional[int] = None, donationsPerWeek: Optional[int] = None,
                 clanScore: Optional[int] = None,
                 badgeId: Optional[int] = None, clanChestMaxLevel: Optional[int] = None,
                 clanChestStatus: Optional[str] = None,
                 clanChestLevel: Optional[int] = None, name: Optional[str] = None, location: Optional[dict] = None,
                 type: Optional[str] = None,
                 members: Optional[int] = None, description: Optional[str] = None,
                 clanChestPoints: Optional[int] = None,
                 badgeUrls: Optional[Dict[str, Any]] = None, **kwargs):
        super().__init__(**kwargs)
        self.memberList = None if memberList is None else list(map(lambda x: ClanMember(**x), memberList))
        self.tag = tag
        self.clanWarTrophies = clanWarTrophies
        self.requiredTrophies = requiredTrophies
        self.donationsPerWeek = donationsPerWeek
        self.clanScore = clanScore
        self.badgeId = badgeId
        self.clanChestMaxLevel = clanChestMaxLevel
        self.clanChestStatus = clanChestStatus
        self.clanChestLevel = clanChestLevel
        self.name = name
        self.location = None if memberList is None else Location(**location)
        self.type = type
        self.members = members
        self.description = description
        self.clanChestPoints = clanChestPoints
        self.badgeUrls = badgeUrls


class Location(SupercellApiResponse):
    def __init__(self, localizedName: Optional[str] = None, id: Optional[int] = None, name: Optional[str] = None,
                 isCountry: Optional[bool] = None,
                 countryCode: Optional[str] = None, **kwargs):
        super().__init__(**kwargs)
        self.localizedName = localizedName
        self.id = id
        self.name = name
        self.isCountry = isCountry
        self.countryCode = countryCode


class ClanMember(SupercellApiResponse):
    def __init__(self, clanChestPoints: Optional[int] = None, arena: Optional[dict] = None,
                 lastSeen: Optional[str] = None,
                 tag: Optional[str] = None, name: Optional[str] = None, role: Optional[str] = None,
                 expLevel: Optional[int] = None,
                 trophies: Optional[int] = None, clanRank: Optional[int] = None, previousClanRank: Optional[int] = None,
                 donations: Optional[int] = None, donationsReceived: Optional[int] = None, **kwargs):
        super().__init__(**kwargs)
        self.clanChestPoints = clanChestPoints
        self.arena = None if arena is None else Arena(**arena)
        self.lastSeen = lastSeen
        self.tag = tag
        self.name = name
        self.role = role
        self.expLevel = expLevel
        self.trophies = trophies
        self.clanRank = clanRank
        self.previousClanRank = previousClanRank
        self.donations = donations
        self.donationsReceived = donationsReceived


class Arena(SupercellApiResponse):
    def __init__(self, name: Optional[str] = None, id: Optional[int] = None, iconUrls: Optional[Dict[str, Any]] = None,
                 **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.id = id
        self.iconUrls = iconUrls


class RiverRaceLogEntry(SupercellApiResponse):
    def __init__(self, standings: Optional[List[dict]] = None, seasonId: Optional[int] = None,
                 createdDate: Optional[str] = None, sectionIndex: Optional[int] = None, **kwargs):
        super().__init__(**kwargs)
        self.standings = None if standings is None else list(map(lambda x: RiverRaceStanding(**x), standings))
        self.seasonId = seasonId
        self.createdDate = createdDate
        self.sectionIndex = sectionIndex


class RiverRaceStanding(SupercellApiResponse):
    def __init__(self, rank: Optional[int] = None, trophyChange: Optional[int] = None, clan: Optional[dict] = None,
                 **kwargs):
        super().__init__(**kwargs)
        self.rank = rank
        self.trophyChange = trophyChange
        self.clan = None if clan is None else RiverRaceClan(**clan)


class RiverRaceClan(SupercellApiResponse):
    def __init__(self, tag: Optional[str] = None, clanScore: Optional[int] = None, badgeId: Optional[int] = None,
                 name: Optional[str] = None,
                 fame: Optional[int] = None, repairPoints: Optional[int] = None, finishTime: Optional[str] = None,
                 participants: Optional[List[dict]] = None, periodPoints: Optional[int] = None, **kwargs):
        super().__init__(**kwargs)
        self.tag = tag
        self.clanScore = clanScore
        self.badgeId = badgeId
        self.name = name
        self.fame = fame
        self.repairPoints = repairPoints
        self.finishTime = finishTime
        self.participants = None if participants is None else list(
            map(lambda x: RiverRaceParticipant(**x), participants)
        )
        self.periodPoints = periodPoints


class RiverRaceParticipant(SupercellApiResponse):
    def __init__(self, tag: Optional[str] = None, name: Optional[str] = None, fame: Optional[int] = None,
                 repairPoints: Optional[int] = None,
                 boatAttacks: Optional[int] = None, decksUsed: Optional[int] = None,
                 decksUsedToday: Optional[int] = None, **kwargs):
        super().__init__(**kwargs)
        self.tag = tag
        self.name = name
        self.fame = fame
        self.repairPoints = repairPoints
        self.boatAttacks = boatAttacks
        self.decksUsed = decksUsed
        self.decksUsedToday = decksUsedToday


class CurrentClanWar(SupercellApiResponse):
    def __init__(self, state: Optional[str] = None, clan: Optional[dict] = None,
                 participants: Optional[List[dict]] = None, clans: Optional[List[dict]] = None,
                 collectionEndTime: Optional[str] = None, warEndTime: Optional[str] = None, **kwargs):
        super().__init__(**kwargs)
        self.state = state
        self.clan = None if clan is None else ClanWarClan(**clan)
        self.participants = None if participants is None else list(map(lambda x: ClanWarParticipant(**x), participants))
        self.clans = None if clans is None else list(map(lambda x: ClanWarClan(**x), clans))
        self.collectionEndTime = collectionEndTime
        self.warEndTime = warEndTime


class CurrentRiverRace(SupercellApiResponse):
    def __init__(self, state: Optional[str] = None, clan: Optional[dict] = None, clans: Optional[List[dict]] = None,
                 collectionEndTime: Optional[str] = None, warEndTime: Optional[str] = None,
                 sectionIndex: Optional[int] = None,
                 periodIndex: Optional[int] = None, periodType: Optional[str] = None,
                 periodLogs: Optional[List[dict]] = None, **kwargs):
        super().__init__(**kwargs)
        self.state = state
        self.clan = None if clan is None else RiverRaceClan(**clan)
        self.clans = None if clans is None else list(map(lambda x: RiverRaceClan(**x), clans))
        self.collectionEndTime = collectionEndTime
        self.warEndTime = warEndTime
        self.sectionIndex = sectionIndex
        self.periodIndex = periodIndex
        self.periodType = periodType
        self.periodLogs = None if periodLogs is None else list(map(lambda x: PeriodLog(**x), periodLogs))


class PeriodLog(SupercellApiResponse):
    def __init__(self, items: Optional[List[dict]] = None, periodIndex: Optional[int] = None, **kwargs):
        super().__init__(**kwargs)
        self.items = None if items is None else list(map(lambda x: PeriodLogEntry(**x), items))
        self.periodIndex = periodIndex


class PeriodLogEntry(SupercellApiResponse):
    def __init__(self, clan: Optional[dict] = None, pointsEarned: Optional[int] = None,
                 progressStartOfDay: Optional[int] = None,
                 progressEndOfDay: Optional[int] = None, endOfDayRank: Optional[int] = None,
                 progressEarned: Optional[int] = None,
                 numOfDefensesRemaining: Optional[int] = None, progressEarnedFromDefenses: Optional[int] = None,
                 **kwargs):
        super().__init__(**kwargs)
        self.clan = None if clan is None else PeriodLogEntryClan(**clan)
        self.pointsEarned = pointsEarned
        self.progressStartOfDay = progressStartOfDay
        self.progressEndOfDay = progressEndOfDay
        self.endOfDayRank = endOfDayRank
        self.progressEarned = progressEarned
        self.numOfDefensesRemaining = numOfDefensesRemaining
        self.progressEarnedFromDefenses = progressEarnedFromDefenses


class PeriodLogEntryClan(SupercellApiResponse):
    def __init__(self, tag: Optional[str] = None, **kwargs):
        super().__init__(**kwargs)
        self.tag = tag
