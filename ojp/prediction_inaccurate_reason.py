from dataclasses import dataclass, field
from typing import Optional
from ojp.prediction_inaccurate_reason_enumeration import PredictionInaccurateReasonEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class PredictionInaccurateReason:
    """Can be used to inform the passenger about the reason for a change of the
    prediction (in)accuracy in case PredictionInaccurate is set to 'true'.

    (since SIRI 2.1)
    """
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: Optional[PredictionInaccurateReasonEnumeration] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
