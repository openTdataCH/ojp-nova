from dataclasses import dataclass, field
from ojp.timetable_type_enumeration import TimetableTypeEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class TimetableType:
    """Timetable type - Tpeg pti33."""
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: TimetableTypeEnumeration = field(
        default=TimetableTypeEnumeration.UNKNOWN,
        metadata={
            "required": True,
        }
    )
