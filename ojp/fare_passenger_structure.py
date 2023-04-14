from dataclasses import dataclass, field
from typing import List, Optional
from ojp.passenger_category_enumeration import PassengerCategoryEnumeration
from ojp.tariff_zone_ref_list_structure import TariffZoneRefListStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class FarePassengerStructure:
    """
    [a specialised form of USER PROFILE in TM and NeTEx] attributes of a
    passenger that influence the price to be paid by that passenger for a FARE
    PRODUCT.

    :ivar age: Age of the passenger on the day of travel.
    :ivar passenger_category: sequence of all passenger categories, for
        which this FareProduct is valid
    :ivar entitlement_product: [a specific form of TRAVEL DOCUMENT in TM
        and NeTEx] a precondition to access a service or to purchase a
        FARE PRODUCT issued by an organisation that may not be a PT
        operator (eg: military card, concessionary card, etc)
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
        }
    )
    passenger_category: Optional[PassengerCategoryEnumeration] = field(
        default=None,
        metadata={
            "name": "PassengerCategory",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    entitlement_product: List[str] = field(
        default_factory=list,
        metadata={
            "name": "EntitlementProduct",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    zones_already_paid: Optional[TariffZoneRefListStructure] = field(
        default=None,
        metadata={
            "name": "ZonesAlreadyPaid",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    sales_package_element_ref: List[str] = field(
        default_factory=list,
        metadata={
            "name": "SalesPackageElementRef",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
