from dataclasses import dataclass, field
from typing import List, Optional
from nova.haltestelle import Haltestelle

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten"


@dataclass
class Haltestellen:
    """
    :ivar haltestelle:
    :ivar id: id wird durch Stammdatenpaket referenziert.
    """
    haltestelle: List[Haltestelle] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "required": True,
        }
    )
