from dataclasses import dataclass, field
from typing import Optional
from nova.sperr_typ import SperrTyp
from nova.vertriebs_request import VertriebsRequest

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class LeistungEntsperrenRequest(VertriebsRequest):
    """
    Request-Element zum Entsperren einer Leistung.

    :ivar leistungs_id: ID der Leistung, welche entsperrt werden soll
    :ivar sperr_typ: Gibt an, ob die Leistung für Nutzung oder für
        Erstattung entsperrt werden soll
    :ivar begruendung: Begründung für die Entsperrung
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
    sperr_typ: Optional[SperrTyp] = field(
        default=None,
        metadata={
            "name": "sperrTyp",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    begruendung: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_length": 0,
            "max_length": 4000,
        }
    )
