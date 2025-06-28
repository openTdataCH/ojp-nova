from dataclasses import dataclass, field
from typing import Optional

from ojp2.abstract_ojpservice_request_structure import (
    AbstractOjpserviceRequestStructure,
)
from ojp2.extensions_2 import Extensions2
from ojp2.initial_location_input_structure import InitialLocationInputStructure
from ojp2.place_param_structure import PlaceParamStructure
from ojp2.place_ref_structure import PlaceRefStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class OjplocationInformationRequestStructure(
    AbstractOjpserviceRequestStructure
):
    """
    :ivar initial_input: Initial input for the location information
        request. This input defines what is originally looked for. Be
        aware that this also can contain PLACEs.
    :ivar place_ref: LOCATION / PLACE for further refinement. If a Place
        in a previous response was marked as not "complete" it can be
        refined by putting it here. If Places are organised
        hierarchically, it may be reasonable to identify the Place in a
        top-down approach with several steps of refining a Place on each
        level of hierarchy. Following this approach an initial request
        retrieves a first list of top-level Places (e.g., streets) which
        are to be refined in a subsequent request to the next level
        (e.g., house number intervals). The objects of the current level
        are presented to the user for selection. The object reference of
        the selected object is then sent in the next request for further
        refinement.
    :ivar restrictions: E.g. place types (stops, addresses, POIs) or
        specific place attributes
    :ivar extensions:
    """

    class Meta:
        name = "OJPLocationInformationRequestStructure"

    initial_input: Optional[InitialLocationInputStructure] = field(
        default=None,
        metadata={
            "name": "InitialInput",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    place_ref: Optional[PlaceRefStructure] = field(
        default=None,
        metadata={
            "name": "PlaceRef",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    restrictions: Optional[PlaceParamStructure] = field(
        default=None,
        metadata={
            "name": "Restrictions",
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
