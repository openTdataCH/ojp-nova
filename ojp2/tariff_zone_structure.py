from dataclasses import dataclass, field
from typing import Optional

from ojp2.tariff_zone_ref import TariffZoneRef

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class TariffZoneStructure:
    """
    [a more clearly defined equivalent of TARIFF ZONE in TM and NeTEx] A ZONE used
    to define a zonal fare structure in a zone-counting or zone-matrix system.

    :ivar tariff_zone_ref:
    :ivar tariff_zone_text: Text describing the fare zone. Passengers
        will recognize the fare zone by this text. Often published on
        Fare Zone Maps.
    """

    tariff_zone_ref: Optional[TariffZoneRef] = field(
        default=None,
        metadata={
            "name": "TariffZoneRef",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        },
    )
    tariff_zone_text: Optional[str] = field(
        default=None,
        metadata={
            "name": "TariffZoneText",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        },
    )
