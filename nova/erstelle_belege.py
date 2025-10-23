from dataclasses import dataclass, field
from typing import Optional
from nova.beleg_request import BelegRequest

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class ErstelleBelege:
    """Request-Element für den 4.

    Klang
    """
    class Meta:
        name = "erstelleBelege"
        namespace = "http://nova.voev.ch/services/v14/vertrieb"

    beleg_request: Optional[BelegRequest] = field(
        default=None,
        metadata={
            "name": "belegRequest",
            "type": "Element",
            "required": True,
        }
    )
