from dataclasses import dataclass, field
from typing import Optional

from ojp2.feature_id_ref_structure import FeatureIdRefStructure

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


@dataclass
class FeatureRefStructure1:
    """
    Type for reference to a FEATURE.

    :ivar feature_id_ref: Unique identfiier of referenced element, eg
        TOId.
    :ivar feature_type: Type for identifier of FEATURE.
    """

    class Meta:
        name = "FeatureRefStructure"

    feature_id_ref: Optional[FeatureIdRefStructure] = field(
        default=None,
        metadata={
            "name": "FeatureIdRef",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
            "required": True,
        },
    )
    feature_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "FeatureType",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
        },
    )
