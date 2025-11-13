from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class EndTimePrecisionEnumeration(Enum):
    """
    Allowed values for EndTime Precision.
    """

    DAY = "day"
    HOUR = "hour"
    SECOND = "second"
    MILLI_SECOND = "milliSecond"
