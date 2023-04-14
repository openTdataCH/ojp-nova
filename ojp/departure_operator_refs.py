from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class DepartureOperatorRefs:
    """OPERATORs of service for departure and onwards.

    May change from that for arrival. (since SIRI 2.0).
    """
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
