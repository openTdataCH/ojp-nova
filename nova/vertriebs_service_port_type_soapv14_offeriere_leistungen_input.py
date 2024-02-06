from dataclasses import dataclass, field
from typing import Optional
from nova.offeriere_leistungen import OfferiereLeistungen

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class VertriebsServicePortTypeSoapv14OfferiereLeistungenInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["VertriebsServicePortTypeSoapv14OfferiereLeistungenInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        offeriere_leistungen: Optional[OfferiereLeistungen] = field(
            default=None,
            metadata={
                "name": "offeriereLeistungen",
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            }
        )
