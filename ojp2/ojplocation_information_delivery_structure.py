from dataclasses import dataclass, field
from typing import Optional

from ojp2.abstract_service_delivery_structure import (
    AbstractServiceDeliveryStructure,
)
from ojp2.data_frame_ref_structure import DataFrameRefStructure
from ojp2.extensions_2 import Extensions2
from ojp2.ojperror_structure import OjperrorStructure
from ojp2.ojplocation_information_request import OjplocationInformationRequest
from ojp2.place_result_structure import PlaceResultStructure
from ojp2.response_context_structure import ResponseContextStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class OjplocationInformationDeliveryStructure(
    AbstractServiceDeliveryStructure
):
    """
    :ivar ojplocation_information_request:
    :ivar data_frame_ref: identifier of the set of data being used by an
        information system, which allows a comparison to be made with
        the versions of data being used by overlapping systems.
    :ivar calc_time: Calculation time.
    :ivar error_condition: OJP generic problem for the whole delivery.
    :ivar location_information_response_context: Context to hold
        response objects that occur frequently.
    :ivar continue_at: If the response returns fewer results than
        expected, the value of skip can be used in a follow-up request
        to get further results. It tells the server to skip the given
        number of results in its response.
    :ivar place_result: The place/location objects found by the service
        are ordered in descending order of how well they match the input
        data. The first result in the list matches best.
    :ivar extensions:
    """

    class Meta:
        name = "OJPLocationInformationDeliveryStructure"

    ojplocation_information_request: Optional[
        OjplocationInformationRequest
    ] = field(
        default=None,
        metadata={
            "name": "OJPLocationInformationRequest",
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
    location_information_response_context: Optional[
        ResponseContextStructure
    ] = field(
        default=None,
        metadata={
            "name": "LocationInformationResponseContext",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    continue_at: Optional[int] = field(
        default=None,
        metadata={
            "name": "ContinueAt",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    place_result: list[PlaceResultStructure] = field(
        default_factory=list,
        metadata={
            "name": "PlaceResult",
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
