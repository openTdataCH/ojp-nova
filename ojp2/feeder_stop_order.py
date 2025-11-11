from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class FeederStopOrder:
    """For implementations in which the overall order is not defined by VISIT
    NUMBER, i.e. in case VisitNumberIsOrder is set to false, ORDER can be used to
    associate the stop order instead.

    ORDER is also used together with VISIT NUMBER in scenarios where an
    extra CALL is inserted as a result of despatching alterations.
    Because such an extra CALL may have the same VisitNumber as another
    (cancelled) CALL, the STOP ORDER is needed. (since SIRI 2.1)
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
