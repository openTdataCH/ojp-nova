from dataclasses import dataclass, field
from typing import Optional

from ojp2.abstract_ojpservice_request_structure import (
    AbstractOjpserviceRequestStructure,
)
from ojp2.extensions_2 import Extensions2
from ojp2.no_change_at_structure import NoChangeAtStructure
from ojp2.not_via_structure import NotViaStructure
from ojp2.participant_ref_structure import ParticipantRefStructure
from ojp2.place_context_structure import PlaceContextStructure
from ojp2.trip_param_structure import TripParamStructure
from ojp2.trip_via_structure import TripViaStructure

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
        a via stop by equivalent stops. Note: Systems may support only
        one.
    :ivar via_system: With this parameter a distributing system is asked
        to build a trip using a given System to pass through. This helps
        in selecting Exchange Points for this trip. ViaSystem is also
        used in sequence. Note: Systems may support only one.
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

    origin: list[PlaceContextStructure] = field(
        default_factory=list,
        metadata={
            "name": "Origin",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "min_occurs": 1,
        },
    )
    destination: list[PlaceContextStructure] = field(
        default_factory=list,
        metadata={
            "name": "Destination",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "min_occurs": 1,
        },
    )
    via: list[TripViaStructure] = field(
        default_factory=list,
        metadata={
            "name": "Via",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    via_system: list[ParticipantRefStructure] = field(
        default_factory=list,
        metadata={
            "name": "ViaSystem",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    not_via: list[NotViaStructure] = field(
        default_factory=list,
        metadata={
            "name": "NotVia",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    no_change_at: list[NoChangeAtStructure] = field(
        default_factory=list,
        metadata={
            "name": "NoChangeAt",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    params: Optional[TripParamStructure] = field(
        default=None,
        metadata={
            "name": "Params",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    extensions: Optional[Extensions2] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
