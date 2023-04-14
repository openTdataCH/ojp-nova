from dataclasses import dataclass, field
from typing import List, Optional
from ojp.natural_language_place_name_structure import NaturalLanguagePlaceNameStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class PlaceNameStructure:
    """Names of VIA points, used to help identify the LINE, for example, Luton
    to Luton via Sutton.

    Currently 3 in VDV. Should only be included if the detail level was
    requested.

    :ivar place_ref: Reference to a TOPOGRAPHIC PLACE.
    :ivar place_name: Names of place used to help identify the LINE.
    :ivar place_short_name: Short name of TOPOGRAPHIC PLACE. Should only
        be included if the detail level was requested.
    """
    place_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlaceRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    place_name: List[NaturalLanguagePlaceNameStructure] = field(
        default_factory=list,
        metadata={
            "name": "PlaceName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    place_short_name: List[NaturalLanguagePlaceNameStructure] = field(
        default_factory=list,
        metadata={
            "name": "PlaceShortName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
