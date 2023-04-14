from dataclasses import dataclass
from ojp.capabilities_response_structure import CapabilitiesResponseStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class CapabilitiesResponse(CapabilitiesResponseStructure):
    """
    Responses with the capabilities of an implementation.
    """
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
