from dataclasses import dataclass, field
from typing import Optional

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
    :ivar from_trip_leg_id_ref: Identifies the "valid from" tripLeg. If
        missing, then valid from the first leg.
    :ivar to_trip_id_ref: Identifies the "valid to" trip.
    :ivar to_trip_leg_id_ref: Identifies the "valid to" tripLeg. If
        missing, then valid to the last leg.
    """
    fare_product_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "FareProductRef",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        }
    )
    from_trip_id_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "FromTripIdRef",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        }
    )
    from_trip_leg_id_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "FromTripLegIdRef",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    to_trip_id_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ToTripIdRef",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        }
    )
    to_trip_leg_id_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ToTripLegIdRef",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
