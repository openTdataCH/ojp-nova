from dataclasses import dataclass, field
from typing import List, Optional
from ojp.tariff_zone_structure import TariffZoneStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class TariffZoneListInAreaStructure:
    """
    List of fare zones within the area of a Fare Authority.

    :ivar fare_authority_ref:
    :ivar fare_authority_text: Textual description or name of Fare
        authority.
    :ivar tariff_zone: Fare zone in area.
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
    fare_authority_text: Optional[str] = field(
        default=None,
        metadata={
            "name": "FareAuthorityText",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        }
    )
    tariff_zone: List[TariffZoneStructure] = field(
        default_factory=list,
        metadata={
            "name": "TariffZone",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "min_occurs": 1,
        }
    )
