from dataclasses import dataclass, field
from typing import Optional
from nova.abstract_leistung import AbstractLeistung
from nova.erstattungs_daten import ErstattungsDaten

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class ZuErstattendeLeistung:
    original_leistung: Optional[AbstractLeistung] = field(
        default=None,
        metadata={
            "name": "originalLeistung",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    erstattungs_daten: Optional[ErstattungsDaten] = field(
        default=None,
        metadata={
            "name": "erstattungsDaten",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
