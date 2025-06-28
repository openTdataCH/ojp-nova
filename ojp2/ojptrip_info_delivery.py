from dataclasses import dataclass

from ojp2.ojptrip_info_delivery_structure import OjptripInfoDeliveryStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class OjptripInfoDelivery(OjptripInfoDeliveryStructure):
    """This service provides information on a single leg (service pattern, real-
    time status, vehicle facilities etc.).

    The service always provides information about a VEHICLE or a SERVICE
    JOURNEY. It doesn't directly provide information about a trip. If
    the response changes the conditions in such a way that the trip
    becomes invalid (connection no longer possible, delay,
    cancellation), a new TripRequest is required for the remainder of
    the trip. The service also provides information about formation,
    occupancy, and capacity. The full SIRI elements are used. Therefore,
    a lot of things can be expressed. Some that go beyond what usually
    may be required. However, if accessibility is fully to be considered
    (with stop-vehicle interaction), then SIRI must be used in full. The
    relevant SIRI documentation should be considered. This service
    implements PI QR Service Journey Request and PI QR Single Journey
    Request from TM 6.
    """

    class Meta:
        name = "OJPTripInfoDelivery"
        namespace = "http://www.vdv.de/ojp"
