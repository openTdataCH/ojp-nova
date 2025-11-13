from dataclasses import dataclass

from ojp2.ojptrip_refine_delivery_structure import (
    OjptripRefineDeliveryStructure,
)

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class OjptripRefineDelivery(OjptripRefineDeliveryStructure):
    """The trip refinement service retrieves additional or updated information
    (e.g., real-time data) about a given, previously retrieved trip.

    It does not depend on the assumption that the trip has been
    retrieved from the same server; it may, in fact, even stem from
    another source than a OJP system. An example scenario may involve a
    trip retrieved from a system A and one wishes to refine the trip
    with real time information from another system B. As it cannot be
    ascertained that both systems use identical object IDs, this is
    signalled by setting ExternalObjectRefs to true. System B, being
    confronted with external IDs, must try to recognise the relevant
    objects in another way and retrieve them in its own database. In the
    response it will use its own object IDs. To maintain a consistent
    mapping, it is imperative that system B reflects the structure of
    the refine request precisely in its response (principle of structure
    maintenance).
    """

    class Meta:
        name = "OJPTripRefineDelivery"
        namespace = "http://www.vdv.de/ojp"
