from dataclasses import dataclass

from ojp2.ojpexchange_points_delivery_structure import (
    OjpexchangePointsDeliveryStructure,
)

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class OjpexchangePointsDelivery(OjpexchangePointsDeliveryStructure):
    """Distributed journey planning requires several journey planning systems
    planning parts of the whole trip which shall be assembled.

    Each of the planners will therefore get a sub-query to plan: the first planner from the origin of the trip to its system boundaries, the next planner must find trips from these boundaries to its boundaries with the next systems. This process will be continued until the final system where the destination of the user’s trip is located.
    The boundary points where the trip calculation is handed over to the next journey planning system are called exchange points. If they are not known in advance the exchange points can be looked up from a server by using the exchange points service. This service implements the model PI QR Location Request from TM 6.
    """

    class Meta:
        name = "OJPExchangePointsDelivery"
        namespace = "http://www.vdv.de/ojp"
