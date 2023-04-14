from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDuration
from ojp.individual_modes_enumeration import IndividualModesEnumeration

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class IndividualTransportOptionsStructure:
    """
    Individual modes and their usage limits as stated by the passenger.

    :ivar mode:
    :ivar max_distance: Maximum distance in meters. If given, it
        restricts the maximum distance of routes with the given mode.
    :ivar max_duration: Maximum duration. If given, it restricts the
        maximum time of routes with the given mode.
    :ivar min_distance: Minimum distance in meters. If given, it
        restricts the minimum distance of routes with the given mode.
    :ivar min_duration: Minimum duration. If given, it restricts the
        minimum time of routes with the given mode.
    :ivar speed: Relative speed in percent. If given slows the standard
        speed (below 100) or fasten it (above 100).
    """
    mode: Optional[IndividualModesEnumeration] = field(
        default=None,
        metadata={
            "name": "Mode",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        }
    )
    max_distance: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaxDistance",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    max_duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MaxDuration",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    min_distance: Optional[int] = field(
        default=None,
        metadata={
            "name": "MinDistance",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    min_duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MinDuration",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    speed: Optional[int] = field(
        default=None,
        metadata={
            "name": "Speed",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
