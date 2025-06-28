from dataclasses import dataclass

from ojp2.ojptrip_change_delivery_structure import (
    OjptripChangeDeliveryStructure,
)

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class OjptripChangeDelivery(OjptripChangeDeliveryStructure):
    """A trip can be modified in a limited manner by specifying a longer time
    duration for a specific interchange or by specifying an estimated leg for which
    the exact time information shall be retrieved.

    In both cases, earlier or later legs of the trip may be recalculated
    as well.
    """

    class Meta:
        name = "OJPTripChangeDelivery"
        namespace = "http://www.vdv.de/ojp"
