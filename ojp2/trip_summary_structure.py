from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime, XmlDuration

from ojp2.feasibility_enumeration import FeasibilityEnumeration
from ojp2.international_text_structure import InternationalTextStructure
from ojp2.operating_days_structure import OperatingDaysStructure
from ojp2.place_ref_structure import PlaceRefStructure
from ojp2.situation_ref_list import SituationRefList

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class TripSummaryStructure:
    """
    Structure for trip overview information (only implementation related and
    therefore not modelled in Transmodel).

    :ivar trip_id: Id of this trip for referencing purposes. Unique
        within trip response.
    :ivar origin: Describes the origin situation of this trip.
    :ivar destination: Describes the arrival situation of this trip.
    :ivar duration: Overall duration of the trip (TRIP attribute, not
        detailed in Transmodel, available from constituting LEGs).
    :ivar start_time: Departure time at origin (TRIP attribute, not
        detailed in Transmodel, available from constituting LEGs).
    :ivar end_time: Arrival time at destination (TRIP attribute, not
        detailed in Transmodel, available from constituting LEGs).
    :ivar ptlegs: Number of public transport legs.
    :ivar distance: Trip distance (TRIP attribute, not detailed in
        Transmodel, available from constituting LEGs).
    :ivar operating_days: Bit string definition of operating days.
    :ivar operating_days_description: Textual description of the
        operation days, e.g., "Monday to Friday" or "not on holidays".
    :ivar feasibility: Information about the feasibility of the TRIP, in
        particular with respect to the access features used.
    :ivar situation_full_refs: A list of references to SITUATIONs.
    :ivar extension:
    """

    trip_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TripId",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        },
    )
    origin: Optional[PlaceRefStructure] = field(
        default=None,
        metadata={
            "name": "Origin",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    destination: Optional[PlaceRefStructure] = field(
        default=None,
        metadata={
            "name": "Destination",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "Duration",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    start_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "StartTime",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    end_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "EndTime",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    ptlegs: Optional[int] = field(
        default=None,
        metadata={
            "name": "PTLegs",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    distance: Optional[int] = field(
        default=None,
        metadata={
            "name": "Distance",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    operating_days: Optional[OperatingDaysStructure] = field(
        default=None,
        metadata={
            "name": "OperatingDays",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    operating_days_description: Optional[InternationalTextStructure] = field(
        default=None,
        metadata={
            "name": "OperatingDaysDescription",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    feasibility: list[FeasibilityEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "Feasibility",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    situation_full_refs: Optional[SituationRefList] = field(
        default=None,
        metadata={
            "name": "SituationFullRefs",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
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
