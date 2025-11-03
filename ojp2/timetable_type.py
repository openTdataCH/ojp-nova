from dataclasses import dataclass, field

from ojp2.timetable_type_enumeration import TimetableTypeEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class TimetableType:
    """Timetable type - TPEG Pti033."""

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: TimetableTypeEnumeration = field(
        default=TimetableTypeEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )
