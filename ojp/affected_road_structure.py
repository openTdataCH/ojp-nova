from dataclasses import dataclass, field
from typing import Optional
from ojp.extensions_1 import Extensions1
from ojp.link_projection_structure import LinkProjectionStructure
from ojp.offset_structure import OffsetStructure
from ojp.roadside_reference_point_linear import RoadsideReferencePointLinear

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class AffectedRoadStructure:
    """
    Type for Raod scope for scope of SITUATION or effect.

    :ivar road: AFfected Road as described by a Date2x location.
    :ivar link_projection: GIs projection of Section. NB Line here means
        Geometry Polyline, not Transmodel Transport Line.
    :ivar offset: Offset from start or end of section to use when
        projecting.
    :ivar extensions:
    """
    road: Optional[RoadsideReferencePointLinear] = field(
        default=None,
        metadata={
            "name": "Road",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    link_projection: Optional[LinkProjectionStructure] = field(
        default=None,
        metadata={
            "name": "LinkProjection",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    offset: Optional[OffsetStructure] = field(
        default=None,
        metadata={
            "name": "Offset",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    extensions: Optional[Extensions1] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
