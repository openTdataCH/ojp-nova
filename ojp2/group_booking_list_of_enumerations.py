from dataclasses import dataclass, field

from ojp2.group_booking_enumeration import GroupBookingEnumeration

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class GroupBookingListOfEnumerations:
    """
    Possibilities and restrictions for group booking.

    :ivar group_booking: Group booking policies.
    """

    group_booking: list[GroupBookingEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "GroupBooking",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "min_occurs": 1,
        },
    )
