from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class SeverityEnumeration(Enum):
    """Values for Severity.

    Correspond to TPEG Pti26 Severity values.

    :cvar PTI26_0:
    :cvar UNKNOWN: TPEG Pti26_0: unknown.
    :cvar PTI26_1:
    :cvar VERY_SLIGHT: TPEG Pti26_1: very slight.
    :cvar PTI26_2:
    :cvar SLIGHT: TPEG Pti26_2: slight.
    :cvar PTI26_3:
    :cvar NORMAL: TPEG Pti26_3: normal.
    :cvar PTI26_4:
    :cvar SEVERE: TPEG Pti26_4: severe.
    :cvar PTI26_5:
    :cvar VERY_SEVERE: TPEG Pti26_5: verySevere.
    :cvar PTI26_6:
    :cvar NO_IMPACT: TPEG Pti26_6: noImpact.
    :cvar PTI26_255:
    :cvar UNDEFINED: TPEG Pti26_255: undefined.
    """
    PTI26_0 = "pti26_0"
    UNKNOWN = "unknown"
    PTI26_1 = "pti26_1"
    VERY_SLIGHT = "verySlight"
    PTI26_2 = "pti26_2"
    SLIGHT = "slight"
    PTI26_3 = "pti26_3"
    NORMAL = "normal"
    PTI26_4 = "pti26_4"
    SEVERE = "severe"
    PTI26_5 = "pti26_5"
    VERY_SEVERE = "verySevere"
    PTI26_6 = "pti26_6"
    NO_IMPACT = "noImpact"
    PTI26_255 = "pti26_255"
    UNDEFINED = "undefined"
