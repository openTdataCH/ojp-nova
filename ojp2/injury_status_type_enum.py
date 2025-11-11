from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


class InjuryStatusTypeEnum(Enum):
    DEAD = "dead"
    INJURED = "injured"
    SERIOUSLY_INJURED = "seriouslyInjured"
    SLIGHTLY_INJURED = "slightlyInjured"
    UNINJURED = "uninjured"
    UNKNOWN = "unknown"
