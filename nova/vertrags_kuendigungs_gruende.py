from dataclasses import dataclass, field
from typing import List
from nova.vertrag_kuendigungs_grund import VertragKuendigungsGrund

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten"


@dataclass
class VertragsKuendigungsGruende:
    vertrag_kuendigungs_grund: List[VertragKuendigungsGrund] = field(
        default_factory=list,
        metadata={
            "name": "vertragKuendigungsGrund",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
        }
    )
