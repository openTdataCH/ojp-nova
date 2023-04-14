from dataclasses import dataclass, field
from typing import Optional
from nova.erstelle_preis_auskunft import ErstellePreisAuskunft

__NAMESPACE__ = "http://nova.voev.ch/services/v14/preisauskunft"


@dataclass
class PreisAuskunftServicePortTypeSoapv14ErstellePreisAuskunftInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["PreisAuskunftServicePortTypeSoapv14ErstellePreisAuskunftInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        erstelle_preis_auskunft: Optional[ErstellePreisAuskunft] = field(
            default=None,
            metadata={
                "name": "erstellePreisAuskunft",
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/preisauskunft",
            }
        )
