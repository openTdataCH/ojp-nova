from dataclasses import dataclass, field
from typing import Optional
from ojp.consumer_response_endpoint_structure import ConsumerResponseEndpointStructure
from ojp.other_error import OtherError
from ojp.unknown_subscription_error import UnknownSubscriptionError

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class DataReadyResponseStructure(ConsumerResponseEndpointStructure):
    """
    Type for Data ready Acknowledgement Response.

    :ivar status:
    :ivar error_condition: Description of any error or warning condition
        as to why Consumer cannot fetch data.
    """
    status: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    error_condition: Optional["DataReadyResponseStructure.ErrorCondition"] = field(
        default=None,
        metadata={
            "name": "ErrorCondition",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )

    @dataclass
    class ErrorCondition:
        """
        :ivar unknown_subscription_error:
        :ivar other_error:
        :ivar description: Text description of error.
        """
        unknown_subscription_error: Optional[UnknownSubscriptionError] = field(
            default=None,
            metadata={
                "name": "UnknownSubscriptionError",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            }
        )
        other_error: Optional[OtherError] = field(
            default=None,
            metadata={
                "name": "OtherError",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            }
        )
        description: Optional[str] = field(
            default=None,
            metadata={
                "name": "Description",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            }
        )
