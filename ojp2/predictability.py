from dataclasses import dataclass, field
from typing import Optional

from ojp2.predictability_enumeration import PredictabilityEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class Predictability:
    """
    Classification of Predictability status.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: Optional[PredictabilityEnumeration] = field(default=None)
