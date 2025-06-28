from enum import Enum

__NAMESPACE__ = "http://www.vdv.de/ojp"


class GroupBookingEnumeration(Enum):
    """
    Allowed values for Group Booking.
    """

    GROUPS_ALLOWED = "groupsAllowed"
    GROUPS_NOT_ALLOWED = "groupsNotAllowed"
    GROUPS_ALLOWED_WITH_RESERVATION = "groupsAllowedWithReservation"
    GROUP_BOOKINGS_RESTRICTED = "groupBookingsRestricted"
    UNKNOWN = "unknown"
