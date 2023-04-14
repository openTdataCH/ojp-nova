from dataclasses import dataclass, field
from typing import List, Optional
from nova.leistungs_request import LeistungsRequest
from nova.transaktions_verhalten import TransaktionsVerhalten
from nova.vertriebs_request import VertriebsRequest

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class OffertenRequest(VertriebsRequest):
    """
    Das Objekt Offertenanfrage dient als Container für mehrere
    Leistungsanfragen.
    """
    leistungs_request: List[LeistungsRequest] = field(
        default_factory=list,
        metadata={
            "name": "leistungsRequest",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_occurs": 1,
        }
    )
    transaktions_verhalten: Optional[TransaktionsVerhalten] = field(
        default=None,
        metadata={
            "name": "transaktionsVerhalten",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
