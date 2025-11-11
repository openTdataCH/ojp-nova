from dataclasses import dataclass, field
from typing import Optional

from ojp2.abstract_service_delivery_structure import (
    AbstractServiceDeliveryStructure,
)
from ojp2.data_frame_ref_structure import DataFrameRefStructure
from ojp2.exchange_points_result_structure import ExchangePointsResultStructure
from ojp2.extensions_2 import Extensions2
from ojp2.ojperror_structure import OjperrorStructure
from ojp2.ojpexchange_points_request import OjpexchangePointsRequest
from ojp2.response_context_structure import ResponseContextStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class OjpexchangePointsDeliveryStructure(AbstractServiceDeliveryStructure):
    """
    :ivar ojpexchange_points_request:
    :ivar data_frame_ref: identifier of the set of data being used by an
        information system, which allows a comparison to be made with
        the versions of data being used by overlapping systems.
    :ivar calc_time: Calculation time.
    :ivar error_condition: OJP generic problem for the whole delivery.
    :ivar exchange_points_response_context: Context to hold trip
        response objects that occur frequently.
    :ivar continue_at: If the response returns fewer results than
        expected, the value of skip can be used in a follow-up request
        to get further results. It tells the server to skip the given
        number of results in its response.
    :ivar exchange_points_result: The exchange points found by the
        service.
    :ivar extensions:
    """

    class Meta:
        name = "OJPExchangePointsDeliveryStructure"

    ojpexchange_points_request: Optional[OjpexchangePointsRequest] = field(
        default=None,
        metadata={
            "name": "OJPExchangePointsRequest",
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
    exchange_points_response_context: Optional[ResponseContextStructure] = (
        field(
            default=None,
            metadata={
                "name": "ExchangePointsResponseContext",
                "type": "Element",
                "namespace": "http://www.vdv.de/ojp",
            },
        )
    )
    continue_at: Optional[int] = field(
        default=None,
        metadata={
            "name": "ContinueAt",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    exchange_points_result: list[ExchangePointsResultStructure] = field(
        default_factory=list,
        metadata={
            "name": "ExchangePointsResult",
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
