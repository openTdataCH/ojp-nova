from dataclasses import dataclass, field
from typing import Optional
from ojp.abstract_ojpservice_request_structure import AbstractOjpserviceRequestStructure
from ojp.extensions_1 import Extensions1
from ojp.fare_param_structure import FareParamStructure
from ojp.multi_trip_fare_request_structure import MultiTripFareRequestStructure
from ojp.static_fare_request_structure import StaticFareRequestStructure
from ojp.stop_fare_request_structure import StopFareRequestStructure
from ojp.trip_fare_request_structure import TripFareRequestStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class OjpfareRequestStructure(AbstractOjpserviceRequestStructure):
    """
    :ivar stop_fare_request: A request for stop-related Fare
        information.
    :ivar static_fare_request: A request for general/static Fare
        information.
    :ivar trip_fare_request: A request to calculate the Fare information
        of a single trip
    :ivar multi_trip_fare_request: A request to calculate aggregated
        Fare information of multiple single trips
    :ivar params: Parameter to filter the response contents.
    :ivar extensions:
    """
    class Meta:
        name = "OJPFareRequestStructure"

    stop_fare_request: Optional[StopFareRequestStructure] = field(
        default=None,
        metadata={
            "name": "StopFareRequest",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    static_fare_request: Optional[StaticFareRequestStructure] = field(
        default=None,
        metadata={
            "name": "StaticFareRequest",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    trip_fare_request: Optional[TripFareRequestStructure] = field(
        default=None,
        metadata={
            "name": "TripFareRequest",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    multi_trip_fare_request: Optional[MultiTripFareRequestStructure] = field(
        default=None,
        metadata={
            "name": "MultiTripFareRequest",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    params: Optional[FareParamStructure] = field(
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
