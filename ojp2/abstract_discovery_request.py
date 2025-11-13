from dataclasses import dataclass

from ojp2.abstract_discovery_request_structure import (
    AbstractDiscoveryRequestStructure,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class AbstractDiscoveryRequest(AbstractDiscoveryRequestStructure):
    """
    Abstract Discovery request.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
