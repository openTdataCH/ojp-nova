from dataclasses import dataclass, field
from typing import Optional

from ojp2.bookable_service_item_type_enumeration import (
    BookableServiceItemTypeEnumeration,
)

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class BookableServiceItemStructure:
    """Possible service items that can be booked in the actual booking system
    (defined by the traffic company of charge).

    Only those elements with value greater 0 are bookable. The indicated
    capacity corresponds to the maximum number that can be booked in one
    booking. This number does not have to be available for the specific
    booking and may result in booking failure. Caution: list can vary
    widely from one traffic company to another.

    :ivar type_value: The type of bookable service.
    :ivar max_bookable_capacity: Maximum number of service items that
        can be booked in one booking transaction. Default is 0.
    """

    type_value: Optional[BookableServiceItemTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        },
    )
    max_bookable_capacity: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaxBookableCapacity",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        },
    )
