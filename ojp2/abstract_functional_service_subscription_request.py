from dataclasses import dataclass

from ojp2.abstract_subscription_structure import AbstractSubscriptionStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class AbstractFunctionalServiceSubscriptionRequest(
    AbstractSubscriptionStructure
):
    """
    Subsititutable type for a SIRI Functional Service subscription request.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
