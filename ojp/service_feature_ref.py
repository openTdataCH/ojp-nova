from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class ServiceFeatureRef:
    """Classification of service into arbitrary Service categories, e.g. school
    bus.

    SIRI provides a recommended set of values covering most usages,
    intended to be TPEG comnpatible. See the SIRI facilities packaged.
    """
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
