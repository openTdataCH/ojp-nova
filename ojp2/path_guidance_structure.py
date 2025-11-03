from dataclasses import dataclass, field

from ojp2.path_guidance_section_structure import PathGuidanceSectionStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class PathGuidanceStructure:
    """Description of a piece of a TRIP.

    May include geographic information, turn instructions and
    accessibility information.

    :ivar path_guidance_section: A view of LEG TRACK including PATH
        JUNCTION information, PATH LINK information and PATH GUIDANCE.
        One or more path guidance sections that form the LEG. For a good
        PATH GUIDANCE, a fine granularity of the sections may be needed.
        This may also depend on the MODE and the type of guidance
        required.
    """

    path_guidance_section: list[PathGuidanceSectionStructure] = field(
        default_factory=list,
        metadata={
            "name": "PathGuidanceSection",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "min_occurs": 1,
        },
    )
