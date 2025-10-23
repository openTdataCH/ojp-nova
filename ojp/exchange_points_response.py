from dataclasses import dataclass
from ojp.exchange_points_response_structure import ExchangePointsResponseStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class ExchangePointsResponse(ExchangePointsResponseStructure):
    class Meta:
        namespace = "http://www.vdv.de/ojp"
