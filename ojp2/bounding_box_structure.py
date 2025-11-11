from dataclasses import dataclass, field
from typing import Optional

from ojp2.location_structure import LocationStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class BoundingBoxStructure:
    """Defines a bounding box using two corner points.

    GML terminology.  (since SIRI 2.0)

    :ivar upper_left: Upper Left corner as a geospatial point.
    :ivar lower_right: Lower right corner as a geospatial point.
    """

    upper_left: Optional[LocationStructure] = field(
        default=None,
        metadata={
            "name": "UpperLeft",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    lower_right: Optional[LocationStructure] = field(
        default=None,
        metadata={
            "name": "LowerRight",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
