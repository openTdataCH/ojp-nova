from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDuration

from ojp2.ojperror_structure import OjperrorStructure
from ojp2.trip_fare_result_structure import TripFareResultStructure
from ojp2.trip_structure import TripStructure
from ojp2.trip_summary_structure import TripSummaryStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class MultiPointTripResultStructure:
    """
    Structure for a multipoint trip result and associated problems.

    :ivar id: Id of this trip result for referencing purposes. Unique
        within multipoint-trip response.
    :ivar error_condition: Problems related to this trip result.
    :ivar trip: Information on the trip.
    :ivar trip_summary: Summary on trip. Only if requestor set
        TripSummaryOnly in request.
    :ivar origin_wait_time: Additional wait time at origin of this trip.
    :ivar destination_wait_time: Additional wait time at destination of
        this trip.
    :ivar trip_fare: Fare and fare product information for this trip as
        a whole or parts of it.
    """

    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        },
    )
    error_condition: list[OjperrorStructure] = field(
        default_factory=list,
        metadata={
            "name": "ErrorCondition",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    trip: Optional[TripStructure] = field(
        default=None,
        metadata={
            "name": "Trip",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    trip_summary: Optional[TripSummaryStructure] = field(
        default=None,
        metadata={
            "name": "TripSummary",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    origin_wait_time: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "OriginWaitTime",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    destination_wait_time: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "DestinationWaitTime",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    trip_fare: list[TripFareResultStructure] = field(
        default_factory=list,
        metadata={
            "name": "TripFare",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
