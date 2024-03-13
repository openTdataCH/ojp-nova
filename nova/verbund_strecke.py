from dataclasses import dataclass, field
from typing import List, Optional
from nova.haltestelle import Haltestelle
from nova.verbund_strecken_typ import VerbundStreckenTyp

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten"


@dataclass
class VerbundStrecke:
    haltestelle: List[Haltestelle] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
        }
    )
    strecken_typ: Optional[VerbundStreckenTyp] = field(
        default=None,
        metadata={
            "name": "streckenTyp",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "required": True,
        }
    )
