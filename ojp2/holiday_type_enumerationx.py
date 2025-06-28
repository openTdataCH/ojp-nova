from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class HolidayTypeEnumerationx(Enum):
    """Subset of TPEG Pti34 - DayType

    :cvar HOLIDAY: TPEG Pti34_10, holiday
    :cvar PUBLIC_HOLIDAY: TPEG Pti34_11, public holiday
    :cvar RELIGIOUS_HOLIDAY: TPEG Pti34_12, religious holiday
    :cvar FEDERAL_HOLIDAY: TPEG Pti34_13, federal holiday
    :cvar REGIONAL_HOLIDAY: TPEG Pti34_14, regional holiday
    :cvar NATIONAL_HOLIDAY: TPEG Pti34_15, national holiday
    :cvar SUNDAYS_AND_PUBLIC_HOLIDAYS: TPEG Pti34_18, Sundays and public
        holidays
    :cvar SCHOOL_DAYS: TPEG Pti34_19, school days
    :cvar EVERY_DAY: TPEG Pti34_20, every day
    :cvar UNDEFINED_DAY_TYPE: TPEG Pti34_255, undefined day type
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
