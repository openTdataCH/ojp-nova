from dataclasses import dataclass, field
from typing import List, Optional
from ojp.error_message_structure import ErrorMessageStructure
from ojp.fare_product_structure import FareProductStructure
from ojp.tariff_zone_list_in_area_structure import TariffZoneListInAreaStructure
from ojp.trip_fare_product_reference_structure import TripFareProductReferenceStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class MultiTripFareResultStructure:
    """
    Structure of a Multi Trip Fare Request result.

    :ivar error_message: Result-specific error messages.
    :ivar trip_fare_product_reference: Non-empty list of trip references
        in the corresponding MultiTripFareRequestStructure
    :ivar fare_product: Zero, one or more FareProducts that are valid
        for the referenced trips / part of trips.
    :ivar passed_zones: The set of passed zones.
    :ivar static_info_url: URL to Fare information pages on the web.
    """
    error_message: List[ErrorMessageStructure] = field(
        default_factory=list,
        metadata={
            "name": "ErrorMessage",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    trip_fare_product_reference: List[TripFareProductReferenceStructure] = field(
        default_factory=list,
        metadata={
            "name": "TripFareProductReference",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "min_occurs": 1,
        }
    )
    fare_product: List[FareProductStructure] = field(
        default_factory=list,
        metadata={
            "name": "FareProduct",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    passed_zones: Optional[TariffZoneListInAreaStructure] = field(
        default=None,
        metadata={
            "name": "PassedZones",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    static_info_url: List[str] = field(
        default_factory=list,
        metadata={
            "name": "StaticInfoUrl",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
