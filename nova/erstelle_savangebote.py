from dataclasses import dataclass, field
from typing import Optional
from nova.savangebots_request import SavangebotsRequest

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class ErstelleSavangebote:
    """Request-Element für den 1.

    Klang (SAV)
    """
    class Meta:
        name = "erstelleSAVAngebote"
        namespace = "http://nova.voev.ch/services/v14/vertrieb"

    sav_request: Optional[SavangebotsRequest] = field(
        default=None,
        metadata={
            "name": "savRequest",
            "type": "Element",
            "required": True,
        }
    )
