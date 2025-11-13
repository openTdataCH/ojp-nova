from dataclasses import dataclass

from ojp2.endpoint_not_available_access_structure import (
    EndpointNotAvailableAccessStructure,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class EndpointNotAvailableAccessError(EndpointNotAvailableAccessStructure):
    """Error:Recipient of a message to be distributed is not available.

    (since SIRI 2.0)
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
