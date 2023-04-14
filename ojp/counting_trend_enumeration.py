from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class CountingTrendEnumeration(Enum):
    """
    Allowed values for trend of a counting.
    """
    DECREASING = "decreasing"
    INCREASING = "increasing"
    STABLE = "stable"
    UNSTABLE = "unstable"
    INCREASING_QUICKLY = "increasingQuickly"
    INCREASING_SLOWLY = "increasingSlowly"
    DECREASING_QUICKLY = "decreasingQuickly"
    DECREASING_SLOWLY = "decreasingSlowly"
    UNKNOWN = "unknown"
