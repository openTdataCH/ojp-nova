from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDuration

from ojp2.linear_shape_structure import LinearShapeStructure
from ojp2.place_ref_structure import PlaceRefStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class TrackSectionStructure:
    """
    SECTION of a LEG TRACK on the infrastructure network of the LEG together with
    time information.

    :ivar track_section_start: Start place of this track section (Start
        of a SECTION of a LEG.TRACK).
    :ivar track_section_end: End place of this track section (End of a
        SECTION of a LEG.TRACK).
    :ivar link_projection: An oriented correspondence from one LINK of a
        source layer, onto an entity in a target layer: e.g., LINK
        SEQUENCE.
    :ivar road_name: Name of the road this track section is attached to
        (LEG TRACK.SECTION NAME, may also be something like "bicycle
        line along Tellstrasse").
    :ivar duration: Duration the passenger needs to travel through this
        track section.
    :ivar length: Length of this track section.
    :ivar extension:
    """

    track_section_start: Optional[PlaceRefStructure] = field(
        default=None,
        metadata={
            "name": "TrackSectionStart",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    track_section_end: Optional[PlaceRefStructure] = field(
        default=None,
        metadata={
            "name": "TrackSectionEnd",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    link_projection: Optional[LinearShapeStructure] = field(
        default=None,
        metadata={
            "name": "LinkProjection",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    road_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "RoadName",
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
    length: Optional[int] = field(
        default=None,
        metadata={
            "name": "Length",
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
