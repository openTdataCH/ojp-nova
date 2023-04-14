from dataclasses import dataclass, field
from typing import List, Optional
from ojp.tariff_zone_list_in_area_structure import TariffZoneListInAreaStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class StopFareResultStructure:
    """
    Stop-related Fare information.

    :ivar tariff_zone_list_in_area: One or more lists of Fare zones that
        belong to a Fare authority/area.
    :ivar extension:
    """
    tariff_zone_list_in_area: List[TariffZoneListInAreaStructure] = field(
        default_factory=list,
        metadata={
            "name": "TariffZoneListInArea",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "min_occurs": 1,
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
