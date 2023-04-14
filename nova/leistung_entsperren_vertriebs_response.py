from dataclasses import dataclass, field
from typing import Optional
from nova.vertriebs_response import VertriebsResponse

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class LeistungEntsperrenVertriebsResponse(VertriebsResponse):
    """
    Response-Element zum Entsperren einer Leistung.

    :ivar entsperrung_erfolgreich: Gibt an, ob die Entsperrung
        erfolgreich war
    """
    entsperrung_erfolgreich: Optional[bool] = field(
        default=None,
        metadata={
            "name": "entsperrungErfolgreich",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
