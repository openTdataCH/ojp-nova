from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class PlatzVergabeKriterien:
    gewuenschte_platz_lage: List[str] = field(
        default_factory=list,
        metadata={
            "name": "gewuenschtePlatzLage",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_length": 0,
            "max_length": 50,
        }
    )
    wagen_art: Optional[str] = field(
        default=None,
        metadata={
            "name": "wagenArt",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
            "min_length": 0,
            "max_length": 50,
        }
    )
    abteil_art: Optional[str] = field(
        default=None,
        metadata={
            "name": "abteilArt",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
            "min_length": 0,
            "max_length": 50,
        }
    )
