from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDate

from ojp2.fare_product_ref import FareProductRef

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class StaticFareRequestStructure:
    """General Fare information.

    May depend on date.

    :ivar date: Date for which to retrieve Fare information.
    :ivar fare_product_ref: Reference to a FareProduct. If no
        FareProductRef is specified, the responding system should reply
        with information about all available fare products.
    """

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
