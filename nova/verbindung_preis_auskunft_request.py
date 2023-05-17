from dataclasses import dataclass, field
from typing import List
from nova.preis_auskunft_request import PreisAuskunftRequest
from nova.verbindung_preis_auskunft import VerbindungPreisAuskunft

__NAMESPACE__ = "http://nova.voev.ch/services/v14/preisauskunft"


@dataclass
class VerbindungPreisAuskunftRequest(PreisAuskunftRequest):
    verbindung: List[VerbindungPreisAuskunft] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/preisauskunft",
            "min_occurs": 1,
        }
    )
