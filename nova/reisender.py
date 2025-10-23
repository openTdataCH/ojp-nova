from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class Reisender:
    """
    Repräsentiert in einer Angebotsantwort einen Reisenden.
    """
    meldungen_refs: List[str] = field(
        default_factory=list,
        metadata={
            "name": "meldungenRefs",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "tokens": True,
        }
    )
    reisenden_beziehung: List[str] = field(
        default_factory=list,
        metadata={
            "name": "reisendenBeziehung",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_length": 0,
            "max_length": 50,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    externe_reisenden_referenz_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "externeReisendenReferenzId",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_length": 0,
            "max_length": 50,
        }
    )
