from dataclasses import dataclass, field
from typing import Optional
from nova.leistung_sperren import LeistungSperren

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class VertriebsServicePortTypeSoapv14LeistungSperrenInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["VertriebsServicePortTypeSoapv14LeistungSperrenInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        leistung_sperren: Optional[LeistungSperren] = field(
            default=None,
            metadata={
                "name": "leistungSperren",
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            }
        )
