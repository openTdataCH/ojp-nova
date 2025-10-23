from dataclasses import dataclass
from ojp.fare_response_structure import FareResponseStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class FareResponse(FareResponseStructure):
    """
    Fare response element.
    """
    class Meta:
        namespace = "http://www.vdv.de/ojp"
