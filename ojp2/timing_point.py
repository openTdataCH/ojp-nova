from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class TimingPoint:
    """Whether the stop is a TIMING POINT.

    Times for stops that are not timing points are sometimes
    interpolated crudely from the timing points, and may represent a
    lower level of accuracy. Default is 'true'.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: bool = field(
        default=True,
        metadata={
            "required": True,
        },
    )
