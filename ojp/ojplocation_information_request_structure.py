from dataclasses import dataclass, field
from typing import Optional
from ojp.abstract_ojpservice_request_structure import AbstractOjpserviceRequestStructure
from ojp.extensions_1 import Extensions1
from ojp.initial_location_input_structure import InitialLocationInputStructure
from ojp.place_param_structure import PlaceParamStructure
from ojp.place_ref_structure import PlaceRefStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class OjplocationInformationRequestStructure(AbstractOjpserviceRequestStructure):
    """
    :ivar initial_input: Initial input for the location information
        request. This input defines what is originally looked for.
    :ivar place_ref: Location for further refinement. If a location in a
        previous response was marked as not "complete" it can be refined
        by putting it here.
    :ivar restrictions: E.g. location types (stops, addresses, POIs) or
        specific location attributes
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
        }
    )
    place_ref: Optional[PlaceRefStructure] = field(
        default=None,
        metadata={
            "name": "PlaceRef",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    restrictions: Optional[PlaceParamStructure] = field(
        default=None,
        metadata={
            "name": "Restrictions",
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
