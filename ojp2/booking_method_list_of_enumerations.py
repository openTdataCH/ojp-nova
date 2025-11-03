from dataclasses import dataclass, field

from ojp2.booking_method_enumeration import BookingMethodEnumeration

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class BookingMethodListOfEnumerations:
    """
    List of values for booking values.

    :ivar booking_method: Booking methods.
    """

    booking_method: list[BookingMethodEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "BookingMethod",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "min_occurs": 1,
        },
    )
