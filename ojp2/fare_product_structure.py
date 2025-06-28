from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDuration

from ojp2.booking_arrangements_container_structure import (
    BookingArrangementsContainerStructure,
)
from ojp2.entitlement_product_structure import EntitlementProductStructure
from ojp2.fare_authority_ref import FareAuthorityRef
from ojp2.fare_class_enumeration import FareClassEnumeration
from ojp2.international_text_structure import InternationalTextStructure
from ojp2.passenger_category_enumeration import PassengerCategoryEnumeration
from ojp2.tariff_zone_list_in_area_structure import (
    TariffZoneListInAreaStructure,
)
from ojp2.web_link_structure import WebLinkStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class FareProductStructure:
    """
    [related to FARE PRODUCT in TM and NeTEx] different FARE PRODUCTs that may be
    available with related information.

    :ivar fare_product_id: Identifier of a FareProduct
    :ivar fare_product_name: Printable FareProduct name
    :ivar fare_authority_ref:
    :ivar fare_authority_text: Textual description or name of Fare
        authority.
    :ivar proto_product: Is this product a proto product? Default is
        false. If true, it should not be shown to the user. In a
        distributed environment (e.g., EU-Spirit) partial systems may
        generate incomplete product information (proto product), which
        has to be processed further and combined with other information
        before it is a complete fare product and can be shown to the
        user. See https://eu-spirit.eu/
    :ivar price: FareProduct price as decimal number.
    :ivar net_price: Net FareProduct price as decimal number for
        accounting purposes.
    :ivar currency: iso 4217 currency code, e.g., EUR for Euro or GBP
        for Pound Sterling
    :ivar vat_rate: Rate of value added tax.
    :ivar fare_quota: Remaining offered tickets in this FARE PRODUCT.
        When absent, the number of remaining tickets is unknown or not
        limited. In most cases if the FareQuota is zero then the
        FareProduct is not shown.
    :ivar fare_class: Fare class for which the FareProduct is valid
        (Transmodel: CLASS OF USE).
    :ivar required_card: One or more ENTITLEMENT PRODUCTs required for
        the purchase of this FareProduct. In most cases, ENTITLEMENT
        PRODUCTs offer discounts, e.g., the "BahnCard50" of "Deutsche
        Bahn".
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
    :ivar sale_url: URL to buy the FareProduct online.
    :ivar booking_arrangements: Multiple sets of multiple booking
        arrangements for different legs of a journey.
    :ivar extension:
    """

    fare_product_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "FareProductId",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        },
    )
    fare_product_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "FareProductName",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        },
    )
    fare_authority_ref: Optional[FareAuthorityRef] = field(
        default=None,
        metadata={
            "name": "FareAuthorityRef",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        },
    )
    fare_authority_text: Optional[str] = field(
        default=None,
        metadata={
            "name": "FareAuthorityText",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        },
    )
    proto_product: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ProtoProduct",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    price: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Price",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    net_price: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NetPrice",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    currency: Optional[str] = field(
        default=None,
        metadata={
            "name": "Currency",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    vat_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "VatRate",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "min_inclusive": Decimal("0.0"),
            "max_inclusive": Decimal("100.0"),
        },
    )
    fare_quota: Optional[int] = field(
        default=None,
        metadata={
            "name": "FareQuota",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    fare_class: Optional[FareClassEnumeration] = field(
        default=None,
        metadata={
            "name": "FareClass",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    required_card: list[EntitlementProductStructure] = field(
        default_factory=list,
        metadata={
            "name": "RequiredCard",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    valid_for: list[PassengerCategoryEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "ValidFor",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    validity_duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "ValidityDuration",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    validity_duration_text: Optional[InternationalTextStructure] = field(
        default=None,
        metadata={
            "name": "ValidityDurationText",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    validity_tariff_zones: list[TariffZoneListInAreaStructure] = field(
        default_factory=list,
        metadata={
            "name": "ValidityTariffZones",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    validity_area_text: Optional[InternationalTextStructure] = field(
        default=None,
        metadata={
            "name": "ValidityAreaText",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    info_url: list[WebLinkStructure] = field(
        default_factory=list,
        metadata={
            "name": "InfoUrl",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    sale_url: list[WebLinkStructure] = field(
        default_factory=list,
        metadata={
            "name": "SaleUrl",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    booking_arrangements: list[BookingArrangementsContainerStructure] = field(
        default_factory=list,
        metadata={
            "name": "BookingArrangements",
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
