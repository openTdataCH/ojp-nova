from dataclasses import dataclass, field
from typing import Any, Optional

from ojp2.abstract_service_journey_interchange_structure import (
    AbstractServiceJourneyInterchangeStructure,
)
from ojp2.distributor_departure_stop_ref import DistributorDepartureStopRef
from ojp2.distributor_ref import DistributorRef
from ojp2.feeder_arrival_stop_ref import FeederArrivalStopRef
from ojp2.feeder_ref import FeederRef

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class ServiceJourneyInterchangeStructure(
    AbstractServiceJourneyInterchangeStructure
):
    """A planned SERVICE JOURNEY INTERCHANGE between two journeys.

    (since SIRI 2.0)
    """

    interchange_ref: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    reason_for_removal: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    feeder_ref: Optional[FeederRef] = field(
        default=None,
        metadata={
            "name": "FeederRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    feeder_arrival_stop_ref: Optional[FeederArrivalStopRef] = field(
        default=None,
        metadata={
            "name": "FeederArrivalStopRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    distributor_ref: Optional[DistributorRef] = field(
        default=None,
        metadata={
            "name": "DistributorRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    distributor_departure_stop_ref: Optional[DistributorDepartureStopRef] = (
        field(
            default=None,
            metadata={
                "name": "DistributorDepartureStopRef",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "required": True,
            },
        )
    )
