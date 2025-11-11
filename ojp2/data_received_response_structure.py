from dataclasses import dataclass, field
from typing import Optional

from ojp2.consumer_response_endpoint_structure import (
    ConsumerResponseEndpointStructure,
)
from ojp2.error_description_structure import ErrorDescriptionStructure
from ojp2.ojperror import Ojperror
from ojp2.other_error import OtherError
from ojp2.status import Status
from ojp2.unknown_subscription_error import UnknownSubscriptionError

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class DataReceivedResponseStructure(ConsumerResponseEndpointStructure):
    """
    Type for Data received Acknowledgement Response.

    :ivar status:
    :ivar error_condition: Description of any error or warning
        condition.
    """

    status: Optional[Status] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    error_condition: Optional[
        "DataReceivedResponseStructure.ErrorCondition"
    ] = field(
        default=None,
        metadata={
            "name": "ErrorCondition",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )

    @dataclass
    class ErrorCondition:
        """
        :ivar unknown_subscription_error:
        :ivar ojperror:
        :ivar other_error:
        :ivar description: Text description of error.
        """

        unknown_subscription_error: Optional[UnknownSubscriptionError] = field(
            default=None,
            metadata={
                "name": "UnknownSubscriptionError",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
        ojperror: Optional[Ojperror] = field(
            default=None,
            metadata={
                "name": "OJPError",
                "type": "Element",
                "namespace": "http://www.vdv.de/ojp",
            },
        )
        other_error: Optional[OtherError] = field(
            default=None,
            metadata={
                "name": "OtherError",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
        description: Optional[ErrorDescriptionStructure] = field(
            default=None,
            metadata={
                "name": "Description",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
