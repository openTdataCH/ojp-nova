from dataclasses import dataclass, field
from typing import List
from nova.klassen_typ import KlassenTyp

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten"


@dataclass
class KlassenTypen:
    klassen_typ: List[KlassenTyp] = field(
        default_factory=list,
        metadata={
            "name": "klassenTyp",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
        }
    )
