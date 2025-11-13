from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class SeverityEnumeration(Enum):
    """Values for TPEG Pti26 - Severity

    :cvar UNKNOWN: TPEG Pti26_0, unknown
    :cvar VERY_SLIGHT: TPEG Pti26_1, very slight
    :cvar SLIGHT: TPEG Pti26_2, slight
    :cvar NORMAL: TPEG Pti26_3, normal
    :cvar SEVERE: TPEG Pti26_4, severe
    :cvar VERY_SEVERE: TPEG Pti26_5, very severe
    :cvar NO_IMPACT: TPEG Pti26_6, no impact
    :cvar UNDEFINED: TPEG Pti26_255, undefined
    """

    UNKNOWN = "unknown"
    VERY_SLIGHT = "verySlight"
    SLIGHT = "slight"
    NORMAL = "normal"
    SEVERE = "severe"
    VERY_SEVERE = "verySevere"
    NO_IMPACT = "noImpact"
    UNDEFINED = "undefined"
