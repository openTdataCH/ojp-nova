from dataclasses import dataclass, field
from typing import Optional
from nova.info_texte import InfoTexte
from nova.vertriebs_stammdaten_response import VertriebsStammdatenResponse

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten"


@dataclass
class InfoTexteResponse(VertriebsStammdatenResponse):
    info_texte: Optional[InfoTexte] = field(
        default=None,
        metadata={
            "name": "infoTexte",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "required": True,
        }
    )
