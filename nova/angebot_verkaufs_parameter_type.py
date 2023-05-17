from dataclasses import dataclass, field
from typing import Optional
from nova.verkaufs_parameter_typ import VerkaufsParameterTyp
from nova.verkaufs_parameter_wert import VerkaufsParameterWert

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class AngebotVerkaufsParameterType:
    verkaufs_parameter: Optional[VerkaufsParameterTyp] = field(
        default=None,
        metadata={
            "name": "verkaufsParameter",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    vorgabe_wert: Optional[VerkaufsParameterWert] = field(
        default=None,
        metadata={
            "name": "vorgabeWert",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    optional: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
