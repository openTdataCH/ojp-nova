from dataclasses import dataclass, field
from typing import Optional
from nova.adresse_request import AdresseRequest

__NAMESPACE__ = "http://nova.voev.ch/services/v14/geschaeftspartner"


@dataclass
class SitzRequest:
    adresse: Optional[AdresseRequest] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
            "required": True,
        }
    )
    ist_temporaer: Optional[bool] = field(
        default=None,
        metadata={
            "name": "istTemporaer",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
            "nillable": True,
        }
    )
