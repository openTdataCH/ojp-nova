from dataclasses import dataclass, field
from typing import List
from nova.verkehrs_mittel_typ import VerkehrsMittelTyp

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten"


@dataclass
class VerkehrsMittelTypen:
    verkehrs_mittel_typ: List[VerkehrsMittelTyp] = field(
        default_factory=list,
        metadata={
            "name": "verkehrsMittelTyp",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
        }
    )
