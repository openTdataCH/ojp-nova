from dataclasses import dataclass

from ojp2.ojptrip_request_structure import OjptripRequestStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class OjptripRequest(OjptripRequestStructure):
    """This service provides intermodal trip information from an origin location to
    a destination taking various user preferences into account.

    In the case of OJPMultipointTripRequest it is a set of origins and
    destinations that are searched. This service implements the model PI
    QR Trip Request from TM 6.
    """

    class Meta:
        name = "OJPTripRequest"
        namespace = "http://www.vdv.de/ojp"
