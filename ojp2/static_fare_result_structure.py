from dataclasses import dataclass, field
from typing import Optional

from ojp2.fare_product_structure import FareProductStructure
from ojp2.web_link_structure import WebLinkStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class StaticFareResultStructure:
    """
    General Fare information.

    :ivar fare_product: [related to FARE PRODUCT in TM and NeTEx]
        different FARE PRODUCTs that may be available with related
        information.
    :ivar static_info_url: URL to information page on the web.
    :ivar extension:
    """

    fare_product: list[FareProductStructure] = field(
        default_factory=list,
        metadata={
            "name": "FareProduct",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    static_info_url: list[WebLinkStructure] = field(
        default_factory=list,
        metadata={
            "name": "StaticInfoUrl",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    extension: Optional[object] = field(
        default=None,
        metadata={
            "name": "Extension",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
