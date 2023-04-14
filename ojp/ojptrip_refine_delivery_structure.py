from dataclasses import dataclass, field
from typing import List, Optional
from ojp.abstract_service_delivery_structure import AbstractServiceDeliveryStructure
from ojp.extensions_2 import Extensions2
from ojp.ojptrip_refine_request import OjptripRefineRequest
from ojp.response_context_structure import ResponseContextStructure
from ojp.trip_result_structure import TripResultStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class OjptripRefineDeliveryStructure(AbstractServiceDeliveryStructure):
    """
    :ivar ojptrip_refine_request:
    :ivar data_frame_ref: identifier of the set of data being used by an
        information system, which allows a comparison to be made with
        the versions of data being used by overlapping systems.
    :ivar calc_time: Calculation time.
    :ivar trip_response_context: Context to hold trip response objects
        that occur frequently.
    :ivar unknown_leg_ref: Refers to a leg that was not found in the
        data of the server. If the to be refined TripResult could not be
        found or unequivocally determined, all RefineLegRefs are
        returned as UnknownLegRefs.
    :ivar trip_result: The trip results refined by the server.
    :ivar extensions:
    """
    class Meta:
        name = "OJPTripRefineDeliveryStructure"

    ojptrip_refine_request: Optional[OjptripRefineRequest] = field(
        default=None,
        metadata={
            "name": "OJPTripRefineRequest",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    data_frame_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "DataFrameRef",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    calc_time: Optional[int] = field(
        default=None,
        metadata={
            "name": "CalcTime",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
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
    unknown_leg_ref: List[str] = field(
        default_factory=list,
        metadata={
            "name": "UnknownLegRef",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    trip_result: List[TripResultStructure] = field(
        default_factory=list,
        metadata={
            "name": "TripResult",
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
