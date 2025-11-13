from dataclasses import dataclass

from ojp2.service_feature_ref_structure import ServiceFeatureRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class ServiceFeatureRef(ServiceFeatureRefStructure):
    """Classification of service into arbitrary Service categories, e.g. school
    bus.

    SIRI provides a recommended set of values covering most usages,
    intended to be TPEG comnpatible. See the SIRI facilities packaged.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
