from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


@dataclass
class FeatureIdRefStructure:
    """
    Type for reference to a GIS FEATURe.
    """

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
