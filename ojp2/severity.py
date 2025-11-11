from dataclasses import dataclass, field

from ojp2.severity_enumeration import SeverityEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class Severity:
    """Severity of Incident - TPEG Pti26. Default is 'normal'."""

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: SeverityEnumeration = field(
        default=SeverityEnumeration.NORMAL,
        metadata={
            "required": True,
        },
    )
