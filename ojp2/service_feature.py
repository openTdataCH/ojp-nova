from dataclasses import dataclass

from ojp2.service_feature_structure import ServiceFeatureStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class ServiceFeature(ServiceFeatureStructure):
    """
    Service Feature description.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
