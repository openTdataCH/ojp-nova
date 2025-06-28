from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDuration

from ojp2.extend_to_front_or_back_type import ExtendToFrontOrBackType
from ojp2.trip_param_structure import TripParamStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class TripChangeParamStructure:
    """
    Trip change request parameter structure.

    :ivar change_leg_ref: Refers to the leg to be adapted by the server.
        Typical usage: either a transfer leg representing an interchange
        that is considered too short or a sharing leg for which the
        exact times shall be retrieved for a specific operator.
    :ivar system_id: System reference to use for the refinement. If not
        specified, the origin systems of each leg are used for the
        refinement.
    :ivar extend_to_front_or_back: Whether to extend the initial time
        interval of the ChangeLeg towards the front or the back of the
        trip (earlier respectively later times).
    :ivar additional_waiting_time: Absolute time in minutes the
        passenger wants additionally to make the interchange. If another
        TransferLeg is needed (e.g., since another quay is used for the
        found arrival/departure) this is taken into account. If not
        passed, the next best arrival/departure is requested.
    :ivar trip_params: Options to control the search behaviour and
        response contents. They should be largely the same as used as in
        the initial OJPTripRequest.
    :ivar extension:
    """

    change_leg_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ChangeLegRef",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        },
    )
    system_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SystemId",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    extend_to_front_or_back: Optional[ExtendToFrontOrBackType] = field(
        default=None,
        metadata={
            "name": "ExtendToFrontOrBack",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    additional_waiting_time: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "AdditionalWaitingTime",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    trip_params: Optional[TripParamStructure] = field(
        default=None,
        metadata={
            "name": "TripParams",
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
