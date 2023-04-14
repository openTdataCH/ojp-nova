from dataclasses import dataclass
from ojp.status_response_structure import StatusResponseStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class ResponseStatus(StatusResponseStructure):
    """Contains infromation about the processing of a an individual service subscription - either success info or an error condition. (VDV Acknowledgement)."""
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
