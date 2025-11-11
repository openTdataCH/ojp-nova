from dataclasses import dataclass

from ojp2.vehicle_features_structure import VehicleFeaturesStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class VehicleFeature(VehicleFeaturesStructure):
    """
    Vehicle Feature description.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
