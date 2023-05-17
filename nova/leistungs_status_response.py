from dataclasses import dataclass, field
from typing import Optional
from nova.leistungs_status import LeistungsStatus
from nova.vertriebs_response import VertriebsResponse

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class LeistungsStatusResponse(VertriebsResponse):
    """
    Die Spezialisierung LeistungsstatusAntwort dient als Container für alle
    ermittelten Leistungsstatus.
    """
    leistungs_status: Optional[LeistungsStatus] = field(
        default=None,
        metadata={
            "name": "leistungsStatus",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
