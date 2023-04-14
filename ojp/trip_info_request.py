from dataclasses import dataclass
from ojp.trip_info_request_structure import TripInfoRequestStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class TripInfoRequest(TripInfoRequestStructure):
    """
    TripInfo request element.
    """
    class Meta:
        namespace = "http://www.vdv.de/ojp"
