from dataclasses import dataclass, field
from typing import Optional
from nova.erstelle_freizeit_belege import ErstelleFreizeitBelege

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class VertriebsServicePortTypeSoapv14ErstelleFreizeitBelegeInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["VertriebsServicePortTypeSoapv14ErstelleFreizeitBelegeInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        erstelle_freizeit_belege: Optional[ErstelleFreizeitBelege] = field(
            default=None,
            metadata={
                "name": "erstelleFreizeitBelege",
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            }
        )
