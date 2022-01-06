from typing import Any, Dict, List, Optional
from .clans import Arena
from ...types import SupercellApiResponse


class PlayerBattleData(SupercellApiResponse):
    def __init__(self, clan: Optional[dict] = None, cards: Optional[List[dict]] = None, tag: Optional[str] = None,
                 name: Optional[str] = None, startingTrophies: Optional[int] = None, trophyChange: Optional[int] = None,
                 crowns: Optional[int] = None, kingTowerHitPoints: Optional[int] = None,
                 princessTowersHitPoints: Optional[List[int]] = None, **kwargs):
        super().__init__(**kwargs)
        self.clan = None if clan is None else PlayerClan(**clan)
        self.cards = None if cards is None else list(map(lambda x: PlayerItemLevel(**x), cards))
        self.tag = tag
        self.name = name
        self.startingTrophies = startingTrophies
        self.trophyChange = trophyChange
        self.crowns = crowns
        self.kingTowerHitPoints = kingTowerHitPoints
        self.princessTowersHitPoints = princessTowersHitPoints


class GameMode(SupercellApiResponse):
    def __init__(self, id: Optional[int] = None, name: Optional[str] = None, **kwargs):
        super().__init__(**kwargs)
        self.id = id
        self.name = name


class Battle(SupercellApiResponse):
    """
    Type representing a battle.
    
    :param gameMode:
    :param arena:
    :param type:
    :param deckSelection:
    :param opponent:
    :param challengeWinCountBefore:
    :param boatBattleSide:
    :param boatBattleWon:
    :param newTowersDestroyed:
    :param prevTowersDestroyed:
    :param remainingTowers:
    :param team:
    :param battleTime:
    :param challengeId:
    :param tournamentTag:
    :param challengeTitle:
    :param isLadderTournament:
    :param isHostedMatch:
    :type gameMode: :class:`GameMode`
    :type arena: :class:`~.clans.Arena`
    :type type: str
    :type deckSelection: str
    :type opponent: :class:`PlayerBattleData`
    :type challengeWinCountBefore: int
    :type boatBattleSide: str
    :type boatBattleWon: bool
    :type newTowersDestroyed: int
    :type prevTowersDestroyed: int
    :type remainingTowers: int
    :type team: :class:`PlayerBattleData`
    :type battleTime: str
    :type challengeId: int
    :type tournamentTag: str
    :type challengeTitle: str
    :type isLadderTournament: bool
    :type isHostedMatch: bool
    """
    
    def __init__(self, gameMode: Optional[dict] = None, arena: Optional[dict] = None, type: Optional[str] = None,
                 deckSelection: Optional[str] = None, opponent: Optional[List[dict]] = None,
                 challengeWinCountBefore: Optional[int] = None, boatBattleSide: Optional[str] = None,
                 boatBattleWon: Optional[bool] = None, newTowersDestroyed: Optional[int] = None,
                 prevTowersDestroyed: Optional[int] = None, remainingTowers: Optional[int] = None,
                 team: Optional[List[dict]] = None, battleTime: Optional[str] = None, challengeId: Optional[int] = None,
                 tournamentTag: Optional[str] = None, challengeTitle: Optional[str] = None,
                 isLadderTournament: Optional[bool] = None, isHostedMatch: Optional[bool] = None, **kwargs):
        super().__init__(**kwargs)
        self.gameMode = None if gameMode is None else GameMode(**gameMode)
        self.arena = None if arena is None else Arena(**arena)
        self.type = type
        self.deckSelection = deckSelection
        self.opponent = None if opponent is None else list(map(lambda x: PlayerBattleData(**x), opponent))
        self.challengeWinCountBefore = challengeWinCountBefore
        self.boatBattleSide = boatBattleSide
        self.boatBattleWon = boatBattleWon
        self.newTowersDestroyed = newTowersDestroyed
        self.prevTowersDestroyed = prevTowersDestroyed
        self.remainingTowers = remainingTowers
        self.team = None if team is None else list(map(lambda x: PlayerBattleData(**x), team))
        self.battleTime = battleTime
        self.challengeId = challengeId
        self.tournamentTag = tournamentTag
        self.challengeTitle = challengeTitle
        self.isLadderTournament = isLadderTournament
        self.isHostedMatch = isHostedMatch


class Chest(SupercellApiResponse):
    def __init__(self, name: Optional[str] = None, index: Optional[int] = None,
                 iconUrls: Optional[Dict[str, Any]] = None, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.index = index
        self.iconUrls = iconUrls


class UpcomingChests(SupercellApiResponse):
    def __init__(self, items: Optional[List[dict]] = None, **kwargs):
        super().__init__(**kwargs)
        self.items = None if items is None else list(map(lambda x: Chest(**x), items))


class PlayerAchievementProgress(SupercellApiResponse):
    def __init__(self, stars: Optional[int] = None, value: Optional[int] = None, name: Optional[str] = None,
                 target: Optional[int] = None, info: Optional[str] = None, completionInfo: Optional[str] = None,
                 **kwargs):
        super().__init__(**kwargs)
        self.stars = stars
        self.value = value
        self.name = name
        self.target = target
        self.info = info
        self.completionInfo = completionInfo


class PlayerAchievementBadge(SupercellApiResponse):
    def __init__(self, maxLevel: Optional[int] = None, progress: Optional[int] = None, level: Optional[int] = None,
                 target: Optional[int] = None, name: Optional[str] = None, **kwargs):
        super().__init__(**kwargs)
        self.maxLevel = maxLevel
        self.progress = progress
        self.level = level
        self.target = target
        self.name = name


class PlayerItemLevel(SupercellApiResponse):
    def __init__(self, id: Optional[int] = None, count: Optional[int] = None, level: Optional[int] = None,
                 starLevel: Optional[int] = None, name: Optional[str] = None, maxLevel: Optional[int] = None,
                 iconUrls: Optional[Dict[str, Any]] = None, **kwargs):
        super().__init__(**kwargs)
        self.id = id
        self.count = count
        self.level = level
        self.starLevel = starLevel
        self.name = name
        self.maxLevel = maxLevel
        self.iconUrls = iconUrls


class LeagueSeasonResult(SupercellApiResponse):
    def __init__(self, trophies: Optional[int] = None, rank: Optional[int] = None, bestTrophies: Optional[int] = None,
                 id: Optional[str] = None, **kwargs):
        super().__init__(**kwargs)
        self.trophies = trophies
        self.rank = rank
        self.bestTrophies = bestTrophies
        self.id = id


class Item(SupercellApiResponse):
    def __init__(self, iconUrls: Optional[Dict[str, Any]] = None, name: Optional[str] = None, id: Optional[int] = None,
                 maxLevel: Optional[int] = None, **kwargs):
        super().__init__(**kwargs)
        self.iconUrls = iconUrls
        self.name = name
        self.id = id
        self.maxLevel = maxLevel


class PlayerLeagueStatistics(SupercellApiResponse):
    def __init__(self, bestSeason: Optional[dict] = None, currentSeason: Optional[dict] = None,
                 previousSeason: Optional[dict] = None, **kwargs):
        super().__init__(**kwargs)
        self.bestSeason = None if bestSeason is None else LeagueSeasonResult(**bestSeason)
        self.currentSeason = None if currentSeason is None else LeagueSeasonResult(**currentSeason)
        self.previousSeason = None if previousSeason is None else LeagueSeasonResult(**previousSeason)


class PlayerClan(SupercellApiResponse):
    def __init__(self, badgeId: Optional[int] = None, tag: Optional[str] = None, name: Optional[str] = None,
                 badgeUrls: Optional[Dict[str, Any]] = None, **kwargs):
        super().__init__(**kwargs)
        self.badgeId = badgeId
        self.tag = tag
        self.name = name
        self.badgeUrls = badgeUrls


class Player(SupercellApiResponse):
    def __init__(self, clan: Optional[dict] = None, arena: Optional[dict] = None, role: Optional[str] = None,
                 wins: Optional[int] = None, losses: Optional[int] = None, totalDonations: Optional[int] = None,
                 leagueStatistics: Optional[dict] = None, cards: Optional[List[dict]] = None,
                 currentFavouriteCard: Optional[dict] = None, badges: Optional[List[dict]] = None,
                 tag: Optional[str] = None, name: Optional[str] = None, expLevel: Optional[int] = None,
                 trophies: Optional[int] = None, bestTrophies: Optional[int] = None, donations: Optional[int] = None,
                 donationsReceived: Optional[int] = None, achievements: Optional[List[dict]] = None,
                 battleCount: Optional[int] = None, threeCrownWins: Optional[int] = None,
                 challengeCardsWon: Optional[int] = None, challengeMaxWins: Optional[int] = None,
                 tournamentCardsWon: Optional[int] = None, tournamentBattleCount: Optional[int] = None,
                 currentDeck: Optional[List[dict]] = None, warDayWins: Optional[int] = None,
                 clanCardsCollected: Optional[int] = None, starPoints: Optional[int] = None,
                 expPoints: Optional[int] = None, **kwargs):
        super().__init__(**kwargs)
        self.clan = None if clan is None else PlayerClan(**clan)
        self.arena = None if arena is None else Arena(**arena)
        self.role = role
        self.wins = wins
        self.losses = losses
        self.totalDonations = totalDonations
        self.leagueStatistics = None if leagueStatistics is None else PlayerLeagueStatistics(**leagueStatistics)
        self.cards = None if cards is None else list(map(lambda x: PlayerItemLevel(**x), cards))
        self.currentFavouriteCard = None if currentFavouriteCard is None else Item(**currentFavouriteCard)
        self.badges = None if badges is None else list(map(lambda x: PlayerAchievementBadge(**x), badges))
        self.tag = tag
        self.name = name
        self.expLevel = expLevel
        self.trophies = trophies
        self.bestTrophies = bestTrophies
        self.donations = donations
        self.donationsReceived = donationsReceived
        self.achievements = None if achievements is None else list(
            map(lambda x: PlayerAchievementProgress(**x), achievements)
        )
        self.battleCount = battleCount
        self.threeCrownWins = threeCrownWins
        self.challengeCardsWon = challengeCardsWon
        self.challengeMaxWins = challengeMaxWins
        self.tournamentCardsWon = tournamentCardsWon
        self.tournamentBattleCount = tournamentBattleCount
        self.currentDeck = None if currentDeck is None else list(map(lambda x: PlayerItemLevel(**x), currentDeck))
        self.warDayWins = warDayWins
        self.clanCardsCollected = clanCardsCollected
        self.starPoints = starPoints
        self.expPoints = expPoints
