from dataclasses import dataclass, field
from typing import Optional

from ojp2.feature_ref_structure_1 import FeatureRefStructure1

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


@dataclass
class AbstractProjection:
    """
    :ivar features: GIS Features that this element projects onto.
    """

    features: Optional["AbstractProjection.Features"] = field(
        default=None,
        metadata={
            "name": "Features",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
        },
    )

    @dataclass
    class Features:
        """
        :ivar gis_feature_ref: Identifier of FEATURE in a GIS data
            system.
        """

        gis_feature_ref: list[FeatureRefStructure1] = field(
            default_factory=list,
            metadata={
                "name": "GisFeatureRef",
                "type": "Element",
                "namespace": "http://www.ifopt.org.uk/ifopt",
                "min_occurs": 1,
            },
        )
