from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class InterchangeStatusEnumeration(Enum):
    """Values for TPEG Pti31 - InterchangeStatus

    :cvar UNKNOWN: TPEG Pti31_0, unknown
    :cvar CONNECTION: TPEG Pti31_1, connection
    :cvar REPLACEMENT: TPEG Pti31_2, replacement
    :cvar ALTERNATIVE: TPEG Pti31_3, alternative
    :cvar CONNECTION_NOT_HELD: TPEG Pti31_4, connection not held
    :cvar CONNECTION_HELD: TPEG Pti31_5, connection held
    :cvar STATUS_OF_CONNECTION_UNDECIDED: TPEG Pti31_6, status of
        connection undecided
    :cvar UNDEFINED_CROSS_REFERENCE_INFORMATION: TPEG Pti31_255,
        undefined cross reference information
    :cvar CONNECTION_CHANGED: Interchange is planned but was updated as
        a result of changes in the QUAYs or arrival/departure times. Can
        be used if the status is a combination of the other values.
        (since SIRI 2.1)
    :cvar DISTRIBUTOR_WAIT_PROLONGED: An important function of
        connection protection is the ability to hold back a distributor
        VEHICLE (i.e. prolonged waiting) to allow passengers to transfer
        from delayed feeders. To achieve this a distributorWaitProlonged
        status shall be communicated back to the feeder VEHICLEs to
        inform the passengers about the new departure time of the
        distributor or even a willWait guarantee. (since SIRI 2.1)
    :cvar DEPARTURE_PLATFORM_CHANGED: Used to provide the passengers
        with information about a new departure platform of the
        distributor VEHICLE if the distributor changes its planned
        stopping position. (since SIRI 2.1)
    :cvar EXTRA_INTERCHANGE: Interchange is an addition to the plan.
        (since SIRI 2.1)
    :cvar CANCELLED: Interchange is a cancellation of an interchange in
        the plan. (since SIRI 2.1)
    :cvar FEEDER_ARRIVAL_CANCELLATION: Loss of the inbound connection
        indicates the cancellation of the visit (of the FeederJourney)
        to the FeederArrivalStop, or a severely delayed arrival. This
        can lead to the distributor VEHICLE abandoning the connection.
        Reasons for the loss of a feeder include (but are not limited
        to) the cancellation of the feeder VEHICLE, diversion/rerouting
        of the feeder VEHICLE, disruption of a line section or journey
        part of the feeder VEHICLE etc. (since SIRI 2.1)
    :cvar DISTRIBUTOR_DEPARTURE_CANCELLATION: Indicates the loss of an
        outbound connection, i.e., is used to signal the cancellation of
        the onward connection to the passengers in the feeder VEHICLEs.
        (since SIRI 2.1)
    :cvar STATUS_OF_CONENCTION_UNDECIDED: DEPRECATED since SIRI 2.1 -
        use statusOfConnectionUndecided instead
    """

    UNKNOWN = "unknown"
    CONNECTION = "connection"
    REPLACEMENT = "replacement"
    ALTERNATIVE = "alternative"
    CONNECTION_NOT_HELD = "connectionNotHeld"
    CONNECTION_HELD = "connectionHeld"
    STATUS_OF_CONNECTION_UNDECIDED = "statusOfConnectionUndecided"
    UNDEFINED_CROSS_REFERENCE_INFORMATION = (
        "undefinedCrossReferenceInformation"
    )
    CONNECTION_CHANGED = "connectionChanged"
    DISTRIBUTOR_WAIT_PROLONGED = "distributorWaitProlonged"
    DEPARTURE_PLATFORM_CHANGED = "departurePlatformChanged"
    EXTRA_INTERCHANGE = "extraInterchange"
    CANCELLED = "cancelled"
    FEEDER_ARRIVAL_CANCELLATION = "feederArrivalCancellation"
    DISTRIBUTOR_DEPARTURE_CANCELLATION = "distributorDepartureCancellation"
    STATUS_OF_CONENCTION_UNDECIDED = "statusOfConenctionUndecided"
