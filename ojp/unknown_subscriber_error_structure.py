from dataclasses import dataclass, field
from typing import Optional
from ojp.error_code_structure import ErrorCodeStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class UnknownSubscriberErrorStructure(ErrorCodeStructure):
    """
    Type for Error: Subscriber not found.

    :ivar subscriber_ref: Id of subscriber that was not found + SIRI
        v2.0
    """
    subscriber_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubscriberRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
