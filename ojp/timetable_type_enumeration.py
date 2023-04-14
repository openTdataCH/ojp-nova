from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class TimetableTypeEnumeration(Enum):
    """
    Values for timetable type TPEG pti_table 33.
    """
    PTI33_0 = "pti33_0"
    UNKNOWN = "unknown"
    PTI33_1 = "pti33_1"
    WINTER = "winter"
    PTI33_2 = "pti33_2"
    SPRING = "spring"
    PTI33_3 = "pti33_3"
    SUMMER = "summer"
    PTI33_4 = "pti33_4"
    AUTUMN = "autumn"
    PTI33_5 = "pti33_5"
    SPECIAL = "special"
    PTI33_6 = "pti33_6"
    EMERGENCY = "emergency"
    PTI33_255 = "pti33_255"
    UNDEFINED_TIMETABLE_TYPE = "undefinedTimetableType"
