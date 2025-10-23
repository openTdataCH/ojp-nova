from dataclasses import dataclass
from ojp.fare_request_structure import FareRequestStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class FareRequest(FareRequestStructure):
    class Meta:
        namespace = "http://www.vdv.de/ojp"
