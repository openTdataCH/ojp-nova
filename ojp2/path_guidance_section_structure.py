from dataclasses import dataclass, field
from typing import Optional

from ojp2.follow_structure import FollowStructure
from ojp2.guidance_advice_enumeration import GuidanceAdviceEnumeration
from ojp2.international_text_structure import InternationalTextStructure
from ojp2.path_link_structure import PathLinkStructure
from ojp2.situation_ref_list import SituationRefList
from ojp2.track_section_structure import TrackSectionStructure
from ojp2.turn_action_enumeration import TurnActionEnumeration

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class PathGuidanceSectionStructure:
    """An extended definition of a NAVIGATION PATH in TMv6 and PATH GUIDANCE to
    include the textual navigation instructions.

    Description of a part of a TRIP. May include geographic information,
    turn instructions and accessibility information.

    :ivar track_section: An aggregate of information that may be leaning
        on LEG TRACK together with duration and length that can be used
        for representing the leg on a map. The points may be STOP PLACE,
        SCHEDULED STOP POINT, coordinates, or ADDRESSes.
    :ivar turn_description: Textual description of a traveller
        manoeuvre. Contains information from manoeuvre, TurnAction, and
        TrackSection.RoadName.
    :ivar guidance_advice: Several types of guidance advice given to
        traveller (according to Transmodel a view of a LEG TRACK and
        PATH GUIDANCE).
    :ivar turn_action: The range of possible turns that can be described
        (according to Transmodel a view of a LEG TRACK and PATH
        GUIDANCE).
    :ivar road_name: Road name
    :ivar follow: Signs, roads, POI to follow.
    :ivar direction_hint: Textual direction hint for better
        understanding, e.g., "follow signs to Hamburg" (according to
        Transmodel a view of a LEG TRACK and PATH GUIDANCE).
    :ivar absolute_bearing: Absolute bearing (sky direction) after the
        described manoeuvre.
    :ivar path_link: Description of the type of accessibility on this
        navigation section. This view is simplified in comparison to the
        NeTEx PathLink structure.
    :ivar situation_full_refs: A list of references to SITUATIONs.
    """

    track_section: Optional[TrackSectionStructure] = field(
        default=None,
        metadata={
            "name": "TrackSection",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    turn_description: Optional[InternationalTextStructure] = field(
        default=None,
        metadata={
            "name": "TurnDescription",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    guidance_advice: Optional[GuidanceAdviceEnumeration] = field(
        default=None,
        metadata={
            "name": "GuidanceAdvice",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    turn_action: Optional[TurnActionEnumeration] = field(
        default=None,
        metadata={
            "name": "TurnAction",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    road_name: Optional[InternationalTextStructure] = field(
        default=None,
        metadata={
            "name": "RoadName",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    follow: list[FollowStructure] = field(
        default_factory=list,
        metadata={
            "name": "Follow",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    direction_hint: Optional[InternationalTextStructure] = field(
        default=None,
        metadata={
            "name": "DirectionHint",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    absolute_bearing: Optional[float] = field(
        default=None,
        metadata={
            "name": "AbsoluteBearing",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    path_link: Optional[PathLinkStructure] = field(
        default=None,
        metadata={
            "name": "PathLink",
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
