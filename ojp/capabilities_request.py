from dataclasses import dataclass
from ojp.capabilities_request_structure import CapabilitiesRequestStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class CapabilitiesRequest(CapabilitiesRequestStructure):
    """Requests a the current capabilities of the server.

    Answred with a CpabailitiesResponse.
    """
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
