from dataclasses import dataclass, field
from typing import Optional
from ojp.capabilities_response import CapabilitiesResponse
from ojp.check_status_response import CheckStatusResponse
from ojp.data_ready_acknowledgement import DataReadyAcknowledgement
from ojp.data_received_acknowledgement import DataReceivedAcknowledgement
from ojp.service_delivery import ServiceDelivery
from ojp.subscription_response import SubscriptionResponse
from ojp.terminate_subscription_response import TerminateSubscriptionResponse

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class OjpresponseStructure:
    """Type for OJP Response - Groups individual functional responses.

    :ivar subscription_response:
    :ivar terminate_subscription_response:
    :ivar data_ready_acknowledgement:
    :ivar service_delivery:
    :ivar data_received_acknowledgement:
    :ivar check_status_response:
    :ivar capabilities_response: Responses with the capabilities of an
        implementation. Answers a CapabilityRequest.
    """
    class Meta:
        name = "OJPResponseStructure"

    subscription_response: Optional[SubscriptionResponse] = field(
        default=None,
        metadata={
            "name": "SubscriptionResponse",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    terminate_subscription_response: Optional[TerminateSubscriptionResponse] = field(
        default=None,
        metadata={
            "name": "TerminateSubscriptionResponse",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    data_ready_acknowledgement: Optional[DataReadyAcknowledgement] = field(
        default=None,
        metadata={
            "name": "DataReadyAcknowledgement",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    service_delivery: Optional[ServiceDelivery] = field(
        default=None,
        metadata={
            "name": "ServiceDelivery",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    data_received_acknowledgement: Optional[DataReceivedAcknowledgement] = field(
        default=None,
        metadata={
            "name": "DataReceivedAcknowledgement",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    check_status_response: Optional[CheckStatusResponse] = field(
        default=None,
        metadata={
            "name": "CheckStatusResponse",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    capabilities_response: Optional[CapabilitiesResponse] = field(
        default=None,
        metadata={
            "name": "CapabilitiesResponse",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
