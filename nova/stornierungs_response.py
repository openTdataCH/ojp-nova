from dataclasses import dataclass, field
from typing import List
from nova.stornierungs_info import StornierungsInfo
from nova.vertriebs_response import VertriebsResponse

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class StornierungsResponse(VertriebsResponse):
    stornierungs_info: List[StornierungsInfo] = field(
        default_factory=list,
        metadata={
            "name": "stornierungsInfo",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
