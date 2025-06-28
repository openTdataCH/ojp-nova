from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class DayTypeEnumeration(Enum):
    """Values for TPEG Pti34 - DayType

    :cvar UNKNOWN: TPEG Pti34_0, unknown
    :cvar MONDAY: TPEG Pti34_1, Monday
    :cvar TUESDAY: TPEG Pti34_2, Tuesday
    :cvar WEDNESDAY: TPEG Pti34_3, Wednesday
    :cvar THURSDAY: TPEG Pti34_4, Thursday
    :cvar FRIDAY: TPEG Pti34_5, Friday
    :cvar SATURDAY: TPEG Pti34_6, Saturday
    :cvar SUNDAY: TPEG Pti34_7, Sunday
    :cvar WEEKDAYS: TPEG Pti34_8, weekdays
    :cvar WEEKENDS: TPEG Pti34_9, weekends
    :cvar HOLIDAY: TPEG Pti34_10, holiday
    :cvar PUBLIC_HOLIDAY: TPEG Pti34_11, public holiday
    :cvar RELIGIOUS_HOLIDAY: TPEG Pti34_12, religious holiday
    :cvar FEDERAL_HOLIDAY: TPEG Pti34_13, federal holiday
    :cvar REGIONAL_HOLIDAY: TPEG Pti34_14, regional holiday
    :cvar NATIONAL_HOLIDAY: TPEG Pti34_15, national holiday
    :cvar MONDAY_TO_FRIDAY: TPEG Pti34_16, Monday to Friday
    :cvar MONDAY_TO_SATURDAY: TPEG Pti34_17, Monday to Saturday
    :cvar SUNDAYS_AND_PUBLIC_HOLIDAYS: TPEG Pti34_18, Sundays and public
        holidays
    :cvar SCHOOL_DAYS: TPEG Pti34_19, school days
    :cvar EVERY_DAY: TPEG Pti34_20, every day
    :cvar UNDEFINED_DAY_TYPE: TPEG Pti34_255, undefined day type
    """

    UNKNOWN = "unknown"
    MONDAY = "monday"
    TUESDAY = "tuesday"
    WEDNESDAY = "wednesday"
    THURSDAY = "thursday"
    FRIDAY = "friday"
    SATURDAY = "saturday"
    SUNDAY = "sunday"
    WEEKDAYS = "weekdays"
    WEEKENDS = "weekends"
    HOLIDAY = "holiday"
    PUBLIC_HOLIDAY = "publicHoliday"
    RELIGIOUS_HOLIDAY = "religiousHoliday"
    FEDERAL_HOLIDAY = "federalHoliday"
    REGIONAL_HOLIDAY = "regionalHoliday"
    NATIONAL_HOLIDAY = "nationalHoliday"
    MONDAY_TO_FRIDAY = "mondayToFriday"
    MONDAY_TO_SATURDAY = "mondayToSaturday"
    SUNDAYS_AND_PUBLIC_HOLIDAYS = "sundaysAndPublicHolidays"
    SCHOOL_DAYS = "schoolDays"
    EVERY_DAY = "everyDay"
    UNDEFINED_DAY_TYPE = "undefinedDayType"
