from dataclasses import dataclass, field
from typing import List
from nova.abstract_rabatt_type import AbstractRabattType

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class RabattAnfrageType:
    rabatt: List[AbstractRabattType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_occurs": 1,
        }
    )
