from dataclasses import dataclass, field
from typing import List
from nova.verbund_strecke import VerbundStrecke

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten"


@dataclass
class VerbundStrecken:
    verbund_strecke: List[VerbundStrecke] = field(
        default_factory=list,
        metadata={
            "name": "verbundStrecke",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
        }
    )
