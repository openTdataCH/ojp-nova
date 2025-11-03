from dataclasses import dataclass, field
from typing import Optional

from ojp2.ojperror_structure import OjperrorStructure
from ojp2.trip_fare_result_structure import TripFareResultStructure
from ojp2.trip_structure import TripStructure
from ojp2.trip_summary_structure import TripSummaryStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class TripResultStructure:
    """
    Structure for a single trip result and associated problems.

    :ivar id: Id of this trip result for referencing purposes. Unique
        within trip response.
    :ivar error_condition: Problems related to this Trip result.
    :ivar trip: Detailed information on trip.
    :ivar trip_summary: Summary on trip. Only if requestor set
        TripSummaryOnly in request.
    :ivar trip_fare: Fare and fare product information for this trip as
        a whole or parts of it.
    :ivar is_alternative_option: When the result is an alternative
        option from IncludeAlternativeOptions, then the flag should be
        set to true. If it is an alternative option this means that the
        server decided to add this result for its own reasons: e.g., to
        push a certain trip leg, because it believes that it might
        better suit at least some possible customers. Such options are
        not an optimal fit to the criteria that were in the request. The
        client may therefore disregard such results depending on the use
        case.
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
    trip_fare: list[TripFareResultStructure] = field(
        default_factory=list,
        metadata={
            "name": "TripFare",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    is_alternative_option: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsAlternativeOption",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
