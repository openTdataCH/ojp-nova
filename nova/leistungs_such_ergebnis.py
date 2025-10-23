from dataclasses import dataclass, field
from typing import List, Optional
from nova.abstract_leistung import AbstractLeistung
from nova.kontroll_status import KontrollStatus

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class LeistungsSuchErgebnis:
    """
    :ivar leistung:
    :ivar kontroll_status: Nur gefüllt, wenn in der Suche explizit
        angefragt.
    :ivar lv_notiz: Optionale Notiz zu einer Leistung. Kann durch
        Support (z.B. Leitstelle, Vertrieb) gesetzt werden.
    """
    leistung: Optional[AbstractLeistung] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    kontroll_status: List[KontrollStatus] = field(
        default_factory=list,
        metadata={
            "name": "kontrollStatus",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    lv_notiz: Optional[str] = field(
        default=None,
        metadata={
            "name": "lvNotiz",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_length": 0,
            "max_length": 4000,
        }
    )
