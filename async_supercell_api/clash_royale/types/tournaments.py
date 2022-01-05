from typing import List, Optional
from ...types import SupercellApiResponse
from .players import GameMode, PlayerClan


class TournamentHeader(SupercellApiResponse):
    def __init__(self, status: Optional[str] = None, preparationDuration: Optional[int] = None,
                 createdTime: Optional[str] = None, firstPlaceCardPrize: Optional[int] = None,
                 gameMode: Optional[dict] = None, duration: Optional[int] = None, type: Optional[str] = None,
                 tag: Optional[str] = None, creatorTag: Optional[str] = None, name: Optional[str] = None,
                 description: Optional[str] = None, capacity: Optional[int] = None, maxCapacity: Optional[int] = None,
                 levelCap: Optional[int] = None, **kwargs):
        super().__init__(**kwargs)
        self.status = status
        self.preparationDuration = preparationDuration
        self.createdTime = createdTime
        self.firstPlaceCardPrize = firstPlaceCardPrize
        self.gameMode = None if gameMode is None else GameMode(**gameMode)
        self.duration = duration
        self.type = type
        self.tag = tag
        self.creatorTag = creatorTag
        self.name = name
        self.description = description
        self.capacity = capacity
        self.maxCapacity = maxCapacity
        self.levelCap = levelCap


class Tournament(SupercellApiResponse):
    def __init__(self, membersList: Optional[List[dict]] = None, status: Optional[str] = None,
                 preparationDuration: Optional[int] = None, createdTime: Optional[str] = None,
                 startedTime: Optional[str] = None, endedTime: Optional[str] = None,
                 firstPlaceCardPrize: Optional[int] = None, gameMode: Optional[dict] = None,
                 duration: Optional[int] = None, type: Optional[str] = None, tag: Optional[str] = None,
                 creatorTag: Optional[str] = None, name: Optional[str] = None, description: Optional[str] = None,
                 capacity: Optional[int] = None, maxCapacity: Optional[int] = None, levelCap: Optional[int] = None,
                 **kwargs):
        super().__init__(**kwargs)
        self.membersList = None if membersList is None else list(map(lambda x: TournamentMember(**x), membersList))
        self.status = status
        self.preparationDuration = preparationDuration
        self.createdTime = createdTime
        self.startedTime = startedTime
        self.endedTime = endedTime
        self.firstPlaceCardPrize = firstPlaceCardPrize
        self.gameMode = None if gameMode is None else GameMode(**gameMode)
        self.duration = duration
        self.type = type
        self.tag = tag
        self.creatorTag = creatorTag
        self.name = name
        self.description = description
        self.capacity = capacity
        self.maxCapacity = maxCapacity
        self.levelCap = levelCap


class TournamentMember(SupercellApiResponse):
    def __init__(self, rank: Optional[int] = None, previousRank: Optional[int] = None, clan: Optional[dict] = None,
                 tag: Optional[str] = None, name: Optional[str] = None, score: Optional[int] = None, **kwargs):
        super().__init__(**kwargs)
        self.rank = rank
        self.previousRank = previousRank
        self.clan = None if clan is None else PlayerClan(**clan)
        self.tag = tag
        self.name = name
        self.score = score
