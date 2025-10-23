from dataclasses import dataclass, field
from typing import Optional
from nova.erstelle_vertrags_belege import ErstelleVertragsBelege

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class VertriebsServicePortTypeSoapv14ErstelleVertragsBelegeInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["VertriebsServicePortTypeSoapv14ErstelleVertragsBelegeInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        erstelle_vertrags_belege: Optional[ErstelleVertragsBelege] = field(
            default=None,
            metadata={
                "name": "erstelleVertragsBelege",
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            }
        )
