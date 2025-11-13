from dataclasses import dataclass, field
from typing import Optional

from ojp2.ojpstatus_response import OjpstatusResponse
from ojp2.producer_response_structure import ProducerResponseStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class CapabilitiesResponseStructure(ProducerResponseStructure):
    """
    Type for the capabilities of an implementation.
    """

    ojpstatus_response: Optional[OjpstatusResponse] = field(
        default=None,
        metadata={
            "name": "OJPStatusResponse",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
