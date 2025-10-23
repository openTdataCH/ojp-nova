from dataclasses import dataclass, field
from typing import List, Optional
from nova.kontroll_element_parameter import KontrollElementParameter
from nova.transaktions_verhalten import TransaktionsVerhalten
from nova.vertriebs_request import VertriebsRequest

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class BelegRequest(VertriebsRequest):
    """
    Das Objekt Beleganfrage dient als Container für alle Informationen, die
    notwendig sind, um für die übermittelte leistungsId eine Belegantwort zu
    liefern.
    """
    leistungs_id: List[int] = field(
        default_factory=list,
        metadata={
            "name": "leistungsId",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_occurs": 1,
            "min_inclusive": 0,
        }
    )
    kontroll_element_parameter: Optional[KontrollElementParameter] = field(
        default=None,
        metadata={
            "name": "kontrollElementParameter",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
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
