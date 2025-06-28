from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class FeatureRefStructure2:
    """
    Type for reference to a Feature Code.
    """

    class Meta:
        name = "FeatureRefStructure"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
