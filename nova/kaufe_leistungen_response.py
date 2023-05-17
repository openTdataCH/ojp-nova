from dataclasses import dataclass, field
from typing import Optional
from nova.kauf_response import KaufResponse

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class KaufeLeistungenResponse:
    """Response-Element für den 3.

    Klang
    """
    class Meta:
        name = "kaufeLeistungenResponse"
        namespace = "http://nova.voev.ch/services/v14/vertrieb"

    kauf_response: Optional[KaufResponse] = field(
        default=None,
        metadata={
            "name": "kaufResponse",
            "type": "Element",
            "required": True,
        }
    )
