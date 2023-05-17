from dataclasses import dataclass, field
from typing import List
from nova.meldung import Meldung

__NAMESPACE__ = "http://nova.voev.ch/services/v14/base"


@dataclass
class Meldungen:
    meldung: List[Meldung] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/base",
        }
    )
