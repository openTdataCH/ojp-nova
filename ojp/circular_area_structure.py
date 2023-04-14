from dataclasses import dataclass, field
from typing import Optional
from ojp.location_structure import LocationStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class CircularAreaStructure(LocationStructure):
    """Type for a circular area centered around a point that may be expressed
    in concrete WGS 84 Coordinates or any gml compatible point coordinates
    format.

    (since SIRI 2.1)

    :ivar radius: Radius around the center point in meters.
    """
    radius: Optional[int] = field(
        default=None,
        metadata={
            "name": "Radius",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
