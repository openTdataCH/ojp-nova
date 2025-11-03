from dataclasses import dataclass, field
from typing import Optional

from ojp2.tariff_zone_list_in_area_structure import (
    TariffZoneListInAreaStructure,
)

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class TariffzoneFilterStructure:
    """
    :ivar exclude: Whether to include or exclude given tariff zones in
        the list from the search. Default is to include.
    :ivar tariff_zones: List of fare zones to include or exclude.
    """

    exclude: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Exclude",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    tariff_zones: Optional[TariffZoneListInAreaStructure] = field(
        default=None,
        metadata={
            "name": "TariffZones",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        },
    )
