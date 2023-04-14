from dataclasses import dataclass, field
from typing import Optional
from ojp.abstract_service_delivery_structure import AbstractServiceDeliveryStructure
from ojp.availability_result_structure import AvailabilityResultStructure
from ojp.extensions_2 import Extensions2
from ojp.response_context_structure import ResponseContextStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class OjpavailabilityDeliveryStructure(AbstractServiceDeliveryStructure):
    """
    :ivar data_frame_ref: identifier of the set of data being used by an
        information system, which allows a comparison to be made with
        the versions of data being used by overlapping systems.
    :ivar calc_time: Calculation time.
    :ivar availability_response_context: Context to hold availability
        response objects that occur frequently.
    :ivar availability_result: Indication of the availability of the
        requested service.
    :ivar extension:
    :ivar extensions:
    """
    class Meta:
        name = "OJPAvailabilityDeliveryStructure"

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
    availability_response_context: Optional[ResponseContextStructure] = field(
        default=None,
        metadata={
            "name": "AvailabilityResponseContext",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    availability_result: Optional[AvailabilityResultStructure] = field(
        default=None,
        metadata={
            "name": "AvailabilityResult",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    extension: Optional[object] = field(
        default=None,
        metadata={
            "name": "Extension",
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
