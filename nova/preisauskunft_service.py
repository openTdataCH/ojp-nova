from dataclasses import dataclass, field
from typing import Optional
from nova.nova_preisauskunft import (
    ErstellePreisAuskunft,
    ErstellePreisAuskunftResponse,
)

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


@dataclass
class PreisAuskunftServicePortTypeSoapv14ErstellePreisAuskunftOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["PreisAuskunftServicePortTypeSoapv14ErstellePreisAuskunftOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        erstelle_preis_auskunft_response: Optional[ErstellePreisAuskunftResponse] = field(
            default=None,
            metadata={
                "name": "erstellePreisAuskunftResponse",
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/preisauskunft",
            }
        )
        fault: Optional["PreisAuskunftServicePortTypeSoapv14ErstellePreisAuskunftOutput.Body.Fault"] = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )


class PreisAuskunftServicePortTypeSoapv14ErstellePreisAuskunft:
    style = "document"
    location = "http://nova.voev.ch/novapa/vertrieb/public/v14/PreisAuskunftService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "https://nova.voev.ch/services/v14/preisauskunft/erstellePreisAuskunft"
    input = PreisAuskunftServicePortTypeSoapv14ErstellePreisAuskunftInput
    output = PreisAuskunftServicePortTypeSoapv14ErstellePreisAuskunftOutput
