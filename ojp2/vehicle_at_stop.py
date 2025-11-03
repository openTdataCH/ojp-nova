from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class VehicleAtStop:
    """Whether VEHICLE is currently at stop.

    Default is false (xml  default added from SIRI 2.0)
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: bool = field(
        default=False,
        metadata={
            "required": True,
        },
    )
