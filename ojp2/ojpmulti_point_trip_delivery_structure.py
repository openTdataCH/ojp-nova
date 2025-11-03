from dataclasses import dataclass, field
from typing import Optional

from ojp2.abstract_service_delivery_structure import (
    AbstractServiceDeliveryStructure,
)
from ojp2.data_frame_ref_structure import DataFrameRefStructure
from ojp2.extensions_2 import Extensions2
from ojp2.multi_point_trip_result_structure import (
    MultiPointTripResultStructure,
)
from ojp2.multi_point_type_enumeration import MultiPointTypeEnumeration
from ojp2.ojperror_structure import OjperrorStructure
from ojp2.ojpmulti_point_trip_request import OjpmultiPointTripRequest
from ojp2.response_context_structure import ResponseContextStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class OjpmultiPointTripDeliveryStructure(AbstractServiceDeliveryStructure):
    """
    :ivar ojpmulti_point_trip_request:
    :ivar data_frame_ref: identifier of the set of data being used by an
        information system, which allows a comparison to be made with
        the versions of data being used by overlapping systems.
    :ivar calc_time: Calculation time.
    :ivar error_condition: OJP generic problem for the whole delivery.
    :ivar multi_point_type: The MultiPointType should be returned
        because it may differ from the one asked. Many systems will
        support only a subset of the MultiPointTypes, and it is
        important to know what the result is based on.
    :ivar multi_point_trip_response_context: Context to hold trip
        response objects that occur frequently.
    :ivar multi_point_trip_result: The trip results found by the server.
    :ivar extensions:
    """

    class Meta:
        name = "OJPMultiPointTripDeliveryStructure"

    ojpmulti_point_trip_request: Optional[OjpmultiPointTripRequest] = field(
        default=None,
        metadata={
            "name": "OJPMultiPointTripRequest",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
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
    multi_point_type: Optional[MultiPointTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "MultiPointType",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    multi_point_trip_response_context: Optional[ResponseContextStructure] = (
        field(
            default=None,
            metadata={
                "name": "MultiPointTripResponseContext",
                "type": "Element",
                "namespace": "http://www.vdv.de/ojp",
            },
        )
    )
    multi_point_trip_result: list[MultiPointTripResultStructure] = field(
        default_factory=list,
        metadata={
            "name": "MultiPointTripResult",
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
