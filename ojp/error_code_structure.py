from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class ErrorCodeStructure:
    """
    Type for Error Code.

    :ivar error_text: Addtional Description of error. This allows a
        descripotion to be supplied when the Error code is used in a
        specific WSDL fault, rather than within a general error
        condition.
    :ivar number: Error code number associated with error.
    """
    error_text: Optional[str] = field(
        default=None,
        metadata={
            "name": "ErrorText",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    number: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
