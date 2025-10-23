from dataclasses import dataclass, field
from typing import List, Optional
from nova.leistungs_kauf_request import LeistungsKaufRequest
from nova.transaktions_verhalten import TransaktionsVerhalten
from nova.vertriebs_request import VertriebsRequest

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class KaufRequest(VertriebsRequest):
    """
    Das Objekt Kaufanfrage dient als Container für mehrere LeistungsKaufanfragen.
    """
    leistungs_kauf_request: List[LeistungsKaufRequest] = field(
        default_factory=list,
        metadata={
            "name": "leistungsKaufRequest",
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
