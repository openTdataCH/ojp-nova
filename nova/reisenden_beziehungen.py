from dataclasses import dataclass, field
from typing import List
from nova.reisenden_beziehung import ReisendenBeziehung

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten"


@dataclass
class ReisendenBeziehungen:
    reisenden_beziehung: List[ReisendenBeziehung] = field(
        default_factory=list,
        metadata={
            "name": "reisendenBeziehung",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
        }
    )
