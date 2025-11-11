from dataclasses import dataclass, field
from typing import Optional

from ojp2.booking_arrangements_structure import BookingArrangementsStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class BookingArrangementsContainerStructure:
    """
    Container for multiple booking arrangements.

    :ivar booking_arrangement: [a more generalised form of BOOKING
        ARRANGEMENTS in TMv6] arrangement for booking any leg or legs of
        a journey.
    :ivar extension:
    """

    booking_arrangement: list[BookingArrangementsStructure] = field(
        default_factory=list,
        metadata={
            "name": "BookingArrangement",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "min_occurs": 1,
        },
    )
    extension: Optional[object] = field(
        default=None,
        metadata={
            "name": "Extension",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
