from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDateTime
from ojp.abstract_ojpservice_request_structure import AbstractOjpserviceRequestStructure
from ojp.extensions_1 import Extensions1
from ojp.trip_info_param_structure import TripInfoParamStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class OjptripInfoRequestStructure(AbstractOjpserviceRequestStructure):
    """
    :ivar journey_ref:
    :ivar operating_day_ref:
    :ivar vehicle_ref:
    :ivar time_of_operation: Time stamp when the vehicle is operating.
        In most use cases equal to "now".
    :ivar params: Request parameter.
    :ivar extensions:
    """
    class Meta:
        name = "OJPTripInfoRequestStructure"

    journey_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "JourneyRef",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    operating_day_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "OperatingDayRef",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    vehicle_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "VehicleRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    time_of_operation: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "TimeOfOperation",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    params: Optional[TripInfoParamStructure] = field(
        default=None,
        metadata={
            "name": "Params",
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
