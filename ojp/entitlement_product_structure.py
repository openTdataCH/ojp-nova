from dataclasses import dataclass, field
from typing import Optional
from ojp.half_open_timestamp_output_range_structure import HalfOpenTimestampOutputRangeStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class EntitlementProductStructure:
    """[a specific form of TRAVEL DOCUMENT in TM and NeTEx] Precondition to
    access a service or to purchase a FARE PRODUCT issued by an organisation
    that may not be a PT operator (e.g. military card, concessionary card,
    ...).

    In most cases, ENTITLEMENT PRODUCTs offer discounts, e.g. the
    "BahnCard50" of "Deutsche Bahn".

    :ivar fare_authority_ref: Reference to the fare authority that
        issued the ENTITLEMENT PRODUCT
    :ivar entitlement_product_ref: Identifier of the ENTITLEMENT PRODUCT
        (e.g. BahnCard50, BahnCard50First, ...)
    :ivar validity_period: Validity period of the ENTITLEMENT PRODUCT
    :ivar entitlement_product_name: Name of the ENTITLEMENT PRODUCT
    """
    fare_authority_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "FareAuthorityRef",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        }
    )
    entitlement_product_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "EntitlementProductRef",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        }
    )
    validity_period: Optional[HalfOpenTimestampOutputRangeStructure] = field(
        default=None,
        metadata={
            "name": "ValidityPeriod",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    entitlement_product_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "EntitlementProductName",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        }
    )
