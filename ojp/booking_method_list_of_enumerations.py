from dataclasses import dataclass, field
from typing import List
from ojp.booking_method_enumeration import BookingMethodEnumeration

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class BookingMethodListOfEnumerations:
    """
    List of values for Flexible Booking values.

    :ivar booking_method: Flexible booking methods.
    """
    booking_method: List[BookingMethodEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "BookingMethod",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "min_occurs": 1,
        }
    )
