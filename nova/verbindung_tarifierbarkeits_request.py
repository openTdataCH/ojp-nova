from dataclasses import dataclass, field
from typing import Optional
from nova.fahrplan_verbindung import FahrplanVerbindung
from nova.vertriebs_request import VertriebsRequest

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class VerbindungTarifierbarkeitsRequest(VertriebsRequest):
    verbindung: Optional[FahrplanVerbindung] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
