from dataclasses import dataclass, field
from typing import Optional

from ojp2.fare_product_ref import FareProductRef

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class TripFareProductReferenceStructure:
    """Element that connects FareProducts to trips.

    A TripFareProduct is a FAREPRODUCT covering a part or the whole of a
    TRIP from boarding the first public transport vehicle to alighting
    from the last public transport vehicle (corresponds to a package of
    PREASSIGNED FARE PRODUCTs)

    :ivar fare_product_ref:
    :ivar from_trip_id_ref: Identifies the "valid from" trip.
    :ivar from_leg_id_ref: Identifies the "valid from" LEG. If missing,
        then valid from the first LEG.
    :ivar to_trip_id_ref: Identifies the "valid to" trip.
    :ivar to_leg_id_ref: Identifies the "valid to" LEG. If missing, then
        valid to the last LEG.
    """

    fare_product_ref: Optional[FareProductRef] = field(
        default=None,
        metadata={
            "name": "FareProductRef",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        },
    )
    from_trip_id_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "FromTripIdRef",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        },
    )
    from_leg_id_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "FromLegIdRef",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    to_trip_id_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ToTripIdRef",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        },
    )
    to_leg_id_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ToLegIdRef",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
