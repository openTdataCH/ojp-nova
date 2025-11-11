from dataclasses import dataclass, field
from typing import Optional

from ojp2.location_structure import LocationStructure
from ojp2.progress_between_stops_structure import ProgressBetweenStopsStructure
from ojp2.vehicle_progress_enumeration import VehicleProgressEnumeration

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class VehiclePositionStructure:
    """
    Geographical and logical position of a vehicle.

    :ivar geo_position: Geographic position of vehicle.
    :ivar progress: Logical progress of vehicle relative to service
        pattern.
    :ivar bearing: Bearing in compass degrees in which vehicle is
        heading (expected to be consistent with Transmodel ROUTE or LEG
        TRACK and PATH GUIDANCE).
    :ivar progress_between_stops: Provides information about the
        progress of the vehicle along its current link, that is link
        from previous visited top to current position.
    """

    geo_position: Optional[LocationStructure] = field(
        default=None,
        metadata={
            "name": "GeoPosition",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    progress: Optional[VehicleProgressEnumeration] = field(
        default=None,
        metadata={
            "name": "Progress",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    bearing: Optional[float] = field(
        default=None,
        metadata={
            "name": "Bearing",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    progress_between_stops: Optional[ProgressBetweenStopsStructure] = field(
        default=None,
        metadata={
            "name": "ProgressBetweenStops",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
