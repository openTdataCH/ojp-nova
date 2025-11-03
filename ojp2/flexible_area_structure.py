from dataclasses import dataclass, field
from typing import Optional

from ojp2.bounding_box_structure import BoundingBoxStructure
from ojp2.circular_area_structure import CircularAreaStructure
from ojp2.polygon import Polygon

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class FlexibleAreaStructure:
    """Bounding box, circular area or gml:polyon of the area where stops of a
    flexible service are called.

    (since SIRI 2.1) A flexible area is used in cases where a pre-booked
    service allows pick-up/drop-off anywhere in a designated area and
    provides a possible interchange to a higher-frequency service.

    :ivar bounding_box: Flexible area specified as a rectangular
        bounding box.
    :ivar circular_area: Flexible area specified as a circular area
        (center coordinates and radius).
    :ivar polygon: Flexible area specified as a gml:Polygon that
        consists of an interior and exterior linear ring.
    """

    bounding_box: Optional[BoundingBoxStructure] = field(
        default=None,
        metadata={
            "name": "BoundingBox",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    circular_area: Optional[CircularAreaStructure] = field(
        default=None,
        metadata={
            "name": "CircularArea",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    polygon: Optional[Polygon] = field(
        default=None,
        metadata={
            "name": "Polygon",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
