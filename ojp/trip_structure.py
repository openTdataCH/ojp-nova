from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime, XmlDuration
from ojp.international_text_structure import InternationalTextStructure
from ojp.operating_days_structure import OperatingDaysStructure
from ojp.situation_full_ref_2 import SituationFullRef2
from ojp.trip_leg_structure import TripLegStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class TripStructure:
    """
    [an extended form of PT TRIP in TM and NeTEx as it also includes the
    initial and final access legs to and from public transport] whole journey
    from passenger origin to passenger destination in one or more trip LEGs.

    :ivar trip_id: Id of this trip for referencing purposes. Unique
        within trip response.
    :ivar duration: Overall duration of the trip.
    :ivar start_time: Departure time at origin.
    :ivar end_time: Arrival time at destination.
    :ivar transfers: Number of interchanges.
    :ivar distance: Trip distance.
    :ivar trip_leg: Legs of the trip
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
    duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "Duration",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        }
    )
    start_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "StartTime",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        }
    )
    end_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "EndTime",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        }
    )
    transfers: Optional[int] = field(
        default=None,
        metadata={
            "name": "Transfers",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
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
    trip_leg: List[TripLegStructure] = field(
        default_factory=list,
        metadata={
            "name": "TripLeg",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "min_occurs": 1,
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
