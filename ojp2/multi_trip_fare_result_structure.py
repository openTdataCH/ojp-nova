from dataclasses import dataclass, field
from typing import Optional

from ojp2.fare_product_structure import FareProductStructure
from ojp2.tariff_zone_list_in_area_structure import (
    TariffZoneListInAreaStructure,
)
from ojp2.trip_fare_product_reference_structure import (
    TripFareProductReferenceStructure,
)
from ojp2.web_link_structure import WebLinkStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class MultiTripFareResultStructure:
    """
    Structure of a Multi Trip Fare Request result.

    :ivar trip_fare_product_reference: Non-empty list of trip references
        in the corresponding MultiTripFareRequestStructure
    :ivar fare_product: Zero, one or more FareProducts that are valid
        for the referenced trips / part of trips.
    :ivar passed_zones: The set of passed zones.
    :ivar static_info_url: URL to Fare information pages on the web.
    """

    trip_fare_product_reference: list[TripFareProductReferenceStructure] = (
        field(
            default_factory=list,
            metadata={
                "name": "TripFareProductReference",
                "type": "Element",
                "namespace": "http://www.vdv.de/ojp",
                "min_occurs": 1,
            },
        )
    )
    fare_product: list[FareProductStructure] = field(
        default_factory=list,
        metadata={
            "name": "FareProduct",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    passed_zones: Optional[TariffZoneListInAreaStructure] = field(
        default=None,
        metadata={
            "name": "PassedZones",
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
