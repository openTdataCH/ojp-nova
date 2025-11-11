from dataclasses import dataclass

from ojp2.request_structure import RequestStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class AbstractTrackedRequest(RequestStructure):
    """
    Subsititutable type for a SIRI request with requestor dteials tracked.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
