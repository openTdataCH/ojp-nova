from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDuration

from ojp2.aimed_arrival_time_of_feeder import AimedArrivalTimeOfFeeder
from ojp2.aimed_departure_time_of_distributor import (
    AimedDepartureTimeOfDistributor,
)
from ojp2.connection_link_ref import ConnectionLinkRef
from ojp2.distributor_departure_stop_ref import DistributorDepartureStopRef
from ojp2.distributor_ref import DistributorRef
from ojp2.distributor_stop_order import DistributorStopOrder
from ojp2.distributor_visit_number import DistributorVisitNumber
from ojp2.extensions_2 import Extensions2
from ojp2.extra_interchange import ExtraInterchange
from ojp2.feeder_arrival_stop_ref import FeederArrivalStopRef
from ojp2.feeder_ref import FeederRef
from ojp2.feeder_stop_order import FeederStopOrder
from ojp2.feeder_visit_number import FeederVisitNumber
from ojp2.interchange_code import InterchangeCode
from ojp2.interchange_ref import InterchangeRef
from ojp2.reason_for_removal import ReasonForRemoval

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class AbstractServiceJourneyInterchangeStructure:
    """A planned SERVICE JOURNEY INTERCHANGE between two journeys.

    (since SIRI 2.0)

    :ivar interchange_code:
    :ivar interchange_ref:
    :ivar connection_link_ref:
    :ivar extra_interchange:
    :ivar cancellation:
    :ivar reason_for_removal:
    :ivar feeder_ref:
    :ivar feeder_arrival_stop_ref:
    :ivar feeder_visit_number:
    :ivar feeder_stop_order:
    :ivar aimed_arrival_time_of_feeder:
    :ivar distributor_ref:
    :ivar distributor_departure_stop_ref:
    :ivar distributor_visit_number:
    :ivar distributor_stop_order:
    :ivar aimed_departure_time_of_distributor:
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
    :ivar extensions:
    """

    interchange_code: Optional[InterchangeCode] = field(
        default=None,
        metadata={
            "name": "InterchangeCode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    interchange_ref: Optional[InterchangeRef] = field(
        default=None,
        metadata={
            "name": "InterchangeRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    connection_link_ref: Optional[ConnectionLinkRef] = field(
        default=None,
        metadata={
            "name": "ConnectionLinkRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    extra_interchange: Optional[ExtraInterchange] = field(
        default=None,
        metadata={
            "name": "ExtraInterchange",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    cancellation: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Cancellation",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    reason_for_removal: Optional[ReasonForRemoval] = field(
        default=None,
        metadata={
            "name": "ReasonForRemoval",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    feeder_ref: Optional[FeederRef] = field(
        default=None,
        metadata={
            "name": "FeederRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    feeder_arrival_stop_ref: Optional[FeederArrivalStopRef] = field(
        default=None,
        metadata={
            "name": "FeederArrivalStopRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    feeder_visit_number: Optional[FeederVisitNumber] = field(
        default=None,
        metadata={
            "name": "FeederVisitNumber",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    feeder_stop_order: Optional[FeederStopOrder] = field(
        default=None,
        metadata={
            "name": "FeederStopOrder",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    aimed_arrival_time_of_feeder: Optional[AimedArrivalTimeOfFeeder] = field(
        default=None,
        metadata={
            "name": "AimedArrivalTimeOfFeeder",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    distributor_ref: Optional[DistributorRef] = field(
        default=None,
        metadata={
            "name": "DistributorRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    distributor_departure_stop_ref: Optional[DistributorDepartureStopRef] = (
        field(
            default=None,
            metadata={
                "name": "DistributorDepartureStopRef",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
    )
    distributor_visit_number: Optional[DistributorVisitNumber] = field(
        default=None,
        metadata={
            "name": "DistributorVisitNumber",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    distributor_stop_order: Optional[DistributorStopOrder] = field(
        default=None,
        metadata={
            "name": "DistributorStopOrder",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    aimed_departure_time_of_distributor: Optional[
        AimedDepartureTimeOfDistributor
    ] = field(
        default=None,
        metadata={
            "name": "AimedDepartureTimeOfDistributor",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    stay_seated: Optional[bool] = field(
        default=None,
        metadata={
            "name": "StaySeated",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    guaranteed: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Guaranteed",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    advertised: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Advertised",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    standard_wait_time: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "StandardWaitTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    maximum_wait_time: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MaximumWaitTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    maximum_automatic_wait_time: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MaximumAutomaticWaitTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    standard_transfer_time: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "StandardTransferTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    minimum_transfer_time: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MinimumTransferTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    maximum_transfer_time: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MaximumTransferTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    extensions: Optional[Extensions2] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
