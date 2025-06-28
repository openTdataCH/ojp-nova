from dataclasses import dataclass, field
from typing import Optional

from ojp2.extensions_1 import Extensions1
from ojp2.installed_equipment_structure import InstalledEquipmentStructure
from ojp2.service_feature_ref_structure import ServiceFeatureRefStructure
from ojp2.validity_conditions_structure import ValidityConditionsStructure

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
        },
    )
    feature_refs: Optional["LocalServiceStructure.FeatureRefs"] = field(
        default=None,
        metadata={
            "name": "FeatureRefs",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
        },
    )
    extensions: Optional[Extensions1] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
        },
    )

    @dataclass
    class FeatureRefs:
        """
        :ivar feature_ref: Features of LOCAL SERVICe.
        """

        feature_ref: list[ServiceFeatureRefStructure] = field(
            default_factory=list,
            metadata={
                "name": "FeatureRef",
                "type": "Element",
                "namespace": "http://www.ifopt.org.uk/ifopt",
            },
        )
