from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class DaysOfWeekEnumerationx(Enum):
    """
    Values for Day Type TPEG pti_table 34.
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
