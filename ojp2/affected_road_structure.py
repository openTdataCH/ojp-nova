from dataclasses import dataclass, field
from typing import Optional

from ojp2.extensions_2 import Extensions2
from ojp2.link_projection_structure import LinkProjectionStructure
from ojp2.offset_structure import OffsetStructure
from ojp2.roadside_reference_point_linear import RoadsideReferencePointLinear

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class AffectedRoadStructure:
    """
    Type for Raod scope for scope of SITUATION or effect.

    :ivar road: Affected Road as described by a Date2x location.
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
        },
    )
    link_projection: Optional[LinkProjectionStructure] = field(
        default=None,
        metadata={
            "name": "LinkProjection",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    offset: Optional[OffsetStructure] = field(
        default=None,
        metadata={
            "name": "Offset",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    extensions: Optional[Extensions2] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
