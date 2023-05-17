from dataclasses import dataclass, field
from typing import Optional
from nova.system_information import SystemInformation

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class PingResponse:
    class Meta:
        name = "pingResponse"
        namespace = "http://nova.voev.ch/services/v14/vertrieb"

    system_information: Optional[SystemInformation] = field(
        default=None,
        metadata={
            "name": "systemInformation",
            "type": "Element",
            "required": True,
        }
    )
