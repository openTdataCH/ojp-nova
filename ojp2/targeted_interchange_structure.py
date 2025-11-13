from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDuration

from ojp2.connection_link_ref_structure import ConnectionLinkRefStructure
from ojp2.contextualised_connection_link_structure import (
    ContextualisedConnectionLinkStructure,
)
from ojp2.dated_vehicle_journey_ref_structure import (
    DatedVehicleJourneyRefStructure,
)
from ojp2.distributor_visit_number import DistributorVisitNumber
from ojp2.interchange_code import InterchangeCode

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class TargetedInterchangeStructure:
    """
    Planned Connection between two VEHICLE JOURNEYs.

    :ivar interchange_code:
    :ivar distributor_vehicle_journey_ref: Reference to a (dated)
        distributor VEHICLE JOURNEY.
    :ivar distributor_connection_link_ref: Reference to a physical
        CONNECTION LINK over which the SERVICE JOURNEY INTERCHANGE takes
        place.
    :ivar distributor_connection_link: Link to Interchange stop from
        which the distributor journey departs. If omitted: the
        distributor journey stop is the same as the feeder journey stop,
        i.e. that of theh dated call.
    :ivar distributor_visit_number:
    :ivar distributor_order: For implementations for which Order is not
        used for VisitNumber, (i.e. if VisitNumberIsOrder is false) then
        Order can be used to associate the Order as well if useful for
        translation.
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
    """

    interchange_code: Optional[InterchangeCode] = field(
        default=None,
        metadata={
            "name": "InterchangeCode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    distributor_vehicle_journey_ref: Optional[
        DatedVehicleJourneyRefStructure
    ] = field(
        default=None,
        metadata={
            "name": "DistributorVehicleJourneyRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    distributor_connection_link_ref: Optional[ConnectionLinkRefStructure] = (
        field(
            default=None,
            metadata={
                "name": "DistributorConnectionLinkRef",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
    )
    distributor_connection_link: Optional[
        ContextualisedConnectionLinkStructure
    ] = field(
        default=None,
        metadata={
            "name": "DistributorConnectionLink",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    distributor_visit_number: Optional[DistributorVisitNumber] = field(
        default=None,
        metadata={
            "name": "DistributorVisitNumber",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    distributor_order: Optional[int] = field(
        default=None,
        metadata={
            "name": "DistributorOrder",
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
