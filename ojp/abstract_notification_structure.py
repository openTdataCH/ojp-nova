from dataclasses import dataclass
from ojp.producer_request_endpoint_structure import ProducerRequestEndpointStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class AbstractNotificationStructure(ProducerRequestEndpointStructure):
    """
    Type for Notification Request.
    """
