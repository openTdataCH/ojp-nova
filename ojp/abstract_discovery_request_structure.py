from dataclasses import dataclass
from ojp.request_structure import RequestStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class AbstractDiscoveryRequestStructure(RequestStructure):
    """
    Requests for stop reference data for use in service requests.
    """
