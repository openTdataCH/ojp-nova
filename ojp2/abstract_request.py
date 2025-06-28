from dataclasses import dataclass

from ojp2.abstract_request_structure import AbstractRequestStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class AbstractRequest(AbstractRequestStructure):
    """
    Subsititutable type for a timestamped SIRI request.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
