from dataclasses import dataclass, field
from typing import Optional
from nova.vertriebs_stammdaten_request import VertriebsStammdatenRequest

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten"


@dataclass
class GetInfoTexte:
    class Meta:
        name = "getInfoTexte"
        namespace = "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten"

    info_texte_request: Optional[VertriebsStammdatenRequest] = field(
        default=None,
        metadata={
            "name": "infoTexteRequest",
            "type": "Element",
            "required": True,
        }
    )
