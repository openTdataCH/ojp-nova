from dataclasses import dataclass, field
from typing import List, Optional
from ojp.error_message_structure import ErrorMessageStructure
from ojp.fare_product_structure import FareProductStructure
from ojp.tariff_zone_list_in_area_structure import TariffZoneListInAreaStructure
from ojp.web_link_structure import WebLinkStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class TripFareResultStructure:
    """
    Structure of a Single Trip Fare Request result.

    :ivar error_message: Result-specific error messages
    :ivar from_trip_leg_id_ref: Identifies the "valid from" trip leg.
    :ivar to_trip_leg_id_ref: Identifies the "valid to" trip leg.
    :ivar passed_zones: The sequence of passed fare zones.
    :ivar fare_product: One ore more FareProducts that are valid for
        this part of the trip.
    :ivar static_info_url: URL to static information page on the web.
    """
    error_message: List[ErrorMessageStructure] = field(
        default_factory=list,
        metadata={
            "name": "ErrorMessage",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    from_trip_leg_id_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "FromTripLegIdRef",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    to_trip_leg_id_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ToTripLegIdRef",
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
    fare_product: List[FareProductStructure] = field(
        default_factory=list,
        metadata={
            "name": "FareProduct",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    static_info_url: List[WebLinkStructure] = field(
        default_factory=list,
        metadata={
            "name": "StaticInfoUrl",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
