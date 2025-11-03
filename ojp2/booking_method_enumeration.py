from enum import Enum

__NAMESPACE__ = "http://www.vdv.de/ojp"


class BookingMethodEnumeration(Enum):
    """
    Allowed values for a booking method.
    """

    CALL_DRIVER = "callDriver"
    CALL_OFFICE = "callOffice"
    ONLINE = "online"
    OTHER = "other"
    PHONE_AT_STOP = "phoneAtStop"
    TEXT = "text"
    MOBILE_APP = "mobileApp"
    AT_OFFICE = "atOffice"
    NONE = "none"
