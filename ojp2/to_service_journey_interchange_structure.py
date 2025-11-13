from dataclasses import dataclass, field
from typing import Any, Optional

from ojp2.abstract_service_journey_interchange_structure import (
    AbstractServiceJourneyInterchangeStructure,
)
from ojp2.distributor_departure_stop_ref import DistributorDepartureStopRef
from ojp2.distributor_ref import DistributorRef
from ojp2.feeder_arrival_stop_ref import FeederArrivalStopRef
from ojp2.feeder_ref import FeederRef
from ojp2.feeder_visit_number import FeederVisitNumber

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class ToServiceJourneyInterchangeStructure(
    AbstractServiceJourneyInterchangeStructure
):
    """A planned SERVICE JOURNEY INTERCHANGE to a journey.

    (since SIRI 2.0)
    """

    interchange_ref: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    extra_interchange: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    cancellation: Any = field(
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
    feeder_ref: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    feeder_arrival_stop_ref: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    feeder_visit_number: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
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
