from dataclasses import dataclass, field

from ojp2.report_type_enumeration import ReportTypeEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class ReportType:
    """Scope of incident - TPEG Pti27 ReportType"""

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: ReportTypeEnumeration = field(
        default=ReportTypeEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )
