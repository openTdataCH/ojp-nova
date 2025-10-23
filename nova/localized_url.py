from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://nova.voev.ch/services/v14/base"


@dataclass
class LocalizedUrl:
    """
    Bietet sprachspezifische URLs.
    """
    class Meta:
        name = "LocalizedURL"

    default_wert: Optional[str] = field(
        default=None,
        metadata={
            "name": "defaultWert",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/base",
            "max_length": 2048,
        }
    )
    de: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/base",
            "max_length": 2048,
        }
    )
    en: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/base",
            "max_length": 2048,
        }
    )
    fr: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/base",
            "max_length": 2048,
        }
    )
    it: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/base",
            "max_length": 2048,
        }
    )
