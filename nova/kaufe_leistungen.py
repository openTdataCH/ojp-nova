from dataclasses import dataclass, field
from typing import Optional
from nova.kauf_request import KaufRequest

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class KaufeLeistungen:
    """Request-Element für den 3.

    Klang
    """
    class Meta:
        name = "kaufeLeistungen"
        namespace = "http://nova.voev.ch/services/v14/vertrieb"

    kauf_request: Optional[KaufRequest] = field(
        default=None,
        metadata={
            "name": "kaufRequest",
            "type": "Element",
            "required": True,
        }
    )
