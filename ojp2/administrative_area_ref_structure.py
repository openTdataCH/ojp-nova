from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


@dataclass
class AdministrativeAreaRefStructure:
    """
    Type for a reference to an ADMINISTRATIVE ZONE.
    """

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"[0-9]{3}",
        },
    )
