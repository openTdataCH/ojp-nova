from dataclasses import dataclass, field
from typing import Any, Optional

from ojp2.abstract_service_journey_interchange_structure import (
    AbstractServiceJourneyInterchangeStructure,
)
from ojp2.distributor_departure_stop_ref import DistributorDepartureStopRef
from ojp2.distributor_ref import DistributorRef
from ojp2.distributor_visit_number import DistributorVisitNumber
from ojp2.feeder_arrival_stop_ref import FeederArrivalStopRef
from ojp2.feeder_ref import FeederRef

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class FromServiceJourneyInterchangeStructure(
    AbstractServiceJourneyInterchangeStructure
):
    """A planned SERVICE JOURNEY INTERCHANGE from a journey.

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
    distributor_ref: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    distributor_departure_stop_ref: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    distributor_visit_number: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
