from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class BookingStatusEnumeration(Enum):
    """
    Values for TBookingStatus TPEG pti_table 24.
    """
    PTI24_0 = "pti24_0"
    UNKNOWN = "unknown"
    PTI17_1 = "pti17_1"
    AVAILABLE = "available"
    PTI24_2 = "pti24_2"
    LIMITED = "limited"
    PTI24_3 = "pti24_3"
    VERY_LIMITED = "veryLimited"
    PTI24_4 = "pti24_4"
    FULL = "full"
    PTI24_5 = "pti24_5"
    WAITING_LIST = "waitingList"
    PTI24_6 = "pti24_6"
    NO_BOOKING_REQUIRED = "noBookingRequired"
    PTI24_7 = "pti24_7"
    BOOKING_REQUIRED = "bookingRequired"
    PTI24_8 = "pti24_8"
    BOOKING_OPTIONAL = "bookingOptional"
    PTI24_255 = "pti24_255"
    UNDEFINED_BOOKING_INFORMATION = "undefinedBookingInformation"
