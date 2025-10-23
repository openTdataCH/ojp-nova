from dataclasses import dataclass, field
from typing import List, Optional
from nova.transaktions_verhalten import TransaktionsVerhalten
from nova.vertriebs_request import VertriebsRequest

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class BestaetigeProduktionRequest(VertriebsRequest):
    """
    Diese Klasse dient als Container für alle zu bestätigenden Leistungen.
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
    transaktions_verhalten: Optional[TransaktionsVerhalten] = field(
        default=None,
        metadata={
            "name": "transaktionsVerhalten",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
