from dataclasses import dataclass

from ojp2.check_status_request_structure import CheckStatusRequestStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class CheckStatusRequest(CheckStatusRequestStructure):
    """Request from Consumer to Producer to check whether services is working.

    Answers a CheckStatusRequest.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
