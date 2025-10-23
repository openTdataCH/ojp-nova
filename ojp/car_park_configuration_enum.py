from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


class CarParkConfigurationEnum(Enum):
    MULTI_STOREY = "multiStorey"
    PARK_AND_RIDE = "parkAndRide"
    SINGLE_LEVEL = "singleLevel"
    UNDERGROUND = "underground"
