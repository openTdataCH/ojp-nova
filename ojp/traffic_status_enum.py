from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


class TrafficStatusEnum(Enum):
    IMPOSSIBLE = "impossible"
    CONGESTED = "congested"
    HEAVY = "heavy"
    FREE_FLOW = "freeFlow"
    UNKNOWN = "unknown"
