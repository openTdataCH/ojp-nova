from dataclasses import dataclass, field
from typing import List
from ojp.fare_class_enumeration import FareClassEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class FareClasses:
    """List of FARE CLASSes.

    (since SIRI 2.1)
    """
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: List[FareClassEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        }
    )
