from dataclasses import dataclass, field
from typing import List
from nova.traeger_medium_typ import TraegerMediumTyp

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten"


@dataclass
class TraegerMediumTypen:
    traeger_medium_typ: List[TraegerMediumTyp] = field(
        default_factory=list,
        metadata={
            "name": "traegerMediumTyp",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
        }
    )
