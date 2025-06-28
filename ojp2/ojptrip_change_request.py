from dataclasses import dataclass

from ojp2.ojptrip_change_request_structure import OjptripChangeRequestStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class OjptripChangeRequest(OjptripChangeRequestStructure):
    """A trip can be modified in a limited manner by specifying a longer time
    duration for a specific interchange or by specifying an estimated leg for which
    the exact time information shall be retrieved.

    In both cases, earlier or later legs of the trip may be recalculated
    as well.
    """

    class Meta:
        name = "OJPTripChangeRequest"
        namespace = "http://www.vdv.de/ojp"
