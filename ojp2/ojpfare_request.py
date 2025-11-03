from dataclasses import dataclass

from ojp2.ojpfare_request_structure import OjpfareRequestStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class OjpfareRequest(OjpfareRequestStructure):
    """This service provides general, stop-specific and trip-specific fare
    information.

    This service implements the models PI Stop Fare Request, PI FQ Fare
    Product Request, PI FQ Single Trip Fare Request from TM 6.
    """

    class Meta:
        name = "OJPFareRequest"
        namespace = "http://www.vdv.de/ojp"
