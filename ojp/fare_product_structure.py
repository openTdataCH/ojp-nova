from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional
from xsdata.models.datatype import XmlDuration
from ojp.booking_arrangements_container_structure import BookingArrangementsContainerStructure
from ojp.international_text_structure import InternationalTextStructure
from ojp.passenger_category_enumeration import PassengerCategoryEnumeration
from ojp.tariff_zone_list_in_area_structure import TariffZoneListInAreaStructure
from ojp.type_of_fare_class_enumeration import TypeOfFareClassEnumeration
from ojp.vat_rate_enumeration import VatRateEnumeration
from ojp.web_link_structure import WebLinkStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class FareProductStructure:
    """
    [related to FARE PRODUCT in TM and NeTEx] different FARE PRODUCTs that may be
    available with related information.

    :ivar fare_product_id: Unique Id of the FareProduct.
    :ivar fare_product_name: printable FareProduct name
    :ivar fare_authority_ref:
    :ivar fare_authority_text: Textual description or name of Fare
        authority.
    :ivar price: FareProduct price as decimal number.
    :ivar net_price: Net FareProduct price as decimal number for
        accounting purposes.
    :ivar currency: iso 4217 currency code, e.g. EUR for Euro or GBP for
        Pound Sterling
    :ivar vat_rate: Rate of value added tax. Default is unknown.
    :ivar travel_class: Travel class for which the FareProduct is valid.
    :ivar required_card: One or more traveller cards that are needed for
        purchase of this FareProduct. In most cases traveller cards
        offer discounts, f.e. BahnCard50 of Deutsche Bahn.
    :ivar valid_for: Sequence of all passenger categories for which this
        FareProduct is valid.
    :ivar validity_duration: Maximum duration of FareProduct validity
        starting with purchase of ticket or begin of journey (ticket
        validation).
    :ivar validity_duration_text: Textual description of maximum
        validity duration.
    :ivar validity_tariff_zones: Spatial validity of FareProduct defined
        as list of fare zones.
    :ivar validity_area_text: Textual description of spatial validity.
    :ivar info_url: URL to information for this FareProduct
    :ivar sale_url: URL to buy the FareProduct online
    :ivar booking_arrangements:
    :ivar extension:
    """
    fare_product_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "FareProductId",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        }
    )
    fare_product_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "FareProductName",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        }
    )
    fare_authority_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "FareAuthorityRef",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        }
    )
    fare_authority_text: Optional[str] = field(
        default=None,
        metadata={
            "name": "FareAuthorityText",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        }
    )
    price: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Price",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    net_price: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NetPrice",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    currency: Optional[str] = field(
        default=None,
        metadata={
            "name": "Currency",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    vat_rate: Optional[VatRateEnumeration] = field(
        default=None,
        metadata={
            "name": "VatRate",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    travel_class: Optional[TypeOfFareClassEnumeration] = field(
        default=None,
        metadata={
            "name": "TravelClass",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    required_card: List[str] = field(
        default_factory=list,
        metadata={
            "name": "RequiredCard",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    valid_for: List[PassengerCategoryEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "ValidFor",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    validity_duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "ValidityDuration",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    validity_duration_text: Optional[InternationalTextStructure] = field(
        default=None,
        metadata={
            "name": "ValidityDurationText",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    validity_tariff_zones: List[TariffZoneListInAreaStructure] = field(
        default_factory=list,
        metadata={
            "name": "ValidityTariffZones",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    validity_area_text: Optional[InternationalTextStructure] = field(
        default=None,
        metadata={
            "name": "ValidityAreaText",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    info_url: List[WebLinkStructure] = field(
        default_factory=list,
        metadata={
            "name": "InfoUrl",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    sale_url: List[WebLinkStructure] = field(
        default_factory=list,
        metadata={
            "name": "SaleUrl",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    booking_arrangements: List[BookingArrangementsContainerStructure] = field(
        default_factory=list,
        metadata={
            "name": "BookingArrangements",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    extension: Optional[object] = field(
        default=None,
        metadata={
            "name": "Extension",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
