from dataclasses import dataclass, field
from typing import List
from nova.ermaessigungs_karte import ErmaessigungsKarte

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten"


@dataclass
class ErmaessigungsKarten:
    ermaessigungs_karte: List[ErmaessigungsKarte] = field(
        default_factory=list,
        metadata={
            "name": "ermaessigungsKarte",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
        }
    )
