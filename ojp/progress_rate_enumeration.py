from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class ProgressRateEnumeration(Enum):
    """
    Classification of the rate of progress of VEHICLE according a fixed list of
    values.

    :cvar NO_PROGRESS: Vehicle is stationary.
    :cvar SLOW_PROGRESS: Vehicle is proceeding slower than normal.
    :cvar NORMAL_PROGRESS: Vehicle is proceeding at a normal rate.
    :cvar FAST_PROGRESS: Vehicle is proceeding faster than normal.
    :cvar UNKNOWN: There is no data.
    """
    NO_PROGRESS = "noProgress"
    SLOW_PROGRESS = "slowProgress"
    NORMAL_PROGRESS = "normalProgress"
    FAST_PROGRESS = "fastProgress"
    UNKNOWN = "unknown"
