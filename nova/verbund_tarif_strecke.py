from dataclasses import dataclass, field
from typing import Optional
from nova.befahrungs_typ import BefahrungsTyp
from nova.verbund_strecken_typ import VerbundStreckenTyp

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class VerbundTarifStrecke:
    strecken_owner: Optional[int] = field(
        default=None,
        metadata={
            "name": "streckenOwner",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
            "max_inclusive": 99999,
        }
    )
    strecken_typ: Optional[VerbundStreckenTyp] = field(
        default=None,
        metadata={
            "name": "streckenTyp",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    befahrungs_typ: Optional[BefahrungsTyp] = field(
        default=None,
        metadata={
            "name": "befahrungsTyp",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    abgang: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
            "min_inclusive": 0,
        }
    )
