from dataclasses import dataclass, field
from typing import Optional

from ojp2.line_information_problem_type_enumeration import (
    LineInformationProblemTypeEnumeration,
)

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class LineInformationProblemType:
    class Meta:
        namespace = "http://www.vdv.de/ojp"

    value: Optional[LineInformationProblemTypeEnumeration] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
