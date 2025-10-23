from dataclasses import dataclass, field
from typing import Optional
from nova.tarif_weg_kombinations_angebots_request import TarifWegKombinationsAngebotsRequest

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class ErstelleTarifWegKombinationsAngebot:
    class Meta:
        name = "erstelleTarifWegKombinationsAngebot"
        namespace = "http://nova.voev.ch/services/v14/vertrieb"

    angebots_request: Optional[TarifWegKombinationsAngebotsRequest] = field(
        default=None,
        metadata={
            "name": "angebotsRequest",
            "type": "Element",
            "required": True,
        }
    )
