from dataclasses import dataclass

from ojp2.ojpavailability_request_structure import (
    OjpavailabilityRequestStructure,
)

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class OjpavailabilityRequest(OjpavailabilityRequestStructure):
    """The availability service informs about the availability of a MOBILITY
    SERVICE, a VEHICLE, SERVICE JOURNEY, or SINGLE JOURNEY.

    This service implements the models PI QR AM Vehicle Type Request and
    PI QR AM Mobility Service Request from TM 6.
    """

    class Meta:
        name = "OJPAvailabilityRequest"
        namespace = "http://www.vdv.de/ojp"
