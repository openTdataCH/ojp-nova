from dataclasses import dataclass
from ojp.trip_info_response_structure import TripInfoResponseStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class TripInfoResponse(TripInfoResponseStructure):
    """
    TripInfo response element.
    """
    class Meta:
        namespace = "http://www.vdv.de/ojp"
