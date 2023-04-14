from dataclasses import dataclass, field
from typing import List, Optional
from ojp.natural_language_string_structure import NaturalLanguageStringStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class VehicleFeaturesStructure:
    """
    Type for description of feature of VEHICLE.

    :ivar vehicle_feature_code: Identifier of feature of VEHICLE. SIRI
        provides a recommended set of values covering most usages,
        intended to be TPEG compatible. See the SIRI facilities
        packaged.
    :ivar name: Name of feature of VEHICLE.  (Unbounded since SIRI 2.0)
    :ivar icon: Icon used to represent feature of VEHICLE.
    """
    vehicle_feature_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "VehicleFeatureCode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    name: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_occurs": 1,
        }
    )
    icon: Optional[str] = field(
        default=None,
        metadata={
            "name": "Icon",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
