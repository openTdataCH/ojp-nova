from dataclasses import dataclass, field
from typing import Optional
from nova.erstelle_angebote import ErstelleAngebote

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class VertriebsServicePortTypeSoapv14ErstelleAngeboteInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["VertriebsServicePortTypeSoapv14ErstelleAngeboteInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        erstelle_angebote: Optional[ErstelleAngebote] = field(
            default=None,
            metadata={
                "name": "erstelleAngebote",
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            }
        )
