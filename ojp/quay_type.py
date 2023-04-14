from dataclasses import dataclass, field
from typing import Optional
from ojp.type_of_nested_quay_enumeration import TypeOfNestedQuayEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class QuayType:
    """Indicates the type of a nested QUAY in case of detailed STOP PLACE
    models.

    A QUAY may be part of a group of QUAYs, or may be divided into
    sectors, i.e., smaller sub-QUAYs. (since SIRI 2.1)
    """
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: Optional[TypeOfNestedQuayEnumeration] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
