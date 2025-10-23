from dataclasses import dataclass, field
from typing import List, Optional
from ojp.manual_action import ManualAction
from ojp.notify_by_email_action import NotifyByEmailAction
from ojp.notify_by_pager_action import NotifyByPagerAction
from ojp.notify_by_sms_action import NotifyBySmsAction
from ojp.notify_user_action import NotifyUserAction
from ojp.publish_to_alerts_action import PublishToAlertsAction
from ojp.publish_to_mobile_action import PublishToMobileAction
from ojp.publish_to_tv_action import PublishToTvAction
from ojp.publish_to_web_action import PublishToWebAction

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class ActionsStructure:
    """
    Type for list of actions.

    :ivar publish_to_web_action:
    :ivar publish_to_mobile_action:
    :ivar publish_to_tv_action:
    :ivar publish_to_alerts_action:
    :ivar manual_action:
    :ivar notify_by_email_action:
    :ivar notify_by_sms_action:
    :ivar notify_by_pager_action:
    :ivar notify_user_action:
    :ivar extensions: Extension point.
    """
    publish_to_web_action: List[PublishToWebAction] = field(
        default_factory=list,
        metadata={
            "name": "PublishToWebAction",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    publish_to_mobile_action: List[PublishToMobileAction] = field(
        default_factory=list,
        metadata={
            "name": "PublishToMobileAction",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    publish_to_tv_action: Optional[PublishToTvAction] = field(
        default=None,
        metadata={
            "name": "PublishToTvAction",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    publish_to_alerts_action: List[PublishToAlertsAction] = field(
        default_factory=list,
        metadata={
            "name": "PublishToAlertsAction",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    manual_action: List[ManualAction] = field(
        default_factory=list,
        metadata={
            "name": "ManualAction",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    notify_by_email_action: List[NotifyByEmailAction] = field(
        default_factory=list,
        metadata={
            "name": "NotifyByEmailAction",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    notify_by_sms_action: Optional[NotifyBySmsAction] = field(
        default=None,
        metadata={
            "name": "NotifyBySmsAction",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    notify_by_pager_action: List[NotifyByPagerAction] = field(
        default_factory=list,
        metadata={
            "name": "NotifyByPagerAction",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    notify_user_action: List[NotifyUserAction] = field(
        default_factory=list,
        metadata={
            "name": "NotifyUserAction",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    extensions: Optional[object] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
