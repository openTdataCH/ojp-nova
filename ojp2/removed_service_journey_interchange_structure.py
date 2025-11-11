from dataclasses import dataclass, field
from typing import Any, Optional

from ojp2.abstract_service_journey_interchange_structure import (
    AbstractServiceJourneyInterchangeStructure,
)
from ojp2.distributor_departure_stop_ref import DistributorDepartureStopRef
from ojp2.distributor_ref import DistributorRef
from ojp2.feeder_arrival_stop_ref import FeederArrivalStopRef
from ojp2.feeder_ref import FeederRef
from ojp2.interchange_ref import InterchangeRef
from ojp2.reason_for_removal import ReasonForRemoval

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class RemovedServiceJourneyInterchangeStructure(
    AbstractServiceJourneyInterchangeStructure
):
    """Type for a previously planned SERVICE JOURNEY INTERCHANGE that a data
    producer wants to silently remove from the plan (because it is erroneous data).

    Careful: Removal is different from Cancellation. (since SIRI 2.1)

    :ivar interchange_code:
    :ivar extra_interchange:
    :ivar cancellation:
    :ivar stay_seated: Whether the passenger can remain in VEHICLE (i.e.
        BLOCKlinking). Default is 'false': the passenger must change
        vehicles for this connection.
    :ivar guaranteed: Whether the SERVICE JOURNEY INTERCHANGE is
        guaranteed. Default is 'false'; SERVICE JOURNEY INTERCHANGE is
        not guaranteed.
    :ivar advertised: Whether the SERVICE JOURNEY INTERCHANGE is
        advertised as a connection. Default is 'false'.
    :ivar standard_wait_time: Standard wait time for INTERCHANGE. SIRI
        v2,0
    :ivar maximum_wait_time: Maximum time that Distributor will wait for
        Feeder for INTERCHANGE. SIRI v1.0
    :ivar maximum_automatic_wait_time: Maximum automatic wait time that
        Distributor will wait for Feeder for INTERCHANGE. (since SIRI
        2.0)
    :ivar standard_transfer_time: Standard transfer duration for
        INTERCHANGE. SIRI v2,0
    :ivar minimum_transfer_time: Minimum transfer duration for
        INTERCHANGE. SIRI v2,0
    :ivar maximum_transfer_time: Maximum transfer duration for
        INTERCHANGE. SIRI v2,0
    :ivar interchange_ref:
    :ivar reason_for_removal:
    :ivar feeder_ref:
    :ivar feeder_arrival_stop_ref:
    :ivar distributor_ref:
    :ivar distributor_departure_stop_ref:
    """

    interchange_code: Any = field(
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
    stay_seated: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    guaranteed: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    advertised: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    standard_wait_time: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    maximum_wait_time: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    maximum_automatic_wait_time: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    standard_transfer_time: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    minimum_transfer_time: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    maximum_transfer_time: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    interchange_ref: Optional[InterchangeRef] = field(
        default=None,
        metadata={
            "name": "InterchangeRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    reason_for_removal: Optional[ReasonForRemoval] = field(
        default=None,
        metadata={
            "name": "ReasonForRemoval",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
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
