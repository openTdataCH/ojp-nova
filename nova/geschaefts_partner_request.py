from dataclasses import dataclass, field
from typing import Optional
from nova.client_identifier import ClientIdentifier
from nova.correlation_kontext import CorrelationKontext

__NAMESPACE__ = "http://nova.voev.ch/services/v14/geschaeftspartner"


@dataclass
class GeschaeftsPartnerRequest:
    client_identifier: Optional[ClientIdentifier] = field(
        default=None,
        metadata={
            "name": "clientIdentifier",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
            "required": True,
        }
    )
    correlation_kontext: Optional[CorrelationKontext] = field(
        default=None,
        metadata={
            "name": "correlationKontext",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
            "required": True,
        }
    )
