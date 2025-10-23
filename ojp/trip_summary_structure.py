from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime, XmlDuration
from ojp.international_text_structure import InternationalTextStructure
from ojp.operating_days_structure import OperatingDaysStructure
from ojp.place_ref_structure import PlaceRefStructure
from ojp.situation_full_ref_2 import SituationFullRef2

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class TripSummaryStructure:
    """
    Structure for trip overview information.

    :ivar trip_id: Id of this trip for referencing purposes. Unique
        within trip response.
    :ivar origin: Describes the origin situation of this trip.
    :ivar destination: Describes the arrival situation of this trip.
    :ivar duration: Overall duration of the trip.
    :ivar start_time: Departure time at origin.
    :ivar end_time: Arrival time at destination.
    :ivar pttrip_legs: Number of public transport trip legs.
    :ivar distance: Trip distance.
    :ivar operating_days: Bit string definition of operating days.
    :ivar operating_days_description: Textual description of the
        operation days, e.g. "monday to friday" or "not on holidays".
    :ivar situation_full_ref:
    :ivar extension:
    """
    trip_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TripId",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        }
    )
    origin: Optional[PlaceRefStructure] = field(
        default=None,
        metadata={
            "name": "Origin",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    destination: Optional[PlaceRefStructure] = field(
        default=None,
        metadata={
            "name": "Destination",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "Duration",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    start_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "StartTime",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    end_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "EndTime",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    pttrip_legs: Optional[int] = field(
        default=None,
        metadata={
            "name": "PTTripLegs",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    distance: Optional[int] = field(
        default=None,
        metadata={
            "name": "Distance",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    operating_days: Optional[OperatingDaysStructure] = field(
        default=None,
        metadata={
            "name": "OperatingDays",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    operating_days_description: Optional[InternationalTextStructure] = field(
        default=None,
        metadata={
            "name": "OperatingDaysDescription",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    situation_full_ref: List[SituationFullRef2] = field(
        default_factory=list,
        metadata={
            "name": "SituationFullRef",
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
