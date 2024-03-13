from dataclasses import dataclass, field
from typing import List, Optional
from nova.klassen_typ_code import KlassenTypCode

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class PlatzVerfuegbarkeit:
    verfuegbare_platz_lage: List[str] = field(
        default_factory=list,
        metadata={
            "name": "verfuegbarePlatzLage",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_length": 0,
            "max_length": 50,
        }
    )
    abteil_art_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "abteilArtCode",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
            "min_length": 0,
            "max_length": 50,
        }
    )
    wagen_art_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "wagenArtCode",
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
