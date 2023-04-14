from dataclasses import dataclass, field
from typing import List, Optional
from ojp.bookable_service_item_structure import BookableServiceItemStructure
from ojp.booking_ptleg_structure import BookingPtlegStructure
from ojp.fare_product_structure import FareProductStructure
from ojp.ojperror_structure import OjperrorStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class AvailabilityResultStructure:
    """
    Availability result structure.

    :ivar error_condition: Problems related to this AVAILABILITY result.
    :ivar public_transport: Definition of the journey leg that should be
        made by public transport. Other mobility services may be added
        later.
    :ivar bookable_ticket: Sequence of bookable tickets or surcharges
        for this part of the trip. If ticket price is zero: an already
        purchased/virtual ticket of this type presented to the driver
        would be accepted.
    :ivar bookable_service_item: Sequence of bookable service items for
        this part of the trip.
    :ivar extension:
    """
    error_condition: List[OjperrorStructure] = field(
        default_factory=list,
        metadata={
            "name": "ErrorCondition",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    public_transport: Optional[BookingPtlegStructure] = field(
        default=None,
        metadata={
            "name": "PublicTransport",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    bookable_ticket: List[FareProductStructure] = field(
        default_factory=list,
        metadata={
            "name": "BookableTicket",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    bookable_service_item: List[BookableServiceItemStructure] = field(
        default_factory=list,
        metadata={
            "name": "BookableServiceItem",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    extension: Optional[object] = field(
        default=None,
        metadata={
            "name": "Extension",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
