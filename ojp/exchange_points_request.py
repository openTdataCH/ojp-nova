from dataclasses import dataclass
from ojp.exchange_points_request_structure import ExchangePointsRequestStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class ExchangePointsRequest(ExchangePointsRequestStructure):
    class Meta:
        namespace = "http://www.vdv.de/ojp"
