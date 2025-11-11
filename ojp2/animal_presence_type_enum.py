from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


class AnimalPresenceTypeEnum(Enum):
    ANIMALS_ON_THE_ROAD = "animalsOnTheRoad"
    HERD_OF_ANIMALS_ON_THE_ROAD = "herdOfAnimalsOnTheRoad"
    LARGE_ANIMALS_ON_THE_ROAD = "largeAnimalsOnTheRoad"
