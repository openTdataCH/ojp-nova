from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class PredictionInaccurate:
    """Whether the prediction for a specific stop or the whole journey is
    considered to be of a useful accuracy or not.

    Default is 'false', i.e. prediction is considered to be accurate. If
    prediction is degraded, e.g. because of a situation,
    PredictionInaccurate is used to indicate a lowered quality of data.
    Inherited property. PredictionInaccurate can be used in combination
    with InCongestion, but is more general.
    """
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: bool = field(
        default=False,
        metadata={
            "required": True,
        }
    )
