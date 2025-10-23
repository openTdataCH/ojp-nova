from dataclasses import dataclass, field
from typing import List, Optional
from nova.haltestelle import Haltestelle

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten"


@dataclass
class LokalNetz:
    haltestelle: List[Haltestelle] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
        }
    )
    bezeichnung: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "required": True,
            "min_length": 0,
            "max_length": 50,
        }
    )
    code: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "required": True,
            "min_length": 0,
            "max_length": 50,
        }
    )
