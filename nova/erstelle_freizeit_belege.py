from dataclasses import dataclass, field
from typing import Optional
from nova.freizeit_beleg_request import FreizeitBelegRequest

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class ErstelleFreizeitBelege:
    class Meta:
        name = "erstelleFreizeitBelege"
        namespace = "http://nova.voev.ch/services/v14/vertrieb"

    freizeit_beleg_request: Optional[FreizeitBelegRequest] = field(
        default=None,
        metadata={
            "name": "freizeitBelegRequest",
            "type": "Element",
            "required": True,
        }
    )
