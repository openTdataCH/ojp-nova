from dataclasses import dataclass, field
from typing import Optional
from nova.erstelle_savangebote import ErstelleSavangebote

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class VertriebsServicePortTypeSoapv14ErstelleSavangeboteInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["VertriebsServicePortTypeSoapv14ErstelleSavangeboteInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        erstelle_savangebote: Optional[ErstelleSavangebote] = field(
            default=None,
            metadata={
                "name": "erstelleSAVAngebote",
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            }
        )
