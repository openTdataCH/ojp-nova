from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class SelfDriveSubmodesOfTransportEnumeration(Enum):
    """
    Values for SelfDrive ModesOfTransport: TPEG pti_table_12.
    """
    PTI12_0 = "pti12_0"
    UNKNOWN = "unknown"
    PTI12_1 = "pti12_1"
    HIRE_CAR = "hireCar"
    PTI12_2 = "pti12_2"
    HIRE_VAN = "hireVan"
    PTI12_3 = "pti12_3"
    HIRE_MOTORBIKE = "hireMotorbike"
    PTI12_4 = "pti12_4"
    HIRE_CYCLE = "hireCycle"
    PTI12_5 = "pti12_5"
    ALL_HIRE_VEHICLES = "allHireVehicles"
    PTI12_255 = "pti12_255"
    UNDEFINED_HIRE_VEHICLE = "undefinedHireVehicle"
