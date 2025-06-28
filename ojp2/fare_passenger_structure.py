from dataclasses import dataclass, field
from typing import Optional

from ojp2.entitlement_product_list_structure import (
    EntitlementProductListStructure,
)
from ojp2.fare_product_ref_structure import FareProductRefStructure
from ojp2.passenger_category_enumeration import PassengerCategoryEnumeration
from ojp2.tariff_zone_ref_list_structure import TariffZoneRefListStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class FarePassengerStructure:
    """
    [a specialised form of USER PROFILE in TM and NeTEx] attributes of a passenger
    that influence the price to be paid by that passenger for a FARE PRODUCT.

    :ivar age: Age of the passenger on the day of travel.
    :ivar passenger_category: sequence of all passenger categories, for
        which this FareProduct is valid
    :ivar entitlement_products: A list of ENTITLEMENT PRODUCTs.
    :ivar zones_already_paid: Fare zones for which the passenger already
        has a valid FareProduct.
    :ivar sales_package_element_ref: Id of a FareProduct that the
        passenger already holds and that may be used for the travel or
        parts of it.
    """

    age: Optional[int] = field(
        default=None,
        metadata={
            "name": "Age",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    passenger_category: Optional[PassengerCategoryEnumeration] = field(
        default=None,
        metadata={
            "name": "PassengerCategory",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    entitlement_products: Optional[EntitlementProductListStructure] = field(
        default=None,
        metadata={
            "name": "EntitlementProducts",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    zones_already_paid: Optional[TariffZoneRefListStructure] = field(
        default=None,
        metadata={
            "name": "ZonesAlreadyPaid",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    sales_package_element_ref: list[FareProductRefStructure] = field(
        default_factory=list,
        metadata={
            "name": "SalesPackageElementRef",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
