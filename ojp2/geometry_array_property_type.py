from dataclasses import dataclass, field

from ojp2.line_string import LineString
from ojp2.point import Point
from ojp2.polygon import Polygon

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class GeometryArrayPropertyType:
    """If a feature has a property which takes an array of geometry elements as its
    value, this is called a geometry array property.

    A generic type for such a geometry property is
    GeometryArrayPropertyType. The elements are always contained inline
    in the array property, referencing geometry elements or arrays of
    geometry elements via XLinks is not supported.
    """

    polygon: list[Polygon] = field(
        default_factory=list,
        metadata={
            "name": "Polygon",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "sequence": 1,
        },
    )
    line_string: list[LineString] = field(
        default_factory=list,
        metadata={
            "name": "LineString",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "sequence": 1,
        },
    )
    point: list[Point] = field(
        default_factory=list,
        metadata={
            "name": "Point",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "sequence": 1,
        },
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
