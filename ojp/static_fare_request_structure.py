from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class StaticFareRequestStructure:
    """General Fare information.

    May depend on date.

    :ivar date: Date for which to retrieve Fare information.
    :ivar fare_product_ref:
    """
    date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Date",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    fare_product_ref: List[str] = field(
        default_factory=list,
        metadata={
            "name": "FareProductRef",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
