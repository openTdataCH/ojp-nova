from dataclasses import dataclass, field
from typing import Optional

from ojp2.abstract_service_delivery_structure import (
    AbstractServiceDeliveryStructure,
)
from ojp2.availability_result_structure import AvailabilityResultStructure
from ojp2.data_frame_ref_structure import DataFrameRefStructure
from ojp2.extensions_2 import Extensions2
from ojp2.ojperror_structure import OjperrorStructure
from ojp2.response_context_structure import ResponseContextStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class OjpavailabilityDeliveryStructure(AbstractServiceDeliveryStructure):
    """
    :ivar data_frame_ref: identifier of the set of data being used by an
        information system, which allows a comparison to be made with
        the versions of data being used by overlapping systems.
    :ivar calc_time: Calculation time.
    :ivar error_condition: OJP generic problem for the whole delivery.
    :ivar availability_response_context: Context to hold availability
        response objects that occur frequently.
    :ivar availability_result: Indication of the availability of the
        requested service.
    :ivar extension:
    :ivar extensions:
    """

    class Meta:
        name = "OJPAvailabilityDeliveryStructure"

    data_frame_ref: Optional[DataFrameRefStructure] = field(
        default=None,
        metadata={
            "name": "DataFrameRef",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    calc_time: Optional[int] = field(
        default=None,
        metadata={
            "name": "CalcTime",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    error_condition: list[OjperrorStructure] = field(
        default_factory=list,
        metadata={
            "name": "ErrorCondition",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    availability_response_context: Optional[ResponseContextStructure] = field(
        default=None,
        metadata={
            "name": "AvailabilityResponseContext",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    availability_result: Optional[AvailabilityResultStructure] = field(
        default=None,
        metadata={
            "name": "AvailabilityResult",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    extension: Optional[object] = field(
        default=None,
        metadata={
            "name": "Extension",
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
