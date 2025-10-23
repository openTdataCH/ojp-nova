from dataclasses import dataclass, field
from typing import List
from nova.produkt_info import ProduktInfo

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten"


@dataclass
class StammdatenProduktInfos:
    produkt_info: List[ProduktInfo] = field(
        default_factory=list,
        metadata={
            "name": "produktInfo",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
        }
    )
