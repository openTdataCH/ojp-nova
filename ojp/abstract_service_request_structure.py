from dataclasses import dataclass, field
from typing import Optional
from ojp.abstract_request_structure import AbstractRequestStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class AbstractServiceRequestStructure(AbstractRequestStructure):
    """
    Abstract Service Request for SIRI Service request.

    :ivar message_identifier: Arbitrary unique reference to this
        message.
    """
    message_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "MessageIdentifier",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
