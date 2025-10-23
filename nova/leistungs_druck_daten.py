from dataclasses import dataclass, field
from typing import List, Optional
from nova.abstract_leistung import AbstractLeistung
from nova.druck_beleg import DruckBeleg

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class LeistungsDruckDaten:
    leistung: Optional[AbstractLeistung] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    beleg: List[DruckBeleg] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
