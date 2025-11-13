from dataclasses import dataclass

from ojp2.point_projection_structure import PointProjectionStructure

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


@dataclass
class PointProjection(PointProjectionStructure):
    """
    Points may be defined in tagged format or using GM coordinates element.
    """

    class Meta:
        namespace = "http://www.ifopt.org.uk/ifopt"
