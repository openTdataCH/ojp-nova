from dataclasses import dataclass, field
from typing import Optional

from ojp2.abstract_ojpservice_request_structure import (
    AbstractOjpserviceRequestStructure,
)
from ojp2.extensions_2 import Extensions2
from ojp2.response_context_structure import ResponseContextStructure
from ojp2.trip_change_param_structure import TripChangeParamStructure
from ojp2.trip_result_structure import TripResultStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class OjptripChangeRequestStructure(AbstractOjpserviceRequestStructure):
    """
    :ivar change_params: Options to control the change.
    :ivar trip_result: The trip result to be changed by the server.
    :ivar trip_response_context: Context to hold objects, which are
        referenced within the response.
    :ivar extensions:
    """

    class Meta:
        name = "OJPTripChangeRequestStructure"

    change_params: Optional[TripChangeParamStructure] = field(
        default=None,
        metadata={
            "name": "ChangeParams",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    trip_result: Optional[TripResultStructure] = field(
        default=None,
        metadata={
            "name": "TripResult",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        },
    )
    trip_response_context: Optional[ResponseContextStructure] = field(
        default=None,
        metadata={
            "name": "TripResponseContext",
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
