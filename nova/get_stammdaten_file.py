from dataclasses import dataclass, field
from typing import Optional
from nova.vertriebs_stammdaten_request import VertriebsStammdatenRequest

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten"


@dataclass
class GetStammdatenFile:
    class Meta:
        name = "getStammdatenFile"
        namespace = "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten"

    stammdaten_file_request: Optional[VertriebsStammdatenRequest] = field(
        default=None,
        metadata={
            "name": "stammdatenFileRequest",
            "type": "Element",
            "required": True,
        }
    )
