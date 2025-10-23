from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class FeatureRef:
    """Classification of facilities into arbitrary Facility categories.

    SIRI provides a recommended set of values covering most usages. SIRI
    provides a recommended set of values covering most usages, intended
    to be TPEG comnpatible. See the SIRI facilities packaged.
    """
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
