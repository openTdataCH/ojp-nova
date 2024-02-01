from dataclasses import dataclass, field
from typing import Optional
from nova.erstelle_tarif_weg_kombinations_angebot import ErstelleTarifWegKombinationsAngebot

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class VertriebsServicePortTypeSoapv14ErstelleTarifWegKombinationsAngebotInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["VertriebsServicePortTypeSoapv14ErstelleTarifWegKombinationsAngebotInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        erstelle_tarif_weg_kombinations_angebot: Optional[ErstelleTarifWegKombinationsAngebot] = field(
            default=None,
            metadata={
                "name": "erstelleTarifWegKombinationsAngebot",
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            }
        )
