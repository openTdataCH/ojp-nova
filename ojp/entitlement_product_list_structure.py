from dataclasses import dataclass, field
from typing import List
from ojp.entitlement_product_structure import EntitlementProductStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class EntitlementProductListStructure:
    """
    A list of ENTITLEMENT PRODUCTs.

    :ivar entitlement_product: [a specific form of TRAVEL DOCUMENT in TM
        and NeTEx] Precondition to access a service or to purchase a
        FARE PRODUCT issued by an organisation that may not be a PT
        operator (e.g. military card, concessionary card, ...). In most
        cases, ENTITLEMENT PRODUCTs offer discounts, e.g. the
        "BahnCard50" of "Deutsche Bahn".
    """
    entitlement_product: List[EntitlementProductStructure] = field(
        default_factory=list,
        metadata={
            "name": "EntitlementProduct",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "min_occurs": 1,
        }
    )
