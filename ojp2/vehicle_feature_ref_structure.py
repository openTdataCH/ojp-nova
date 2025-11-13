from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class VehicleFeatureRefStructure:
    """Type for reference to a Vehicle Feature Code.

    SIRI provides a recommended set of values covering most usages,
    intended to be TPEG comnpatible. See the SIRI facilities packaged.
    """

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
