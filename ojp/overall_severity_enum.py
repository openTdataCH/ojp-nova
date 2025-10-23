from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


class OverallSeverityEnum(Enum):
    HIGHEST = "highest"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    LOWEST = "lowest"
    NONE = "none"
    UNKNOWN = "unknown"
