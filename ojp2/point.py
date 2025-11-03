from dataclasses import dataclass

from ojp2.point_type import PointType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class Point(PointType):
    """A Point is defined by a single coordinate tuple.

    The direct position of a point is specified by the pos element which
    is of type DirectPositionType.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
