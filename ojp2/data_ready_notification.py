from dataclasses import dataclass

from ojp2.data_ready_request_structure import DataReadyRequestStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class DataReadyNotification(DataReadyRequestStructure):
    """Request from Producer to Consumer to notify that data update is ready to
    fetch.

    Answered with a DataReadyResponse.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
