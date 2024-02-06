from dataclasses import dataclass, field
from typing import List
from nova.reisenden_typ import ReisendenTyp

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten"


@dataclass
class ReisendenTypen:
    reisenden_typ: List[ReisendenTyp] = field(
        default_factory=list,
        metadata={
            "name": "reisendenTyp",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
        }
    )
