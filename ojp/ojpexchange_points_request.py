from dataclasses import dataclass
from ojp.ojpexchange_points_request_structure import OjpexchangePointsRequestStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class OjpexchangePointsRequest(OjpexchangePointsRequestStructure):
    class Meta:
        name = "OJPExchangePointsRequest"
        namespace = "http://www.vdv.de/ojp"
