from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://nova.voev.ch/services/v14/base"


@dataclass
class NameVorname:
    """
    :ivar name:
    :ivar vorname:
    :ivar version_name: will be mandatory in NOVA 15
    """
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/base",
            "required": True,
            "min_length": 0,
            "max_length": 30,
        }
    )
    vorname: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/base",
            "required": True,
            "min_length": 0,
            "max_length": 30,
        }
    )
    version_name: Optional[int] = field(
        default=None,
        metadata={
            "name": "versionName",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/base",
        }
    )
