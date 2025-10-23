from dataclasses import dataclass, field
from typing import List, Optional
from ojp.abstract_ojpservice_request_structure import AbstractOjpserviceRequestStructure
from ojp.extensions_1 import Extensions1
from ojp.no_change_at_structure import NoChangeAtStructure
from ojp.not_via_structure import NotViaStructure
from ojp.place_context_structure import PlaceContextStructure
from ojp.trip_param_structure import TripParamStructure
from ojp.trip_via_structure import TripViaStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class OjptripRequestStructure(AbstractOjpserviceRequestStructure):
    """
    :ivar origin: Specifies the origin situation from where the user
        wants to start.
    :ivar destination: Specifies the destination situation where the
        user is heading to.
    :ivar via: Ordered series of points where the journey must pass
        through. If more than one via point is given all of them must be
        obeyed - in the correct order. The server is allowed to replace
        a via stop by equivalent stops.
    :ivar not_via: Not-via restrictions for a TRIP, i.e. SCHEDULED STOP
        POINTs or STOP PLACEs that the TRIP is not allowed to pass
        through. If more than one not via point is given all of them
        must be obeyed.
    :ivar no_change_at: no-change-at restrictions for a TRIP, i.e.
        SCHEDULED STOP POINTs or STOP PLACEs at which no TRANSFER is
        allowed within a TRIP.
    :ivar params: Options to control the search behaviour and response
        contents.
    :ivar extensions:
    """
    class Meta:
        name = "OJPTripRequestStructure"

    origin: List[PlaceContextStructure] = field(
        default_factory=list,
        metadata={
            "name": "Origin",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "min_occurs": 1,
        }
    )
    destination: List[PlaceContextStructure] = field(
        default_factory=list,
        metadata={
            "name": "Destination",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "min_occurs": 1,
        }
    )
    via: List[TripViaStructure] = field(
        default_factory=list,
        metadata={
            "name": "Via",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    not_via: List[NotViaStructure] = field(
        default_factory=list,
        metadata={
            "name": "NotVia",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    no_change_at: List[NoChangeAtStructure] = field(
        default_factory=list,
        metadata={
            "name": "NoChangeAt",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    params: Optional[TripParamStructure] = field(
        default=None,
        metadata={
            "name": "Params",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    extensions: Optional[Extensions1] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
