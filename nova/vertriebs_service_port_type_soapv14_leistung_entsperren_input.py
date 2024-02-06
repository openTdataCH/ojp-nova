from dataclasses import dataclass, field
from typing import Optional
from nova.leistung_entsperren import LeistungEntsperren

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class VertriebsServicePortTypeSoapv14LeistungEntsperrenInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["VertriebsServicePortTypeSoapv14LeistungEntsperrenInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        leistung_entsperren: Optional[LeistungEntsperren] = field(
            default=None,
            metadata={
                "name": "leistungEntsperren",
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            }
        )
