from dataclasses import dataclass, field
from typing import Optional
from nova.vertriebs_request import VertriebsRequest

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class LeistungsStatusRequest(VertriebsRequest):
    """
    Über die Subklasse LeistungsstatusAnfrage wird die Anfrage für alle
    möglichen LeistungsStatus definiert.
    """
    leistungs_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "leistungsId",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
            "min_inclusive": 0,
        }
    )
