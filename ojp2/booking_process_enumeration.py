from enum import Enum

__NAMESPACE__ = "http://www.vdv.de/ojp"


class BookingProcessEnumeration(Enum):
    """
    Allowed values for Booking Process UIC 7037 Code list.

    :cvar PRODUCT_NOT_AVAILABLE: Product is not available.
    :cvar PRODUCT_NOT_BOOKABLE: Product cannot be booked.
    :cvar BOOKABLE_THROUGH_INTERNATIONAL_SYSTEM: Product can be booked
        online internationally.
    :cvar BOOKABLE_THROUGH_NATIONAL_SYSTEM: Product can be booked online
        nationally.
    :cvar BOOKABLE_MANUALLY: Product can only be booked by contacting
        specific authorised retail outlets.
    :cvar OTHER: Other booking process.
    """

    PRODUCT_NOT_AVAILABLE = "productNotAvailable"
    PRODUCT_NOT_BOOKABLE = "productNotBookable"
    BOOKABLE_THROUGH_INTERNATIONAL_SYSTEM = (
        "bookableThroughInternationalSystem"
    )
    BOOKABLE_THROUGH_NATIONAL_SYSTEM = "bookableThroughNationalSystem"
    BOOKABLE_MANUALLY = "bookableManually"
    OTHER = "other"
