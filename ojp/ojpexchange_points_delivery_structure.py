from dataclasses import dataclass, field
from typing import List, Optional
from ojp.abstract_service_delivery_structure import AbstractServiceDeliveryStructure
from ojp.exchange_points_result_structure import ExchangePointsResultStructure
from ojp.extensions_1 import Extensions1
from ojp.ojpexchange_points_request import OjpexchangePointsRequest

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class OjpexchangePointsDeliveryStructure(AbstractServiceDeliveryStructure):
    """
    :ivar ojpexchange_points_request:
    :ivar data_frame_ref: identifier of the set of data being used by an
        information system, which allows a comparison to be made with
        the versions of data being used by overlapping systems.
    :ivar calc_time: Calculation time.
    :ivar continue_at: If the response returns less results than
        expected, the value of skip can be used in a follow-up request
        to get further results. It tells the server to skip the given
        number of results in its response.
    :ivar place:
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
    continue_at: Optional[int] = field(
        default=None,
        metadata={
            "name": "ContinueAt",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    place: List[ExchangePointsResultStructure] = field(
        default_factory=list,
        metadata={
            "name": "Place",
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
