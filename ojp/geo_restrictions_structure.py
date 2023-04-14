from dataclasses import dataclass, field
from typing import Optional
from ojp.geo_area_structure import GeoAreaStructure
from ojp.geo_circle_structure import GeoCircleStructure
from ojp.geo_rectangle_structure import GeoRectangleStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class GeoRestrictionsStructure:
    """
    :ivar circle:
    :ivar rectangle:
    :ivar area: Area is defined by a polyline
    """
    circle: Optional[GeoCircleStructure] = field(
        default=None,
        metadata={
            "name": "Circle",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    rectangle: Optional[GeoRectangleStructure] = field(
        default=None,
        metadata={
            "name": "Rectangle",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    area: Optional[GeoAreaStructure] = field(
        default=None,
        metadata={
            "name": "Area",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
