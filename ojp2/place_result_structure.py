from dataclasses import dataclass, field
from typing import Optional

from ojp2.ojperror_structure import OjperrorStructure
from ojp2.operator_refs_rel_structure import OperatorRefsRelStructure
from ojp2.participant_ref_structure import ParticipantRefStructure
from ojp2.place_structure import PlaceStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class PlaceResultStructure:
    """
    :ivar error_condition: Problems related to this LOCATION result.
    :ivar place: The Place / Location object.
    :ivar complete: States whether the included location/place is
        complete or needs further refinement. Only complete
        locations/places are fully resolved and can be used in e.g.,
        trip requests. Incomplete locations/places must be refined
        entering them once again into a LocationInformationRequest.
    :ivar probability: Probability, that this result is the one meant by
        the user's input. Value should be between 0 and 1.
    :ivar system: Stores the system reference, where to ask for actual
        locations corresponding to this city name result. To get actual
        locations, a new location information request using the system
        ID of this result is needed.
    :ivar operators: List of operators operating at this place object.
        This list should only be filled if this is explicitly requested.
    """

    error_condition: list[OjperrorStructure] = field(
        default_factory=list,
        metadata={
            "name": "ErrorCondition",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    place: Optional[PlaceStructure] = field(
        default=None,
        metadata={
            "name": "Place",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        },
    )
    complete: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Complete",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        },
    )
    probability: Optional[float] = field(
        default=None,
        metadata={
            "name": "Probability",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "min_inclusive": 0.0,
            "max_inclusive": 1.0,
        },
    )
    system: Optional[ParticipantRefStructure] = field(
        default=None,
        metadata={
            "name": "System",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    operators: Optional[OperatorRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "Operators",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
