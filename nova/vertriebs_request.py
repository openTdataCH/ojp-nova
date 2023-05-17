from dataclasses import dataclass, field
from typing import Optional
from nova.anfrage_protokoll_level import AnfrageProtokollLevel
from nova.client_identifier import ClientIdentifier
from nova.correlation_kontext import CorrelationKontext
from nova.time_shift import TimeShift

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class VertriebsRequest:
    """
    Abstrakte Basisklasse aller Anfragen, welche der NOVA Vertriebsservice entgegen
    nimmt.
    """
    client_identifier: Optional[ClientIdentifier] = field(
        default=None,
        metadata={
            "name": "clientIdentifier",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    correlation_kontext: Optional[CorrelationKontext] = field(
        default=None,
        metadata={
            "name": "correlationKontext",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    time_shift: Optional[TimeShift] = field(
        default=None,
        metadata={
            "name": "timeShift",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    fachlog_level: Optional[AnfrageProtokollLevel] = field(
        default=None,
        metadata={
            "name": "fachlogLevel",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
