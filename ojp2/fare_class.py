from dataclasses import dataclass, field

from ojp2.fare_class_enumeration import FareClassEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class FareClass:
    """Classification of FARE CLASSes.

    (since SIRI 2.1)
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: FareClassEnumeration = field(
        default=FareClassEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )
