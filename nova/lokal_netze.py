from dataclasses import dataclass, field
from typing import List
from nova.lokal_netz import LokalNetz

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten"


@dataclass
class LokalNetze:
    lokal_netz: List[LokalNetz] = field(
        default_factory=list,
        metadata={
            "name": "lokalNetz",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
        }
    )
