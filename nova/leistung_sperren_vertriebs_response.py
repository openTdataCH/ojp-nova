from dataclasses import dataclass, field
from typing import Optional
from nova.vertriebs_response import VertriebsResponse

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class LeistungSperrenVertriebsResponse(VertriebsResponse):
    """
    Response-Element zum Sperren einer Leistung.

    :ivar sperrung_erfolgreich: Gibt an, ob die Sperrung erfolgreich war
    """
    sperrung_erfolgreich: Optional[bool] = field(
        default=None,
        metadata={
            "name": "sperrungErfolgreich",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
