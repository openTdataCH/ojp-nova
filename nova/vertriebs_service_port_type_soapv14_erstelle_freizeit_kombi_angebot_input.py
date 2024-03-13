from dataclasses import dataclass, field
from typing import Optional
from nova.erstelle_freizeit_kombi_angebot import ErstelleFreizeitKombiAngebot

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class VertriebsServicePortTypeSoapv14ErstelleFreizeitKombiAngebotInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["VertriebsServicePortTypeSoapv14ErstelleFreizeitKombiAngebotInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        erstelle_freizeit_kombi_angebot: Optional[ErstelleFreizeitKombiAngebot] = field(
            default=None,
            metadata={
                "name": "erstelleFreizeitKombiAngebot",
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            }
        )
