from dataclasses import dataclass, field
from typing import Optional
from nova.kaufe_angebote import KaufeAngebote

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class VertriebsServicePortTypeSoapv14KaufeAngeboteInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["VertriebsServicePortTypeSoapv14KaufeAngeboteInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        kaufe_angebote: Optional[KaufeAngebote] = field(
            default=None,
            metadata={
                "name": "kaufeAngebote",
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            }
        )
