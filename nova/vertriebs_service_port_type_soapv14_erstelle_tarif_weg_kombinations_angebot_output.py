from dataclasses import dataclass, field
from typing import Optional
from nova.erstelle_tarif_weg_kombinations_angebot_response import ErstelleTarifWegKombinationsAngebotResponse

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class VertriebsServicePortTypeSoapv14ErstelleTarifWegKombinationsAngebotOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["VertriebsServicePortTypeSoapv14ErstelleTarifWegKombinationsAngebotOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        erstelle_tarif_weg_kombinations_angebot_response: Optional[ErstelleTarifWegKombinationsAngebotResponse] = field(
            default=None,
            metadata={
                "name": "erstelleTarifWegKombinationsAngebotResponse",
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            }
        )
        fault: Optional["VertriebsServicePortTypeSoapv14ErstelleTarifWegKombinationsAngebotOutput.Body.Fault"] = field(
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
