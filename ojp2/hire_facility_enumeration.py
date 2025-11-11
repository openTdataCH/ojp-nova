from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class HireFacilityEnumeration(Enum):
    """
    Values for Hire Facility.
    """

    UNKNOWN = "unknown"
    CAR_HIRE = "carHire"
    MOTOR_CYCLE_HIRE = "motorCycleHire"
    CYCLE_HIRE = "cycleHire"
    TAXI = "taxi"
    RECREATION_DEVICE_HIRE = "recreationDeviceHire"
