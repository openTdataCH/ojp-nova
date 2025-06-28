from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class BookingStatusEnumeration(Enum):
    """Values for Values for TPEG Pti024 - BookingStatus

    :cvar UNKNOWN: TPEG Pti24_0, unknown
    :cvar AVAILABLE: TPEG Pti24_1, available
    :cvar LIMITED: TPEG Pti24_2, limited
    :cvar VERY_LIMITED: TPEG Pti24_3, very limited
    :cvar FULL: TPEG Pti24_4, full
    :cvar WAITING_LIST: TPEG Pti24_5, waiting list
    :cvar NO_BOOKING_REQUIRED: TPEG Pti24_6, no booking required
    :cvar BOOKING_REQUIRED: TPEG Pti24_7, booking is required
    :cvar BOOKING_OPTIONAL: TPEG Pti24_8, booking is optional
    :cvar UNDEFINED_BOOKING_INFORMATION: TPEG Pti24_255, undefined
        booking information
    """

    UNKNOWN = "unknown"
    AVAILABLE = "available"
    LIMITED = "limited"
    VERY_LIMITED = "veryLimited"
    FULL = "full"
    WAITING_LIST = "waitingList"
    NO_BOOKING_REQUIRED = "noBookingRequired"
    BOOKING_REQUIRED = "bookingRequired"
    BOOKING_OPTIONAL = "bookingOptional"
    UNDEFINED_BOOKING_INFORMATION = "undefinedBookingInformation"
