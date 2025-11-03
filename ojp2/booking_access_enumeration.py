from enum import Enum

__NAMESPACE__ = "http://www.vdv.de/ojp"


class BookingAccessEnumeration(Enum):
    """
    Allowed values for Booking Access.
    """

    PUBLIC = "public"
    AUTHORISED_PUBLIC = "authorisedPublic"
    STAFF = "staff"
    OTHER = "other"
