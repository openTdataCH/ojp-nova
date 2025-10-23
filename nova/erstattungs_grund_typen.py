from dataclasses import dataclass, field
from typing import List
from nova.erstattungs_grund_typ import ErstattungsGrundTyp

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten"


@dataclass
class ErstattungsGrundTypen:
    erstattungs_grund_typ: List[ErstattungsGrundTyp] = field(
        default_factory=list,
        metadata={
            "name": "erstattungsGrundTyp",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
        }
    )
