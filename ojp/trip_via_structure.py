from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDuration
from ojp.place_ref_structure import PlaceRefStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class TripViaStructure:
    """
    VIA restrictions for a TRIP.

    :ivar via_point: Reference to specify the via location.
    :ivar dwell_time: Duration the passenger wants to stay at the via
        location. Default is 0.
    """
    via_point: Optional[PlaceRefStructure] = field(
        default=None,
        metadata={
            "name": "ViaPoint",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        }
    )
    dwell_time: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "DwellTime",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
