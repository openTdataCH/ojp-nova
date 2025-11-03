from dataclasses import dataclass, field
from typing import Optional

from ojp2.abstract_surface_type import AbstractSurfaceType
from ojp2.exterior import Exterior
from ojp2.interior import Interior

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class PolygonType(AbstractSurfaceType):
    exterior: Optional[Exterior] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    interior: list[Interior] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
