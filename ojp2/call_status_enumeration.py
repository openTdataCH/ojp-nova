from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class CallStatusEnumeration(Enum):
    """Classification of the timeliness of the CALL, according to a fixed list of
    values.

    This may reflect a presentation policy, for example CALLs less than
    one minute behind target time are still classified as on-time.
    Applications may use this to guide their own presentation of times.

    :cvar ON_TIME: Service is on time.
    :cvar EARLY: Service is earlier than expected.
    :cvar DELAYED: Service is delayed.
    :cvar CANCELLED: Service is cancelled.
    :cvar ARRIVED: Service has arrived.
    :cvar DEPARTED:
    :cvar MISSED:
    :cvar NO_REPORT: There is no information about the service.
    :cvar NOT_EXPECTED: Service is not expected to call this stop. For
        instance a flexible service that has not yet been preordered.
    """

    ON_TIME = "onTime"
    EARLY = "early"
    DELAYED = "delayed"
    CANCELLED = "cancelled"
    ARRIVED = "arrived"
    DEPARTED = "departed"
    MISSED = "missed"
    NO_REPORT = "noReport"
    NOT_EXPECTED = "notExpected"
