from dataclasses import dataclass, field
from ojp.day_type_enumeration import DayTypeEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class DayType:
    """
    Tpeg DAY TYPE pti_table 34.
    """
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: DayTypeEnumeration = field(
        default=DayTypeEnumeration.EVERY_DAY,
        metadata={
            "required": True,
        }
    )
