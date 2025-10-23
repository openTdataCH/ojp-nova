from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class FreizeitBeleg:
    payload: Optional[bytes] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
            "format": "base64",
        }
    )
    mime_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "mimeType",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    freizeit_traeger_medium_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "freizeitTraegerMediumCode",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
            "min_length": 0,
            "max_length": 50,
        }
    )
