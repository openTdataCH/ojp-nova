from dataclasses import dataclass, field
from typing import Optional
from nova.verkaufs_parameter_wert import VerkaufsParameterWert

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class LeistungVerkaufsParameterType:
    wert: Optional[VerkaufsParameterWert] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    code: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
            "min_length": 0,
            "max_length": 50,
        }
    )
