from dataclasses import dataclass, field
from typing import Optional
from ojp.operators_rel_structure import OperatorsRelStructure
from ojp.places_structure import PlacesStructure
from ojp.situations_structure import SituationsStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class ResponseContextStructure:
    """
    Structure providing response contexts related to journeys, containing
    collections of places and situations.

    :ivar operators: Container for OPERATOR objects. Only operator
        objects that are referenced in the response should be put into
        the container.
    :ivar places: Container for place objects. Only place objects that
        are referenced in the response should be put into the container.
    :ivar situations: Container for SIRI SX situation objects. Only
        situations that are referenced in the response should be put
        into the container.
    """
    operators: Optional[OperatorsRelStructure] = field(
        default=None,
        metadata={
            "name": "Operators",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    places: Optional[PlacesStructure] = field(
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
