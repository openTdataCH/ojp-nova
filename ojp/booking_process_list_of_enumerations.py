from dataclasses import dataclass, field
from typing import List
from ojp.booking_process_enumeration import BookingProcessEnumeration

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class BookingProcessListOfEnumerations:
    """
    List of Booking Process values.

    :ivar booking_process: Ways how to book (UIC 7037 codes).
    """
    booking_process: List[BookingProcessEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "BookingProcess",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "min_occurs": 1,
        }
    )
