from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class ProgressBetweenStopsStructure:
    """
    Type for Progress between stops.

    :ivar link_distance: The total distance in metres between the
        previous stop and the next stop.
    :ivar percentage: Percentage along link that VEHICLE has travelled.
    """
    link_distance: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "LinkDistance",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    percentage: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Percentage",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
