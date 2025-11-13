from dataclasses import dataclass

from ojp2.feature_ref_structure_2 import FeatureRefStructure2

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class FeatureRef(FeatureRefStructure2):
    """Classification of facilities into arbitrary Facility categories.

    SIRI provides a recommended set of values covering most usages. SIRI
    provides a recommended set of values covering most usages, intended
    to be TPEG comnpatible. See the SIRI facilities packaged.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
