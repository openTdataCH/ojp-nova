from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class BlockingStructure:
    """
    Type for blocking.

    :ivar journey_planner: Whether information about parts of the
        NETWORK identified by AffectsScope should be blocked from the
        Journey Planner. Default is false; do not suppress.
    :ivar real_time: Whether information about parts of the NETWORK
        identified by AffectsScope should be blocked from real-time
        departure info systems. Default is false; do not suppress.
    """

    journey_planner: Optional[bool] = field(
        default=None,
        metadata={
            "name": "JourneyPlanner",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    real_time: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RealTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
