from dataclasses import dataclass, field
from typing import List, Optional
from nova.klassen_typ_code import KlassenTypCode

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class Platz:
    platz_lage: List[str] = field(
        default_factory=list,
        metadata={
            "name": "platzLage",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
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
    klasse: Optional[KlassenTypCode] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    platz_nummer: Optional[str] = field(
        default=None,
        metadata={
            "name": "platzNummer",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    wagen_nummer: Optional[str] = field(
        default=None,
        metadata={
            "name": "wagenNummer",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
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
