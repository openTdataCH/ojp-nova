from dataclasses import dataclass

from ojp2.dated_call_structure import DatedCallStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class DatedCall(DatedCallStructure):
    """
    Complete sequence of stops along the route path, in calling order.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
