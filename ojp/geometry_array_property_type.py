from dataclasses import dataclass, field
from typing import List
from ojp.line_string import LineString
from ojp.point import Point
from ojp.polygon import Polygon

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class GeometryArrayPropertyType:
    """If a feature has a property which takes an array of geometry elements as
    its value, this is called a geometry array property.

    A generic type for such a geometry property is
    GeometryArrayPropertyType. The elements are always contained inline
    in the array property, referencing geometry elements or arrays of
    geometry elements via XLinks is not supported.
    """
    polygon: List[Polygon] = field(
        default_factory=list,
        metadata={
            "name": "Polygon",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "sequential": True,
        }
    )
    line_string: List[LineString] = field(
        default_factory=list,
        metadata={
            "name": "LineString",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "sequential": True,
        }
    )
    point: List[Point] = field(
        default_factory=list,
        metadata={
            "name": "Point",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "sequential": True,
        }
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )
