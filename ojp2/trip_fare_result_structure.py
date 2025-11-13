from dataclasses import dataclass, field
from typing import Optional

from ojp2.fare_product_structure import FareProductStructure
from ojp2.ojperror_structure import OjperrorStructure
from ojp2.tariff_zone_list_in_area_structure import (
    TariffZoneListInAreaStructure,
)
from ojp2.web_link_structure import WebLinkStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class TripFareResultStructure:
    """Structure of a single TripFareResult.

    This may cover the whole trip or only the part the service can
    answer. If only partial answers can be delivered, then this must be
    indicated with FARE_ADDITIONALTICKETS (as a warning). For a given
    trip multiple FareResults may need to be combined to get the whole
    tariff. A typical example may be classic public transport and a
    sharing leg. Some legs, e.g., TransferLegs and walking ContinuousLeg
    will never have a price. The service may include them in one of the
    tickets. If the whole trip is for free, then a TripFareResult with a
    price of 0 is expected. It is possible to have combined FareResults
    (e.g., for a bundle) and in addition price each leg individually.

    :ivar error_condition: Result-specific error messages.
    :ivar trip_id:
    :ivar booking_id:
    :ivar from_leg_id_ref: Identifies the "valid from" LEG.
    :ivar to_leg_id_ref: Identifies the "valid to" LEG.
    :ivar passed_zones: The sequence of passed fare zones.
    :ivar fare_product: One or more FareProducts that are valid for this
        part of the trip.
    :ivar static_info_url: URL to static information page on the web.
    """

    error_condition: list[OjperrorStructure] = field(
        default_factory=list,
        metadata={
            "name": "ErrorCondition",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    trip_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TripId",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    booking_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "BookingId",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    from_leg_id_ref: list[str] = field(
        default_factory=list,
        metadata={
            "name": "FromLegIdRef",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    to_leg_id_ref: list[str] = field(
        default_factory=list,
        metadata={
            "name": "ToLegIdRef",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    passed_zones: Optional[TariffZoneListInAreaStructure] = field(
        default=None,
        metadata={
            "name": "PassedZones",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    fare_product: list[FareProductStructure] = field(
        default_factory=list,
        metadata={
            "name": "FareProduct",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    static_info_url: list[WebLinkStructure] = field(
        default_factory=list,
        metadata={
            "name": "StaticInfoUrl",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
