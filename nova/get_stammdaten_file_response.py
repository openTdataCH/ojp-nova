from dataclasses import dataclass, field
from typing import Optional
from nova.stammdaten_file_response import StammdatenFileResponse

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten"


@dataclass
class GetStammdatenFileResponse:
    class Meta:
        name = "getStammdatenFileResponse"
        namespace = "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten"

    stammdaten_file_response: Optional[StammdatenFileResponse] = field(
        default=None,
        metadata={
            "name": "stammdatenFileResponse",
            "type": "Element",
            "required": True,
        }
    )
