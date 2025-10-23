from dataclasses import dataclass, field
from typing import Optional
from ojp.location_structure import LocationStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class BoundingBoxStructure:
    """Defines a bounding box using two corner points.

    GML terminology.  +SIRI v2.0

    :ivar upper_left: A geospatial point. Upper Left corner. .
    :ivar lower_right: A geospatial point. Lower right corner. .
    """
    upper_left: Optional[LocationStructure] = field(
        default=None,
        metadata={
            "name": "UpperLeft",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    lower_right: Optional[LocationStructure] = field(
        default=None,
        metadata={
            "name": "LowerRight",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
