from dataclasses import dataclass, field
from typing import List
from nova.info_text import InfoText

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten"


@dataclass
class InfoTexte:
    info_text: List[InfoText] = field(
        default_factory=list,
        metadata={
            "name": "infoText",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
        }
    )
