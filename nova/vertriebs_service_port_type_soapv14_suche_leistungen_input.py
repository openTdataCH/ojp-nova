from dataclasses import dataclass, field
from typing import Optional
from nova.suche_leistungen import SucheLeistungen

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class VertriebsServicePortTypeSoapv14SucheLeistungenInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["VertriebsServicePortTypeSoapv14SucheLeistungenInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        suche_leistungen: Optional[SucheLeistungen] = field(
            default=None,
            metadata={
                "name": "sucheLeistungen",
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            }
        )
