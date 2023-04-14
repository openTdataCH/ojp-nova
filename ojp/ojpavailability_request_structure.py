from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime
from ojp.abstract_ojpservice_request_structure import AbstractOjpserviceRequestStructure
from ojp.booking_ptleg_structure import BookingPtlegStructure
from ojp.booking_user_structure import BookingUserStructure
from ojp.extensions_2 import Extensions2

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class OjpavailabilityRequestStructure(AbstractOjpserviceRequestStructure):
    """
    :ivar public_transport: Definition of the journey leg to be covered
        by public transport. Other mobility services can be added later.
    :ivar mobility_user: Passenger(s) for whom the service needs to be
        booked, one MobilityUser per passenger.
    :ivar earliest_departure_time: Earliest possible departure time from
        start location.
    :ivar latest_arrival_time: Latest possible arrival time at
        destination location.
    :ivar extensions:
    """
    class Meta:
        name = "OJPAvailabilityRequestStructure"

    public_transport: Optional[BookingPtlegStructure] = field(
        default=None,
        metadata={
            "name": "PublicTransport",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    mobility_user: List[BookingUserStructure] = field(
        default_factory=list,
        metadata={
            "name": "MobilityUser",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "min_occurs": 1,
        }
    )
    earliest_departure_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "EarliestDepartureTime",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    latest_arrival_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "LatestArrivalTime",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    extensions: Optional[Extensions2] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
