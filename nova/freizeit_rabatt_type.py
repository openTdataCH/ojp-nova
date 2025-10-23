from dataclasses import dataclass, field
from typing import List
from nova.abstract_rabatt_type import AbstractRabattType
from nova.produkt_rabatt_type import ProduktRabattType

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class FreizeitRabattType(AbstractRabattType):
    produkt_rabatt: List[ProduktRabattType] = field(
        default_factory=list,
        metadata={
            "name": "produktRabatt",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_occurs": 1,
        }
    )
