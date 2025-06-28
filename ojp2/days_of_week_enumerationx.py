from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class DaysOfWeekEnumerationx(Enum):
    """Subset of TPEG Pti34 - DayType

    :cvar UNKNOWN: TPEG Pti34_0, unknown
    :cvar MONDAY: TPEG Pti34_1, Monday
    :cvar TUESDAY: TPEG Pti34_2, Tuesday
    :cvar WEDNESDAY: TPEG Pti34_3, Wednesday
    :cvar THURSDAY: TPEG Pti34_4, Thursday
    :cvar FRIDAY: TPEG Pti34_5, Friday
    :cvar SATURDAY: TPEG Pti34_6, Saturday
    :cvar SUNDAY: TPEG Pti34_7, Sunday
    :cvar MONDAY_TO_FRIDAY: TPEG Pti34_16, Monday to Friday
    :cvar MONDAY_TO_SATURDAY: TPEG Pti34_17, Monday to Saturday
    :cvar WEEKDAYS: TPEG Pti34_8, weekdays
    :cvar WEEKENDS: TPEG Pti34_9, weekends
    """

    UNKNOWN = "unknown"
    MONDAY = "monday"
    TUESDAY = "tuesday"
    WEDNESDAY = "wednesday"
    THURSDAY = "thursday"
    FRIDAY = "friday"
    SATURDAY = "saturday"
    SUNDAY = "sunday"
    MONDAY_TO_FRIDAY = "mondayToFriday"
    MONDAY_TO_SATURDAY = "mondayToSaturday"
    WEEKDAYS = "weekdays"
    WEEKENDS = "weekends"
