from dataclasses import dataclass, field
from typing import Optional

from ojp2.consumer_request_endpoint_structure import (
    ConsumerRequestEndpointStructure,
)
from ojp2.message_ref_structure import MessageRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class DataSupplyRequestStructure(ConsumerRequestEndpointStructure):
    """
    Type for Data supply Request.

    :ivar notification_ref: Reference to a specific notification message
        for which data is to be fetched. Can be used to distinguish
        between notfcatiosn for the same service and subscriber but for
        different filters.If none specified,
    :ivar all_data: Whether to return all data, or just new updates
        since the last delivery. Default false, i.e. just updates.
    """

    notification_ref: Optional[MessageRefStructure] = field(
        default=None,
        metadata={
            "name": "NotificationRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    all_data: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AllData",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
