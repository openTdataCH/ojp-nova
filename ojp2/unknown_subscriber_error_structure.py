from dataclasses import dataclass, field
from typing import Optional

from ojp2.error_code_structure import ErrorCodeStructure
from ojp2.participant_ref_structure import ParticipantRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class UnknownSubscriberErrorStructure(ErrorCodeStructure):
    """Type for Error: Subscriber not found.

    :ivar subscriber_ref: Id of capabiliuty that is noit supported. +
        SIRI v2.0
    """

    subscriber_ref: Optional[ParticipantRefStructure] = field(
        default=None,
        metadata={
            "name": "SubscriberRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
