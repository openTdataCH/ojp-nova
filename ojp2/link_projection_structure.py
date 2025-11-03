from dataclasses import dataclass, field
from typing import Optional

from ojp2.abstract_projection import AbstractProjection
from ojp2.point_projection import PointProjection

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


@dataclass
class LinkProjectionStructure(AbstractProjection):
    """
    Type for PROJECTION as a geospatial polyline.

    :ivar line: Ordered sequence of points. There must always be a start
        and end point.
    """

    line: Optional["LinkProjectionStructure.Line"] = field(
        default=None,
        metadata={
            "name": "Line",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
        },
    )

    @dataclass
    class Line:
        point_projection: list[PointProjection] = field(
            default_factory=list,
            metadata={
                "name": "PointProjection",
                "type": "Element",
                "namespace": "http://www.ifopt.org.uk/ifopt",
                "min_occurs": 2,
            },
        )
