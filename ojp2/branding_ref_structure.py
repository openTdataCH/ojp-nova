from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class BrandingRefStructure:
    """Type for reference to a BRANDING.

    (since SIRI 2.1)
    """

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
