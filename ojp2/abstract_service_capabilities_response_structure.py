from dataclasses import dataclass, field
from typing import Optional

from ojp2.message_ref_structure import MessageRefStructure
from ojp2.participant_ref_structure import ParticipantRefStructure
from ojp2.response_structure import ResponseStructure
from ojp2.service_delivery_error_condition_structure import (
    ServiceDeliveryErrorConditionStructure,
)
from ojp2.status import Status

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class AbstractServiceCapabilitiesResponseStructure(ResponseStructure):
    """
    Type for capabilities response.

    :ivar request_message_ref: Arbitrary unique reference to the request
        which gave rise to this message.
    :ivar delegator_address: Address of original Consumer, i.e.
        requesting system to which delegating response is to be
        returned. (since SIRI 2.0)
    :ivar delegator_ref: Identifier of delegating system that originated
        message. (since SIRI 2.0)
    :ivar status:
    :ivar siri_org_uk_siri_error_condition: Description of any error or
        warning condition.
    """

    request_message_ref: Optional[MessageRefStructure] = field(
        default=None,
        metadata={
            "name": "RequestMessageRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    delegator_address: Optional[str] = field(
        default=None,
        metadata={
            "name": "DelegatorAddress",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    delegator_ref: Optional[ParticipantRefStructure] = field(
        default=None,
        metadata={
            "name": "DelegatorRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    status: Optional[Status] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    siri_org_uk_siri_error_condition: Optional[
        ServiceDeliveryErrorConditionStructure
    ] = field(
        default=None,
        metadata={
            "name": "ErrorCondition",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
