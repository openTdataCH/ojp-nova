from dataclasses import dataclass, field
from typing import List
from ojp.group_booking_enumeration import GroupBookingEnumeration

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class GroupBookingListOfEnumerations:
    """
    Possibilites and restrictions for group booking.

    :ivar group_booking: Group booking policies.
    """
    group_booking: List[GroupBookingEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "GroupBooking",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "min_occurs": 1,
        }
    )
