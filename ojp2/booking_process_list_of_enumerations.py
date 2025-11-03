from dataclasses import dataclass, field

from ojp2.booking_process_enumeration import BookingProcessEnumeration

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class BookingProcessListOfEnumerations:
    """
    List of Booking Process values.

    :ivar booking_process: Ways how to book (UIC 7037 codes).
    """

    booking_process: list[BookingProcessEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "BookingProcess",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "min_occurs": 1,
        },
    )
