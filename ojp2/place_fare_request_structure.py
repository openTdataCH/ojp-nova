from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDate

from ojp2.fare_product_ref import FareProductRef
from ojp2.place_structure import PlaceStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class PlaceFareRequestStructure:
    """Sub-request: PLACE related fare information. This doesn't make a lot of sense for addresses, topographic place, and coordinates. However, STOP PLACE, SCHEDULED STOP POINT and POINT OF INTEREST are different.

    :ivar place: Place to get FAREs from (usually use only StopPoint,
        StopPlace and PointOfInterest).
    :ivar date: Date for which to retrieve Fare information.
    :ivar fare_product_ref: Reference to a FareProduct. If no
        FareProductRef is specified, the responding system should reply
        with information about all available fare products.
    """

    place: Optional[PlaceStructure] = field(
        default=None,
        metadata={
            "name": "Place",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        },
    )
    date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Date",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    fare_product_ref: list[FareProductRef] = field(
        default_factory=list,
        metadata={
            "name": "FareProductRef",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
