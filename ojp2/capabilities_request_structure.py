from dataclasses import dataclass, field

from ojp2.request_structure import RequestStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class CapabilitiesRequestStructure(RequestStructure):
    """
    Type for Requests for capabilities of the current system.
    """

    version: str = field(
        default="2.1",
        metadata={
            "type": "Attribute",
        },
    )
