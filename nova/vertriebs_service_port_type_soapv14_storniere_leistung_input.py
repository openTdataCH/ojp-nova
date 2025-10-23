from dataclasses import dataclass, field
from typing import Optional
from nova.storniere_leistung import StorniereLeistung

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class VertriebsServicePortTypeSoapv14StorniereLeistungInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["VertriebsServicePortTypeSoapv14StorniereLeistungInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        storniere_leistung: Optional[StorniereLeistung] = field(
            default=None,
            metadata={
                "name": "storniereLeistung",
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            }
        )
