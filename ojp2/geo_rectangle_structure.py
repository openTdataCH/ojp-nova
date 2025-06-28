from dataclasses import dataclass, field
from typing import Optional

from ojp2.location_structure import LocationStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class GeoRectangleStructure:
    """
    :ivar upper_left: Upper-left (north-west) corner of the rectangle.
    :ivar lower_right: Lower-right (south-east) corner of the rectangle.
    """

    upper_left: Optional[LocationStructure] = field(
        default=None,
        metadata={
            "name": "UpperLeft",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        },
    )
    lower_right: Optional[LocationStructure] = field(
        default=None,
        metadata={
            "name": "LowerRight",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        },
    )
