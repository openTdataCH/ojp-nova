from dataclasses import dataclass, field
from typing import Optional

from ojp2.geo_area_structure import GeoAreaStructure
from ojp2.geo_circle_structure import GeoCircleStructure
from ojp2.geo_rectangle_structure import GeoRectangleStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class GeoRestrictionsStructure:
    """
    :ivar circle: Area defined by a circle.
    :ivar rectangle: Area defined by a rectangle.
    :ivar area: Area defined by a polyline.
    """

    circle: Optional[GeoCircleStructure] = field(
        default=None,
        metadata={
            "name": "Circle",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    rectangle: Optional[GeoRectangleStructure] = field(
        default=None,
        metadata={
            "name": "Rectangle",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    area: Optional[GeoAreaStructure] = field(
        default=None,
        metadata={
            "name": "Area",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
