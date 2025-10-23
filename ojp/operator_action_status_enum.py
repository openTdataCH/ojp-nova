from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


class OperatorActionStatusEnum(Enum):
    REQUESTED = "requested"
    APPROVED = "approved"
    BEING_IMPLEMENTED = "beingImplemented"
    IMPLEMENTED = "implemented"
    REJECTED = "rejected"
    TERMINATION_REQUESTED = "terminationRequested"
    BEING_TERMINATED = "beingTerminated"
