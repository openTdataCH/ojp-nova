from dataclasses import dataclass, field
from typing import Optional
from nova.bestaetige_produktion import BestaetigeProduktion

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class VertriebsServicePortTypeSoapv14BestaetigeProduktionInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["VertriebsServicePortTypeSoapv14BestaetigeProduktionInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        bestaetige_produktion: Optional[BestaetigeProduktion] = field(
            default=None,
            metadata={
                "name": "bestaetigeProduktion",
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            }
        )
