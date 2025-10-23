from dataclasses import dataclass, field
from typing import Optional
from ojp.abstract_ojpservice_request_structure import AbstractOjpserviceRequestStructure
from ojp.exchange_points_param_structure import ExchangePointsParamStructure
from ojp.extensions_1 import Extensions1
from ojp.place_ref_structure import PlaceRefStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class OjpexchangePointsRequestStructure(AbstractOjpserviceRequestStructure):
    """
    :ivar place_ref: Location for which exchange points to other
        "neighbour" systems are to be searched. This location is usually
        the origin/destination of a passenger journey. May be omitted if
        all exchange points shall be returned.
    :ivar params: E.g. location types (stops, addresses, POIs) or
        specific location attributes
    :ivar extensions:
    """
    class Meta:
        name = "OJPExchangePointsRequestStructure"

    place_ref: Optional[PlaceRefStructure] = field(
        default=None,
        metadata={
            "name": "PlaceRef",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    params: Optional[ExchangePointsParamStructure] = field(
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
