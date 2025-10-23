from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDate
from nova.sperr_typ import SperrTyp
from nova.vertriebs_request import VertriebsRequest

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class LeistungSperrenRequest(VertriebsRequest):
    """
    Request-Element zum Sperren einer Leistung.

    :ivar leistungs_id: ID der Leistung, welche gesperrt werden soll
    :ivar gueltig_ab: Zeitpunkt ab wann die Leistung gesperrt werden
        soll
    :ivar gueltig_bis: Zeitpunkt bis wann die Leistung gesperrt werden
        soll. Leer = unbeschränkt
    :ivar begruendung: Begründung für die Sperrung
    :ivar sperr_typ: Gibt an, ob die Leistung für Nutzung oder für
        Erstattung gesperrt werden soll
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
    gueltig_ab: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "gueltigAb",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    gueltig_bis: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "gueltigBis",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
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
    sperr_typ: Optional[SperrTyp] = field(
        default=None,
        metadata={
            "name": "sperrTyp",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
