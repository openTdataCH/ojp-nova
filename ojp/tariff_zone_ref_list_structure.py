from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class TariffZoneRefListStructure:
    """
    List of fare zones references within the area of a Fare Authority.
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
    tariff_zone_ref: List[str] = field(
        default_factory=list,
        metadata={
            "name": "TariffZoneRef",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "min_occurs": 1,
        }
    )
