from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


class DrivingConditionTypeEnum(Enum):
    IMPOSSIBLE = "impossible"
    HAZARDOUS = "hazardous"
    NORMAL = "normal"
    PASSABLE_WITH_CARE = "passableWithCare"
    UNKNOWN = "unknown"
    VERY_HAZARDOUS = "veryHazardous"
    WINTER_CONDITIONS = "winterConditions"
    OTHER = "other"
