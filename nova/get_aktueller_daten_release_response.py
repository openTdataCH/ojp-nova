from dataclasses import dataclass, field
from typing import Optional
from nova.aktueller_daten_release_response import AktuellerDatenReleaseResponse

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten"


@dataclass
class GetAktuellerDatenReleaseResponse:
    class Meta:
        name = "getAktuellerDatenReleaseResponse"
        namespace = "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten"

    aktueller_daten_release_response: Optional[AktuellerDatenReleaseResponse] = field(
        default=None,
        metadata={
            "name": "aktuellerDatenReleaseResponse",
            "type": "Element",
            "required": True,
        }
    )
