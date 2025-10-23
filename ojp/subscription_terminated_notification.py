from dataclasses import dataclass
from ojp.subscription_terminated_notification_structure import SubscriptionTerminatedNotificationStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class SubscriptionTerminatedNotification(SubscriptionTerminatedNotificationStructure):
    """
    Notification from Subscriber to Subscription Manager to terminate a
    subscription.
    """
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
