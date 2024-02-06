from dataclasses import dataclass, field
from typing import List
from nova.zonen_tarife import ZonenTarife

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten"


@dataclass
class StammdatenZonenTarife:
    zonen_tarife: List[ZonenTarife] = field(
        default_factory=list,
        metadata={
            "name": "zonenTarife",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
        }
    )
