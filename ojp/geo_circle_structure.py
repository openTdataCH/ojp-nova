from dataclasses import dataclass, field
from typing import Optional
from ojp.location_structure import LocationStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class GeoCircleStructure:
    """
    :ivar center:
    :ivar radius: Radius in metres.
    """
    center: Optional[LocationStructure] = field(
        default=None,
        metadata={
            "name": "Center",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        }
    )
    radius: Optional[int] = field(
        default=None,
        metadata={
            "name": "Radius",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        }
    )
