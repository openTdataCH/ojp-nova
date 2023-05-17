from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://nova.voev.ch/services/v14/base"


@dataclass
class LocalizedText:
    value_de: Optional[str] = field(
        default=None,
        metadata={
            "name": "valueDe",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/base",
            "required": True,
            "min_length": 0,
            "max_length": 4000,
        }
    )
    value_en: Optional[str] = field(
        default=None,
        metadata={
            "name": "valueEn",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/base",
            "required": True,
            "min_length": 0,
            "max_length": 4000,
        }
    )
    value_fr: Optional[str] = field(
        default=None,
        metadata={
            "name": "valueFr",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/base",
            "required": True,
            "min_length": 0,
            "max_length": 4000,
        }
    )
    value_it: Optional[str] = field(
        default=None,
        metadata={
            "name": "valueIt",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/base",
            "required": True,
            "min_length": 0,
            "max_length": 4000,
        }
    )
