from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class ZonenBuendelRequest:
    zone: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_length": 0,
            "max_length": 50,
        }
    )
    alle_zonen: Optional[bool] = field(
        default=None,
        metadata={
            "name": "alleZonen",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    tarif_owner: Optional[int] = field(
        default=None,
        metadata={
            "name": "tarifOwner",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
            "max_inclusive": 99999,
        }
    )
