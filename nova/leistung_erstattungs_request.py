from dataclasses import dataclass, field
from typing import Optional
from nova.teil_erstattung import TeilErstattung

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class LeistungErstattungsRequest:
    teil_erstattung: Optional[TeilErstattung] = field(
        default=None,
        metadata={
            "name": "teilErstattung",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    leistungs_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "leistungsId",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
            "min_inclusive": 0,
        }
    )
    erstattungs_grund: Optional[str] = field(
        default=None,
        metadata={
            "name": "erstattungsGrund",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_length": 0,
            "max_length": 50,
        }
    )
