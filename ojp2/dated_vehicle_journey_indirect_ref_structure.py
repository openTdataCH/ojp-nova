from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from ojp2.stop_point_ref_structure import StopPointRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class DatedVehicleJourneyIndirectRefStructure:
    """
    Type for Origin and Destination stop of a VEHICLE JOURNEY.

    :ivar origin_ref: The origin is used to help identify the VEHICLE
        JOURNEY.
    :ivar aimed_departure_time: Departure time from origin SCHEDULED
        STOP POINT.
    :ivar destination_ref: The destination is used to help identify the
        VEHICLE JOURNEY.
    :ivar aimed_arrival_time: Arrival time at destination SCHEDULED STOP
        POINT.
    """

    origin_ref: Optional[StopPointRefStructure] = field(
        default=None,
        metadata={
            "name": "OriginRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    aimed_departure_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "AimedDepartureTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    destination_ref: Optional[StopPointRefStructure] = field(
        default=None,
        metadata={
            "name": "DestinationRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    aimed_arrival_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "AimedArrivalTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
