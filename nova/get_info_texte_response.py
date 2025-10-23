from dataclasses import dataclass, field
from typing import Optional
from nova.info_texte_response import InfoTexteResponse

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten"


@dataclass
class GetInfoTexteResponse:
    class Meta:
        name = "getInfoTexteResponse"
        namespace = "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten"

    info_texte_response: Optional[InfoTexteResponse] = field(
        default=None,
        metadata={
            "name": "infoTexteResponse",
            "type": "Element",
            "required": True,
        }
    )
