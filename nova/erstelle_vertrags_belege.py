from dataclasses import dataclass, field
from typing import Optional
from nova.beleg_request import BelegRequest

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class ErstelleVertragsBelege:
    class Meta:
        name = "erstelleVertragsBelege"
        namespace = "http://nova.voev.ch/services/v14/vertrieb"

    vertrags_beleg_request: Optional[BelegRequest] = field(
        default=None,
        metadata={
            "name": "vertragsBelegRequest",
            "type": "Element",
            "required": True,
        }
    )
