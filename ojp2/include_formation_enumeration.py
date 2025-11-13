from enum import Enum

__NAMESPACE__ = "http://www.vdv.de/ojp"


class IncludeFormationEnumeration(Enum):
    """
    Possible values how to include formations in the basic filters.

    :cvar NONE:
    :cvar VEHICLEFEATURE: The response should include VehicleFeatureRef
        (from SIRI).
    :cvar FULL: Besides VehicleFeatureRefs also Formation,
        ArrivalFormation and DepartureFormation can be used. This is the
        full SIRI formation experience. Refer to the SIRI documentation
        for details. The specification document and the examples may
        show simpler ways of doing things. For full accessibility many
        features are needed. It is recommended to always also use
        VehicleFeatureRef (for people not processing SIRI formation and
        because buses and the like don't need Formation in most cases).
    """

    NONE = "none"
    VEHICLEFEATURE = "vehiclefeature"
    FULL = "full"
