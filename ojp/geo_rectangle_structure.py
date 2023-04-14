from dataclasses import dataclass, field
from typing import Optional
from ojp.location_structure import LocationStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class GeoRectangleStructure:
    upper_left: Optional[LocationStructure] = field(
        default=None,
        metadata={
            "name": "UpperLeft",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        }
    )
    lower_right: Optional[LocationStructure] = field(
        default=None,
        metadata={
            "name": "LowerRight",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        }
    )
