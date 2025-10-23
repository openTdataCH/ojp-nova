from dataclasses import dataclass, field
from typing import Optional
from nova.adresse import Adresse

__NAMESPACE__ = "http://nova.voev.ch/services/v14/geschaeftspartner"


@dataclass
class Sitz:
    adresse: Optional[Adresse] = field(
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
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
        }
    )
    version_sitz: Optional[int] = field(
        default=None,
        metadata={
            "name": "versionSitz",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
            "required": True,
        }
    )
