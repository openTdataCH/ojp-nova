from dataclasses import dataclass, field
from typing import List
from nova.fahr_art_typ import FahrArtTyp

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten"


@dataclass
class FahrArtTypen:
    fahr_art_typ: List[FahrArtTyp] = field(
        default_factory=list,
        metadata={
            "name": "fahrArtTyp",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
        }
    )
