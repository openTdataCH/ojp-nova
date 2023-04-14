from dataclasses import dataclass, field
from typing import List
from nova.abstract_leistung import AbstractLeistung
from nova.vertriebs_response import VertriebsResponse

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class KaufResponse(VertriebsResponse):
    """Die Kaufantwort ist das Antwortsobjekt des 3.

    Klangs. Sie enthält für jede übermittelte LeistungId eine Leistung
    mit dem Status gekauft.
    """
    leistung: List[AbstractLeistung] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
