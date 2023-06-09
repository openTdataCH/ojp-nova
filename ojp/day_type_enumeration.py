from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class DayTypeEnumeration(Enum):
    """
    Values for Day Type TPEG pti_table 34.
    """
    PTI34_0 = "pti34_0"
    UNKNOWN = "unknown"
    PTI34_1 = "pti34_1"
    MONDAY = "monday"
    PTI34_2 = "pti34_2"
    TUESDAY = "tuesday"
    PTI34_3 = "pti34_3"
    WEDNESDAY = "wednesday"
    PTI34_4 = "pti34_4"
    THURSDAY = "thursday"
    PTI34_5 = "pti34_5"
    FRIDAY = "friday"
    PTI34_6 = "pti34_6"
    SATURDAY = "saturday"
    PTI34_7 = "pti34_7"
    SUNDAY = "sunday"
    PTI34_8 = "pti34_8"
    WEEKDAYS = "weekdays"
    PTI34_9 = "pti34_9"
    WEEKENDS = "weekends"
    PTI34_10 = "pti34_10"
    HOLIDAY = "holiday"
    PTI34_11 = "pti34_11"
    PUBLIC_HOLIDAY = "publicHoliday"
    PTI34_12 = "pti34_12"
    RELIGIOUS_HOLIDAY = "religiousHoliday"
    PTI34_13 = "pti34_13"
    FEDERAL_HOLIDAY = "federalHoliday"
    PTI34_14 = "pti34_14"
    REGIONAL_HOLIDAY = "regionalHoliday"
    PTI34_15 = "pti34_15"
    NATIONAL_HOLIDAY = "nationalHoliday"
    PTI34_16 = "pti34_16"
    MONDAY_TO_FRIDAY = "mondayToFriday"
    PTI34_17 = "pti34_17"
    MONDAY_TO_SATURDAY = "mondayToSaturday"
    PTI34_18 = "pti34_18"
    SUNDAYS_AND_PUBLIC_HOLIDAYS = "sundaysAndPublicHolidays"
    PTI34_19 = "pti34_19"
    SCHOOL_DAYS = "schoolDays"
    PTI34_20 = "pti34_20"
    EVERY_DAY = "everyDay"
    PTI34_255 = "pti34_255"
    UNDEFINED_DAY_TYPE = "undefinedDayType"
