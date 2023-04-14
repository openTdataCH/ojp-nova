from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime, XmlDuration
from ojp.individual_transport_options_structure import IndividualTransportOptionsStructure
from ojp.place_ref_structure import PlaceRefStructure
from ojp.trip_location_structure import TripLocationStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class PlaceContextStructure:
    """
    [a view of PLACE in TMv6] a PLACE and access to it by individual transport.

    :ivar place_ref: Spatial location.
    :ivar trip_location: Location within a (moving) vehicle.
    :ivar dep_arr_time: Time when departure/arrival from/to location is
        required.
    :ivar time_allowance: Extra time needed before reaching/after
        leaving this location.
    :ivar individual_transport_options: Options how to access/leave the
        location by individual transport.
    """
    place_ref: Optional[PlaceRefStructure] = field(
        default=None,
        metadata={
            "name": "PlaceRef",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    trip_location: Optional[TripLocationStructure] = field(
        default=None,
        metadata={
            "name": "TripLocation",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    dep_arr_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DepArrTime",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    time_allowance: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "TimeAllowance",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    individual_transport_options: List[IndividualTransportOptionsStructure] = field(
        default_factory=list,
        metadata={
            "name": "IndividualTransportOptions",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
