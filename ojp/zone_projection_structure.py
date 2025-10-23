from dataclasses import dataclass, field
from typing import List
from ojp.abstract_projection import AbstractProjection
from ojp.point_projection import PointProjection

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


@dataclass
class ZoneProjectionStructure(AbstractProjection):
    """
    Type for PROJECTION as a geospatial zone.

    :ivar boundary: Boundary line of Zone as an ordered set of points.
    """
    boundary: List["ZoneProjectionStructure.Boundary"] = field(
        default_factory=list,
        metadata={
            "name": "Boundary",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
            "min_occurs": 1,
        }
    )

    @dataclass
    class Boundary:
        point_projection: List[PointProjection] = field(
            default_factory=list,
            metadata={
                "name": "PointProjection",
                "type": "Element",
                "namespace": "http://www.ifopt.org.uk/ifopt",
                "min_occurs": 3,
            }
        )
