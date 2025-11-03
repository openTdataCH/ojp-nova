from dataclasses import dataclass

from ojp2.tariff_zone_ref_structure import TariffZoneRefStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class TariffZoneRef(TariffZoneRefStructure):
    """
    Reference to a fare zone.
    """

    class Meta:
        namespace = "http://www.vdv.de/ojp"
