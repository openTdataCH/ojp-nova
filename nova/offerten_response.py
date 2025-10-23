from dataclasses import dataclass, field
from typing import List
from nova.abstract_leistung import AbstractLeistung
from nova.vertriebs_response import VertriebsResponse

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class OffertenResponse(VertriebsResponse):
    """Die Offertenantwort ist das Antwortobjekt des 2.

    Klangs. Sie enthält für jede übermittelte angebotsId eine offerierte
    Leistung.
    """
    leistung: List[AbstractLeistung] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
