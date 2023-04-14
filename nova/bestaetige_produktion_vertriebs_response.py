from dataclasses import dataclass, field
from typing import List
from nova.abstract_leistung import AbstractLeistung
from nova.vertriebs_response import VertriebsResponse

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class BestaetigeProduktionVertriebsResponse(VertriebsResponse):
    """
    Diese Klasse dient als Container für alle Leistungen, deren Produktion
    bestätigt worden ist.
    """
    leistung: List[AbstractLeistung] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
