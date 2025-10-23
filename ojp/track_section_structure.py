from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDuration
from ojp.location_structure import LocationStructure
from ojp.place_ref_structure import PlaceRefStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class TrackSectionStructure:
    """
    LINK PROJECTION on the infrastructure network of the TRIP LEG together with
    time information.

    :ivar track_start: Start location of this track.
    :ivar track_end: End location of this track.
    :ivar link_projection: an oriented correspondence from one LINK of a
        source layer, onto an entity in a target layer: e.g. LINK
        SEQUENCE, COMPLEX FEATURE, within a defined TYPE OF PROJECTION
    :ivar road_name: Name of the road this track section is attached to.
    :ivar duration: Duration the passenger needs to travel through this
        track section.
    :ivar length: Length of this track section.
    :ivar extension:
    """
    track_start: Optional[PlaceRefStructure] = field(
        default=None,
        metadata={
            "name": "TrackStart",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    track_end: Optional[PlaceRefStructure] = field(
        default=None,
        metadata={
            "name": "TrackEnd",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    link_projection: Optional["TrackSectionStructure.LinkProjection"] = field(
        default=None,
        metadata={
            "name": "LinkProjection",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    road_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "RoadName",
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
    extension: Optional[object] = field(
        default=None,
        metadata={
            "name": "Extension",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )

    @dataclass
    class LinkProjection:
        position: List[LocationStructure] = field(
            default_factory=list,
            metadata={
                "name": "Position",
                "type": "Element",
                "namespace": "http://www.vdv.de/ojp",
                "min_occurs": 2,
            }
        )
