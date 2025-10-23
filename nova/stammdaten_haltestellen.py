from dataclasses import dataclass, field
from typing import List
from nova.haltestellen import Haltestellen

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten"


@dataclass
class StammdatenHaltestellen:
    haltestellen: List[Haltestellen] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
        }
    )
