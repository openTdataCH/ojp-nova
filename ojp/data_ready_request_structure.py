from dataclasses import dataclass
from ojp.abstract_notification_structure import AbstractNotificationStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class DataReadyRequestStructure(AbstractNotificationStructure):
    """Type for Request from Producer to Consumer to notify that data update is
    ready to fetch.

    Answered with a DataReadyResponse.
    """
