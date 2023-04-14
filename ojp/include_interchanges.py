from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class IncludeInterchanges:
    """Whether SERVICE JOURNEY INTERCHANGE data is to be transmitted or not.

    Default is 'true'. (since SIRI 2.1)
    """
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: bool = field(
        default=True,
        metadata={
            "required": True,
        }
    )
