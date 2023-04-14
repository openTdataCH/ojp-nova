from dataclasses import dataclass, field
from typing import List, Optional
from ojp.mode_structure import ModeStructure
from ojp.place_structure import PlaceStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class PlaceResultStructure:
    """
    :ivar location:
    :ivar complete: States whether the included location is complete or
        needs further refinement. Only complete locations are fully
        resolved and can be used in e.g. trip requests. Incomplete
        locations have to be refined entering them once again into a
        LocationInformationRequest.
    :ivar probability: Probability, that this result is the one meant by
        the user's input. Value should be between 0 and 1.
    :ivar mode:
    """
    location: Optional[PlaceStructure] = field(
        default=None,
        metadata={
            "name": "Location",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        }
    )
    complete: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Complete",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        }
    )
    probability: Optional[float] = field(
        default=None,
        metadata={
            "name": "Probability",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "min_inclusive": 0.0,
            "max_inclusive": 1.0,
        }
    )
    mode: List[ModeStructure] = field(
        default_factory=list,
        metadata={
            "name": "Mode",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
