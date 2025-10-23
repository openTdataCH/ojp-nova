from dataclasses import dataclass, field
from typing import Optional
from nova.meldungen import Meldungen
from nova.status import Status

__NAMESPACE__ = "http://nova.voev.ch/services/v14/geschaeftspartner"


@dataclass
class GeschaeftsPartnerResponse:
    meldungen: Optional[Meldungen] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
            "required": True,
        }
    )
    status: Optional[Status] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
            "required": True,
        }
    )
