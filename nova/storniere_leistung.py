from dataclasses import dataclass, field
from typing import Optional
from nova.stornierungs_request import StornierungsRequest

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class StorniereLeistung:
    class Meta:
        name = "storniereLeistung"
        namespace = "http://nova.voev.ch/services/v14/vertrieb"

    stornierungs_request: Optional[StornierungsRequest] = field(
        default=None,
        metadata={
            "name": "stornierungsRequest",
            "type": "Element",
            "required": True,
        }
    )
