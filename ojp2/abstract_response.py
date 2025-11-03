from dataclasses import dataclass

from ojp2.response_structure import ResponseStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class AbstractResponse(ResponseStructure):
    """
    Subsititutable type for a SIRI response.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
