from dataclasses import dataclass, field
from typing import List, Optional
from ojp.place_structure import PlaceStructure
from ojp.situations_structure import SituationsStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class AbstractResponseContextStructure:
    """
    Abstract structure providing response contexts related to journeys.

    :ivar places: Container for location objects.
    :ivar situations: Container for SIRI SX situation objects.
    """
    places: Optional["AbstractResponseContextStructure.Places"] = field(
        default=None,
        metadata={
            "name": "Places",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    situations: Optional[SituationsStructure] = field(
        default=None,
        metadata={
            "name": "Situations",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )

    @dataclass
    class Places:
        location: List[PlaceStructure] = field(
            default_factory=list,
            metadata={
                "name": "Location",
                "type": "Element",
                "namespace": "http://www.vdv.de/ojp",
                "min_occurs": 1,
            }
        )
