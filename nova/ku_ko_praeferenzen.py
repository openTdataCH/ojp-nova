from dataclasses import dataclass, field
from typing import List
from nova.ku_ko_praeferenz import KuKoPraeferenz

__NAMESPACE__ = "http://nova.voev.ch/services/v14/geschaeftspartner"


@dataclass
class KuKoPraeferenzen:
    kuko_praeferenz: List[KuKoPraeferenz] = field(
        default_factory=list,
        metadata={
            "name": "kukoPraeferenz",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
            "min_occurs": 1,
        }
    )
