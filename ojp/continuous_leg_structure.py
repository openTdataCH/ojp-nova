from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime, XmlDuration
from ojp.continuous_service_structure import ContinuousServiceStructure
from ojp.international_text_structure import InternationalTextStructure
from ojp.leg_track_structure import LegTrackStructure
from ojp.path_guidance_structure import PathGuidanceStructure
from ojp.place_ref_structure import PlaceRefStructure
from ojp.situation_full_ref_2 import SituationFullRef2

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class ContinuousLegStructure:
    """
    [relates to a specific type of RIDE in TM and NeTEx] leg of a journey that
    is not bound to a timetable.

    :ivar leg_start: Stop/Station where boarding is done
    :ivar leg_end: Stop/Station to alight
    :ivar service: Service of this leg. May be "walk" in most cases, but
        also cycling or taxi etc.
    :ivar time_window_start: Time at which window begins.
    :ivar time_window_end: Time at which window ends.
    :ivar duration: Duration of this leg according to user preferences
        like walk speed.
    :ivar leg_description: Title or summary of this leg for overview.
    :ivar length: Length of the leg.
    :ivar leg_track: Detailed description of each element of this leg
        including geometric projection.
    :ivar path_guidance: Structured model further describing this
        interchange, its geographic embedding and accessibility.
    :ivar situation_full_ref:
    :ivar extension:
    """
    leg_start: Optional[PlaceRefStructure] = field(
        default=None,
        metadata={
            "name": "LegStart",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        }
    )
    leg_end: Optional[PlaceRefStructure] = field(
        default=None,
        metadata={
            "name": "LegEnd",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        }
    )
    service: Optional[ContinuousServiceStructure] = field(
        default=None,
        metadata={
            "name": "Service",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        }
    )
    time_window_start: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "TimeWindowStart",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    time_window_end: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "TimeWindowEnd",
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
            "required": True,
        }
    )
    leg_description: Optional[InternationalTextStructure] = field(
        default=None,
        metadata={
            "name": "LegDescription",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    length: Optional[int] = field(
        default=None,
        metadata={
            "name": "Length",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    leg_track: Optional[LegTrackStructure] = field(
        default=None,
        metadata={
            "name": "LegTrack",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    path_guidance: Optional[PathGuidanceStructure] = field(
        default=None,
        metadata={
            "name": "PathGuidance",
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
