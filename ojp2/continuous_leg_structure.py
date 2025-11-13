from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime, XmlDuration

from ojp2.continuous_service_structure import ContinuousServiceStructure
from ojp2.emission_co2_structure import EmissionCo2Structure
from ojp2.feasibility_enumeration import FeasibilityEnumeration
from ojp2.international_text_structure import InternationalTextStructure
from ojp2.leg_track_structure import LegTrackStructure
from ojp2.path_guidance_structure import PathGuidanceStructure
from ojp2.place_ref_structure import PlaceRefStructure
from ojp2.situation_ref_list import SituationRefList

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class ContinuousLegStructure:
    """
    [relates to a specific type of RIDE LEG with Timed=false or an ACCESS LEG in TM
    and NeTEx] leg of a journey that is not bound to a timetable.

    :ivar leg_start: PLACE where the leg starts (can be a PLACE,
        SCHEDULED STOP POINT or a VEHICLE MEETING POINT) with time
        information.
    :ivar leg_end: PLACE to alight (can be a SCHEDULED STOP POINT or a
        VEHICLE MEETING POINT) with time information.
    :ivar service: Service of this leg.
    :ivar time_window_start: Time at which window begins.
    :ivar time_window_end: Time at which window ends.
    :ivar duration: Duration of this leg according to user preferences
        like walking speed.
    :ivar leg_description: Title or summary of this leg for overview.
    :ivar length: Length of the leg.
    :ivar leg_track: Detailed description of each element of this leg
        including geometric projection.
    :ivar path_guidance: Structured model further describing this
        interchange, its geographic embedding and accessibility
        (LEG.PATH GUIDANCE).
    :ivar feasibility: Information about the feasibility of the
        ContinuousLeg, in particular with respect to the access features
        used.
    :ivar situation_full_refs: A list of references to SITUATIONs.
    :ivar emission_co2: Estimation of CO2 emissions.
    :ivar extension:
    """

    leg_start: Optional[PlaceRefStructure] = field(
        default=None,
        metadata={
            "name": "LegStart",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        },
    )
    leg_end: Optional[PlaceRefStructure] = field(
        default=None,
        metadata={
            "name": "LegEnd",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        },
    )
    service: Optional[ContinuousServiceStructure] = field(
        default=None,
        metadata={
            "name": "Service",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        },
    )
    time_window_start: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "TimeWindowStart",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    time_window_end: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "TimeWindowEnd",
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
            "required": True,
        },
    )
    leg_description: Optional[InternationalTextStructure] = field(
        default=None,
        metadata={
            "name": "LegDescription",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    length: Optional[int] = field(
        default=None,
        metadata={
            "name": "Length",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    leg_track: Optional[LegTrackStructure] = field(
        default=None,
        metadata={
            "name": "LegTrack",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    path_guidance: Optional[PathGuidanceStructure] = field(
        default=None,
        metadata={
            "name": "PathGuidance",
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
    emission_co2: Optional[EmissionCo2Structure] = field(
        default=None,
        metadata={
            "name": "EmissionCO2",
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
