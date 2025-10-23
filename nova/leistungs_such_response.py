from dataclasses import dataclass, field
from typing import List, Optional
from nova.leistungs_such_ergebnis import LeistungsSuchErgebnis
from nova.vertriebs_response import VertriebsResponse

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class LeistungsSuchResponse(VertriebsResponse):
    """
    Die LeistungsSuchantwort liefert eine Auflistung von Leistungen.
    """
    leistungs_such_ergebnis: List[LeistungsSuchErgebnis] = field(
        default_factory=list,
        metadata={
            "name": "leistungsSuchErgebnis",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    ist_teil_ergebnis: Optional[bool] = field(
        default=None,
        metadata={
            "name": "istTeilErgebnis",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
