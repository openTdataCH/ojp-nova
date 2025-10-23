from dataclasses import dataclass, field
from typing import List
from nova.geschlecht import Geschlecht

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten"


@dataclass
class Geschlechter:
    geschlecht: List[Geschlecht] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
        }
    )
