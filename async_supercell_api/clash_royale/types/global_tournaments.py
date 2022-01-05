from typing import List, Optional
from ...types import SupercellApiResponse
from .players import GameMode, Item


class LadderTournament(SupercellApiResponse):
    def __init__(self, gameMode: Optional[dict] = None, maxLosses: Optional[int] = None,
                 minExpLevel: Optional[int] = None, tournamentLevel: Optional[int] = None,
                 milestoneRewards: Optional[List[dict]] = None, freeTierRewards: Optional[List[dict]] = None,
                 tag: Optional[str] = None, title: Optional[str] = None, startTime: Optional[str] = None,
                 endTime: Optional[str] = None, topRankReward: Optional[List[dict]] = None,
                 maxTopRewardRank: Optional[int] = None, **kwargs):
        super().__init__(**kwargs)
        self.gameMode = None if gameMode is None else GameMode(**gameMode)
        self.maxLosses = maxLosses
        self.minExpLevel = minExpLevel
        self.tournamentLevel = tournamentLevel
        self.milestoneRewards = None if milestoneRewards is None else list(
            map(lambda x: SurvivalMilestoneReward(**x), milestoneRewards)
        )
        self.freeTierRewards = None if freeTierRewards is None else list(
            map(lambda x: SurvivalMilestoneReward(**x), freeTierRewards)
        )
        self.tag = tag
        self.title = title
        self.startTime = startTime
        self.endTime = endTime
        self.topRankReward = None if topRankReward is None else list(
            map(lambda x: SurvivalMilestoneReward(**x), topRankReward)
        )
        self.maxTopRewardRank = maxTopRewardRank


class SurvivalMilestoneReward(SupercellApiResponse):
    def __init__(self, chest: Optional[str] = None, rarity: Optional[str] = None, resource: Optional[str] = None,
                 type: Optional[str] = None, amount: Optional[int] = None, card: Optional[dict] = None,
                 wins: Optional[int] = None, **kwargs):
        super().__init__(**kwargs)
        self.chest = chest
        self.rarity = rarity
        self.resource = resource
        self.type = type
        self.amount = amount
        self.card = None if card is None else Item(**card)
        self.wins = wins
