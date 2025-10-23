from dataclasses import dataclass, field
from typing import List, Optional
from ojp.extensions_2 import Extensions2
from ojp.installed_equipment_structure import InstalledEquipmentStructure
from ojp.validity_conditions_structure import ValidityConditionsStructure

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


@dataclass
class LocalServiceStructure(InstalledEquipmentStructure):
    """
    Type for LOCAL SERVICE.

    :ivar validity_conditions: Conditison governing availability of
        serevice.
    :ivar feature_refs: Classification of features.
    :ivar extensions:
    """
    validity_conditions: Optional[ValidityConditionsStructure] = field(
        default=None,
        metadata={
            "name": "ValidityConditions",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
        }
    )
    feature_refs: Optional["LocalServiceStructure.FeatureRefs"] = field(
        default=None,
        metadata={
            "name": "FeatureRefs",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
        }
    )
    extensions: Optional[Extensions2] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
        }
    )

    @dataclass
    class FeatureRefs:
        """
        :ivar feature_ref: Features of LOCAL SERVICe.
        """
        feature_ref: List[str] = field(
            default_factory=list,
            metadata={
                "name": "FeatureRef",
                "type": "Element",
                "namespace": "http://www.ifopt.org.uk/ifopt",
            }
        )
