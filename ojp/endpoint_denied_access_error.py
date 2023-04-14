from dataclasses import dataclass
from ojp.endpoint_denied_access_structure import EndpointDeniedAccessStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class EndpointDeniedAccessError(EndpointDeniedAccessStructure):
    """Error:Endpoint to which a message is to be distributed did not allow
    access by the cloient.

    +SIRI v2.0
    """
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
