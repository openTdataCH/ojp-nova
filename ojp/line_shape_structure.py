from dataclasses import dataclass, field
from typing import List
from ojp.location_structure import LocationStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class LineShapeStructure:
    """
    Defines a line shape +SIRI v2.0.

    :ivar point: A geospatial point. +SIRI v2.0 .
    """
    point: List[LocationStructure] = field(
        default_factory=list,
        metadata={
            "name": "Point",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_occurs": 2,
        }
    )
