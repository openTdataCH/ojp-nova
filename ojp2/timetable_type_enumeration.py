from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class TimetableTypeEnumeration(Enum):
    """Values for TPEG Pti033 - TimetableType

    :cvar UNKNOWN: TPEG Pti33_0, unknown
    :cvar WINTER: TPEG Pti33_1, winter
    :cvar SPRING: TPEG Pti33_2, spring
    :cvar SUMMER: TPEG Pti33_3, summer
    :cvar AUTUMN: TPEG Pti33_4, autumn
    :cvar SPECIAL: TPEG Pti33_5, special
    :cvar EMERGENCY: TPEG Pti33_6, emergency
    :cvar UNDEFINED_TIMETABLE_TYPE: TPEG Pti33_255, undefined timetable
        type
    """

    UNKNOWN = "unknown"
    WINTER = "winter"
    SPRING = "spring"
    SUMMER = "summer"
    AUTUMN = "autumn"
    SPECIAL = "special"
    EMERGENCY = "emergency"
    UNDEFINED_TIMETABLE_TYPE = "undefinedTimetableType"
