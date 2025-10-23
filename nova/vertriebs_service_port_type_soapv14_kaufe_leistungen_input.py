from dataclasses import dataclass, field
from typing import Optional
from nova.kaufe_leistungen import KaufeLeistungen

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class VertriebsServicePortTypeSoapv14KaufeLeistungenInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["VertriebsServicePortTypeSoapv14KaufeLeistungenInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        kaufe_leistungen: Optional[KaufeLeistungen] = field(
            default=None,
            metadata={
                "name": "kaufeLeistungen",
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            }
        )
