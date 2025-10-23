from dataclasses import dataclass, field
from typing import List
from nova.zonen_buendel import ZonenBuendel

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class ZonenGeltungsBereich:
    zonen_buendel: List[ZonenBuendel] = field(
        default_factory=list,
        metadata={
            "name": "zonenBuendel",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    moegliche_zonen_buendel: List[ZonenBuendel] = field(
        default_factory=list,
        metadata={
            "name": "moeglicheZonenBuendel",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
