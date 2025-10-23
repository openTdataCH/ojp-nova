from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlTime

__NAMESPACE__ = "http://nova.voev.ch/services/v14/base"


@dataclass
class UhrzeitAbschnitt:
    von: Optional[XmlTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/base",
        }
    )
    bis: Optional[XmlTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/base",
        }
    )
