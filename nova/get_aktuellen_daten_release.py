from dataclasses import dataclass, field
from typing import Optional
from nova.vertriebs_stammdaten_request import VertriebsStammdatenRequest

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten"


@dataclass
class GetAktuellenDatenRelease:
    class Meta:
        name = "getAktuellenDatenRelease"
        namespace = "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten"

    aktueller_daten_release_request: Optional[VertriebsStammdatenRequest] = field(
        default=None,
        metadata={
            "name": "aktuellerDatenReleaseRequest",
            "type": "Element",
            "required": True,
        }
    )
