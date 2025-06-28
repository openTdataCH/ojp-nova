from dataclasses import dataclass, field

from ojp2.track_section_structure import TrackSectionStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class LegTrackStructure:
    """
    The LINK PROJECTION of a Leg onto the topography of the route being followed.

    :ivar track_section: A geographical view of a Transmodel LEG TRACK
        together with duration and length that can be used for
        representing the leg on a map. The points may be STOP PLACE,
        SCHEDULED STOP POINT, coordinates, or ADDRESSes. Specialisation
        of SECTION.
    """

    track_section: list[TrackSectionStructure] = field(
        default_factory=list,
        metadata={
            "name": "TrackSection",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "min_occurs": 1,
        },
    )
