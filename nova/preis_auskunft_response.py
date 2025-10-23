from dataclasses import dataclass, field
from typing import List, Optional
from nova.meldungen import Meldungen
from nova.preis_auspraegung import PreisAuspraegung

__NAMESPACE__ = "http://nova.voev.ch/services/v14/preisauskunft"


@dataclass
class PreisAuskunftResponse:
    meldungen: Optional[Meldungen] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/preisauskunft",
            "required": True,
        }
    )
    preis_auspraegung: List[PreisAuspraegung] = field(
        default_factory=list,
        metadata={
            "name": "preisAuspraegung",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/preisauskunft",
        }
    )
