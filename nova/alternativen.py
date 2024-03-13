from dataclasses import dataclass, field
from typing import List
from nova.partner_1 import Partner1

__NAMESPACE__ = "http://nova.voev.ch/services/v14/geschaeftspartner"


@dataclass
class Alternativen:
    alternative: List[Partner1] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
        }
    )
