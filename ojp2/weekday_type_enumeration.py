from enum import Enum

__NAMESPACE__ = "http://www.vdv.de/ojp"


class WeekdayTypeEnumeration(Enum):
    """
    [a specialisation of DAY OF WEEK in TMv6] enumeration of individual the seven
    DAYs OF WEEK, along with public holidays.
    """

    SUNDAY = "Sunday"
    MONDAY = "Monday"
    TUESDAY = "Tuesday"
    WEDNESDAY = "Wednesday"
    THURSDAY = "Thursday"
    FRIDAY = "Friday"
    SATURDAY = "Saturday"
    PUBLIC_HOLIDAY = "PublicHoliday"
