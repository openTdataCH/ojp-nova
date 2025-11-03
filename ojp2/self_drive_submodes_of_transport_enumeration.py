from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class SelfDriveSubmodesOfTransportEnumeration(Enum):
    """Values for SelfDrive ModesOfTransport: TPEG pti_table_12.

    :cvar UNKNOWN: Submode of transport is not known to the source
        system.
    :cvar UNDEFINED: (SIRI 2.1) - see also 'undefinedHireVehicle'.
    :cvar HIRE_CAR:
    :cvar HIRE_VAN:
    :cvar HIRE_MOTORBIKE:
    :cvar HIRE_CYCLE:
    :cvar ALL_HIRE_VEHICLES:
    :cvar UNDEFINED_HIRE_VEHICLE: Submode of transport is not supported
        in this list.
    :cvar PTI12_0: DEPRECATED since SIRI 2.1
    :cvar PTI12_1: DEPRECATED since SIRI 2.1
    :cvar PTI12_2: DEPRECATED since SIRI 2.1
    :cvar PTI12_3: DEPRECATED since SIRI 2.1
    :cvar PTI12_4: DEPRECATED since SIRI 2.1
    :cvar PTI12_5: DEPRECATED since SIRI 2.1
    :cvar PTI12_255: DEPRECATED since SIRI 2.1
    """

    UNKNOWN = "unknown"
    UNDEFINED = "undefined"
    HIRE_CAR = "hireCar"
    HIRE_VAN = "hireVan"
    HIRE_MOTORBIKE = "hireMotorbike"
    HIRE_CYCLE = "hireCycle"
    ALL_HIRE_VEHICLES = "allHireVehicles"
    UNDEFINED_HIRE_VEHICLE = "undefinedHireVehicle"
    PTI12_0 = "pti12_0"
    PTI12_1 = "pti12_1"
    PTI12_2 = "pti12_2"
    PTI12_3 = "pti12_3"
    PTI12_4 = "pti12_4"
    PTI12_5 = "pti12_5"
    PTI12_255 = "pti12_255"
