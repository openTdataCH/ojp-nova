from dataclasses import dataclass, field
from typing import Optional
from ojp.abstract_ojpservice_request_structure import AbstractOjpserviceRequestStructure
from ojp.extensions_2 import Extensions2
from ojp.response_context_structure import ResponseContextStructure
from ojp.trip_refine_param_structure import TripRefineParamStructure
from ojp.trip_result_structure import TripResultStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class OjptripRefineRequestStructure(AbstractOjpserviceRequestStructure):
    """
    :ivar refine_params: Options to control the refine
    :ivar trip_result: The trip result to be refined by the server.
    :ivar trip_response_context: Context to hold objects, which are
        referenced within the response.
    :ivar extensions:
    """
    class Meta:
        name = "OJPTripRefineRequestStructure"

    refine_params: Optional[TripRefineParamStructure] = field(
        default=None,
        metadata={
            "name": "RefineParams",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    trip_result: Optional[TripResultStructure] = field(
        default=None,
        metadata={
            "name": "TripResult",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        }
    )
    trip_response_context: Optional[ResponseContextStructure] = field(
        default=None,
        metadata={
            "name": "TripResponseContext",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    extensions: Optional[Extensions2] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
