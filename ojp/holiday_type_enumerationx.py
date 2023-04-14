from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class HolidayTypeEnumerationx(Enum):
    """
    Values for Day Type TPEG pti_table 34.
    """
    HOLIDAY = "holiday"
    PUBLIC_HOLIDAY = "publicHoliday"
    RELIGIOUS_HOLIDAY = "religiousHoliday"
    FEDERAL_HOLIDAY = "federalHoliday"
    REGIONAL_HOLIDAY = "regionalHoliday"
    NATIONAL_HOLIDAY = "nationalHoliday"
    SUNDAYS_AND_PUBLIC_HOLIDAYS = "sundaysAndPublicHolidays"
    SCHOOL_DAYS = "schoolDays"
    EVERY_DAY = "everyDay"
    UNDEFINED_DAY_TYPE = "undefinedDayType"
