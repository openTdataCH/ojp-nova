from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class SiteRefStructure:
    """
    Reference to a SITE.
    """

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
