from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class VehicleStatusEnumeration(Enum):
    """Classification of the State of the VEHICLE JOURNEY according to a fixed list
    of values.

    This may reflect a presentation policy, for example CALLs less than
    one minute behind target time are still classified as on-time.
    Applications may use this to guide their own presentation of times.

    :cvar EXPECTED: Service is expected to be performed.
    :cvar NOT_EXPECTED: Service is not expected to be run. For instance
        a flexible service that has not yet been preordered.
    :cvar CANCELLED:
    :cvar ASSIGNED:
    :cvar SIGNED_ON:
    :cvar AT_ORIGIN:
    :cvar IN_PROGRESS: Service has departed from first stop.
    :cvar ABORTED:
    :cvar OFF_ROUTE:
    :cvar COMPLETED: It has been detected that the Service was
        completed.
    :cvar ASSUMED_COMPLETED: It is assumed that the Service has
        completed.
    :cvar NOT_RUN:
    """

    EXPECTED = "expected"
    NOT_EXPECTED = "notExpected"
    CANCELLED = "cancelled"
    ASSIGNED = "assigned"
    SIGNED_ON = "signedOn"
    AT_ORIGIN = "atOrigin"
    IN_PROGRESS = "inProgress"
    ABORTED = "aborted"
    OFF_ROUTE = "offRoute"
    COMPLETED = "completed"
    ASSUMED_COMPLETED = "assumedCompleted"
    NOT_RUN = "notRun"
