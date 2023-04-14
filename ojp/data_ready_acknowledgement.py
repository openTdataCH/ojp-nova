from dataclasses import dataclass
from ojp.data_ready_response_structure import DataReadyResponseStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class DataReadyAcknowledgement(DataReadyResponseStructure):
    """
    Response from Consumer to Producer to acknowledge to Producer that a
    DataReadyRequest has been received.
    """
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
