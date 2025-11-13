from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from ojp2.abstract_ojpservice_request_structure import (
    AbstractOjpserviceRequestStructure,
)
from ojp2.extensions_2 import Extensions2
from ojp2.journey_ref import JourneyRef
from ojp2.operating_day_ref import OperatingDayRef
from ojp2.operator_ref_structure import OperatorRefStructure
from ojp2.trip_info_param_structure import TripInfoParamStructure
from ojp2.vehicle_ref import VehicleRef

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class OjptripInfoRequestStructure(AbstractOjpserviceRequestStructure):
    """
    :ivar journey_ref:
    :ivar operating_day_ref:
    :ivar train_number:
    :ivar operator_ref:
    :ivar vehicle_ref: Reference to vehicle.
    :ivar time_of_operation: Time stamp when the vehicle is operating.
        In most use cases equal to "now".
    :ivar params: Request parameter.
    :ivar extensions:
    """

    class Meta:
        name = "OJPTripInfoRequestStructure"

    journey_ref: Optional[JourneyRef] = field(
        default=None,
        metadata={
            "name": "JourneyRef",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    operating_day_ref: list[OperatingDayRef] = field(
        default_factory=list,
        metadata={
            "name": "OperatingDayRef",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "max_occurs": 2,
        },
    )
    train_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "TrainNumber",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    operator_ref: Optional[OperatorRefStructure] = field(
        default=None,
        metadata={
            "name": "OperatorRef",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    vehicle_ref: Optional[VehicleRef] = field(
        default=None,
        metadata={
            "name": "VehicleRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    time_of_operation: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "TimeOfOperation",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    params: Optional[TripInfoParamStructure] = field(
        default=None,
        metadata={
            "name": "Params",
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
