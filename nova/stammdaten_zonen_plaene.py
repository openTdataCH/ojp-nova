from dataclasses import dataclass, field
from typing import List
from nova.zonen_plaene import ZonenPlaene

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten"


@dataclass
class StammdatenZonenPlaene:
    zonen_plaene: List[ZonenPlaene] = field(
        default_factory=list,
        metadata={
            "name": "zonenPlaene",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
        }
    )
