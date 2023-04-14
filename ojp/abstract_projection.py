from dataclasses import dataclass, field
from typing import List, Optional
from ojp.feature_ref_structure import FeatureRefStructure

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
        }
    )

    @dataclass
    class Features:
        """
        :ivar gis_feature_ref: Identifier of FEATURE in a GIS data
            system.
        """
        gis_feature_ref: List[FeatureRefStructure] = field(
            default_factory=list,
            metadata={
                "name": "GisFeatureRef",
                "type": "Element",
                "namespace": "http://www.ifopt.org.uk/ifopt",
                "min_occurs": 1,
            }
        )
