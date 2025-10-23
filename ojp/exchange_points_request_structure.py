from dataclasses import dataclass, field
from typing import Optional
from ojp.exchange_points_param_structure import ExchangePointsParamStructure
from ojp.place_ref_structure import PlaceRefStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class ExchangePointsRequestStructure:
    """
    :ivar place_ref: Location for which exchange points to other
        "neighbour" systems are to be searched. This location is usually
        the origin/destination of a passenger journey. May be omitted if
        all exchange points shall be returned.
    :ivar params: E.g. location types (stops, addresses, POIs) or
        specific location attributes
    :ivar extension:
    """
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
    extension: Optional[object] = field(
        default=None,
        metadata={
            "name": "Extension",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
