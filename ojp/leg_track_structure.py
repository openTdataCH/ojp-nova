from dataclasses import dataclass, field
from typing import List
from ojp.track_section_structure import TrackSectionStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class LegTrackStructure:
    """
    The LINK PROJECTION of a Leg onto the topography of the route being followed.

    :ivar track_section: LINK PROJECTION on the infrastructure network
        of the TRIP LEG together with time information
    """
    track_section: List[TrackSectionStructure] = field(
        default_factory=list,
        metadata={
            "name": "TrackSection",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "min_occurs": 1,
        }
    )
