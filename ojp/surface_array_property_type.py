from dataclasses import dataclass, field
from typing import List
from ojp.polygon import Polygon

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class SurfaceArrayPropertyType:
    """gml:SurfaceArrayPropertyType is a container for an array of surfaces.

    The elements are always contained in the array property, referencing
    geometry elements or arrays of geometry elements via XLinks is not
    supported.
    """
    polygon: List[Polygon] = field(
        default_factory=list,
        metadata={
            "name": "Polygon",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )
