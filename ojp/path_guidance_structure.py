from dataclasses import dataclass, field
from typing import List
from ojp.path_guidance_section_structure import PathGuidanceSectionStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class PathGuidanceStructure:
    """description of a piece of a TRIP.

    May include geographic information, turn instructions and
    accessibility information

    :ivar path_guidance_section: one or more path guidance sections that
        build the trip Leg
    """
    path_guidance_section: List[PathGuidanceSectionStructure] = field(
        default_factory=list,
        metadata={
            "name": "PathGuidanceSection",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "min_occurs": 1,
        }
    )
