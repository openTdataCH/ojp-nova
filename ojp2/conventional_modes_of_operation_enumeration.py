from enum import Enum

__NAMESPACE__ = "http://www.vdv.de/ojp"


class ConventionalModesOfOperationEnumeration(Enum):
    """Types of MODES OF OPERATION  are scheduled, classic and flexible.

    From NeTEx.

    :cvar SCHEDULED: Regular MODE OF OPERATION for CONVENTIONAL MODE OF
        OPERATION. Based on SCHEDULED STOP POINTs and timetables.
    :cvar DEMAND_RESPONSIVE: Demand responsive services. General term
        when nothing else is known. Requires SCHEDULED STOP POINTs. The
        more taxi-like a demand responsive service becomes the more
        probable it is better to use ALTERNATIVE MODE OF OPERATION.
    :cvar FLEXIBLE_ROUTE: Specialisation of demand responsive MODE OF
        OPERATION. The service is still based on a ROUTE.
    :cvar FLEXIBLE_AREA: Specialisation of demand responsive MODE OF
        OPERATION. The service is based on AREAs, but still SCHEDULED
        STOP POINTs are used. Sometimes the characteristics of a given
        demand responsive service makes it mor of an ALTERNATIVE MODE OF
        OPERATION (e.g., pure area service). A conventional mode of
        operation is more indicated, when there is a limited list of
        stops within the area.
    :cvar SHUTTLE: If the service is provided as a form of shuttle.
    :cvar POOLING: In some cases, pooling is not an ALTERNATIVE MODE OF
        OPERATION, but is better served with a TimedLeg. Then this MODE
        OF OPERATION is to be used.
    :cvar REPLACEMENT: The service is provided as a replacement of a
        SCHEDULED service.
    :cvar SCHOOL: MODE OF OPERATION that specifically states that it is
        school related. Specialisation of demand responsive or
        scheduled.
    :cvar P_RM: If for a scheduled, conventional service a special
        additional vehicle is needed to provide for special PRM needs.
        This kind of MODE OF OPERATION is to be used.
    """

    SCHEDULED = "scheduled"
    DEMAND_RESPONSIVE = "demandResponsive"
    FLEXIBLE_ROUTE = "flexibleRoute"
    FLEXIBLE_AREA = "flexibleArea"
    SHUTTLE = "shuttle"
    POOLING = "pooling"
    REPLACEMENT = "replacement"
    SCHOOL = "school"
    P_RM = "pRM"
