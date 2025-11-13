from dataclasses import dataclass, field

from ojp2.day_type_enumeration import DayTypeEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class DayType:
    """Day on which a SITUATION may apply - TPEG Pti34 DayType"""

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: DayTypeEnumeration = field(
        default=DayTypeEnumeration.EVERY_DAY,
        metadata={
            "required": True,
        },
    )
