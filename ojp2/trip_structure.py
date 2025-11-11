from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime, XmlDuration

from ojp2.feasibility_enumeration import FeasibilityEnumeration
from ojp2.international_text_structure import InternationalTextStructure
from ojp2.leg_structure import LegStructure
from ojp2.operating_days_structure import OperatingDaysStructure
from ojp2.situation_ref_list import SituationRefList

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class TripStructure:
    """
    [an extended form of PT TRIP in TM and NeTEx as it also includes the initial
    and final access legs to and from public transport] whole journey from
    passenger origin to passenger destination in one or more LEGs.

    :ivar id: Id of this trip for referencing purposes. Unique within
        trip response.
    :ivar duration: Overall duration of the trip (TRIP attribute, not
        detailed in Transmodel, available from constituting LEGs).
    :ivar start_time: Departure time at origin (TRIP attribute, not
        detailed in Transmodel, available from constituting LEGs).
    :ivar end_time: Arrival time at destination (TRIP attribute, not
        detailed in Transmodel, available from constituting LEGs).
    :ivar transfers: Number of interchanges.
    :ivar distance: Trip distance (TRIP attribute, not detailed in
        Transmodel, available from constituting LEGs).
    :ivar leg: Legs of the trip (Transmodel: LEG or MONITORED LEG).
        Note: There is always a TransferLeg between two TimedLegs. There
        can be a TransferLeg between two ContinuousLegs (e.g., because
        some special time-consuming action is necessary like a car
        hire). There can be a TransferLeg between a ContinuousLeg and a
        TimedLeg for the same reason. There aren't two consecutive
        TransferLegs.
    :ivar operating_days: Bit string definition of operating days.
    :ivar operating_days_description: Textual description of the
        operation days, e.g., "Monday to Friday" or "not on holidays".
    :ivar unplanned: Whether this trip is an additional one that has not
        been planned. Default is false.
    :ivar cancelled: Whether this trip is cancelled and will not be run.
        Default is false.
    :ivar deviation: Whether this trip deviates from the planned service
        pattern. Default is false.
    :ivar delayed: Whether this trip is delayed. Default is false.
    :ivar infeasible: Whether this trip cannot be used, due to
        operational delays and impossible transfers. Default is false.
    :ivar feasibility: Information about the feasibility of the TRIP, in
        particular with respect to the access features used.
    :ivar situation_full_refs: A list of references to SITUATIONs.
    :ivar extension:
    """

    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        },
    )
    duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "Duration",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        },
    )
    start_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "StartTime",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        },
    )
    end_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "EndTime",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        },
    )
    transfers: Optional[int] = field(
        default=None,
        metadata={
            "name": "Transfers",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
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
    leg: list[LegStructure] = field(
        default_factory=list,
        metadata={
            "name": "Leg",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "min_occurs": 1,
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
    unplanned: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Unplanned",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    cancelled: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Cancelled",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    deviation: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Deviation",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    delayed: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Delayed",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    infeasible: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Infeasible",
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
