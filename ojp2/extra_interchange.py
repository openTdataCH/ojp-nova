from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class ExtraInterchange:
    """Whether this interchange is an addition to the plan.

    Can only be used when both participants recognise the same schedule
    version. If omitted, defaults to 'false': the interchange is not an
    addition. (since SIRI 2.1)
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: bool = field(
        default=False,
        metadata={
            "required": True,
        },
    )
