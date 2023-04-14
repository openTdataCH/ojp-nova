from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://nova.voev.ch/services/v14/base"


@dataclass
class SystemInformation:
    plattform_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "plattformVersion",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/base",
            "required": True,
            "min_length": 0,
            "max_length": 50,
        }
    )
