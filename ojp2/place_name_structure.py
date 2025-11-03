from dataclasses import dataclass, field
from typing import Optional

from ojp2.journey_place_ref_structure import JourneyPlaceRefStructure
from ojp2.natural_language_place_name_structure import (
    NaturalLanguagePlaceNameStructure,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class PlaceNameStructure:
    """Names of VIA points, used to help identify the LINE, for example, Luton to
    Luton via Sutton.

    Currently 3 in VDV. Should only be included if the detail level was
    requested.

    :ivar place_ref: Reference to a TOPOGRAPHIC PLACE.
    :ivar place_name: Names of place used to help identify the LINE.
    :ivar place_short_name: Short name of TOPOGRAPHIC PLACE. Should only
        be included if the detail level was requested.
    """

    place_ref: Optional[JourneyPlaceRefStructure] = field(
        default=None,
        metadata={
            "name": "PlaceRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    place_name: list[NaturalLanguagePlaceNameStructure] = field(
        default_factory=list,
        metadata={
            "name": "PlaceName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    place_short_name: list[NaturalLanguagePlaceNameStructure] = field(
        default_factory=list,
        metadata={
            "name": "PlaceShortName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
