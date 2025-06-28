from dataclasses import dataclass, field
from typing import Optional

from ojp2.manual_action import ManualAction
from ojp2.notify_by_email_action import NotifyByEmailAction
from ojp2.notify_by_pager_action import NotifyByPagerAction
from ojp2.notify_by_sms_action import NotifyBySmsAction
from ojp2.notify_user_action import NotifyUserAction
from ojp2.publish_to_alerts_action import PublishToAlertsAction
from ojp2.publish_to_display_action import PublishToDisplayAction
from ojp2.publish_to_mobile_action import PublishToMobileAction
from ojp2.publish_to_tv_action import PublishToTvAction
from ojp2.publish_to_web_action import PublishToWebAction
from ojp2.publishing_action_structure import PublishingActionStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class ActionsStructure:
    """
    Type for list of actions.

    :ivar publish_to_web_action:
    :ivar publish_to_mobile_action:
    :ivar publish_to_tv_action:
    :ivar publish_to_alerts_action:
    :ivar publish_to_display_action:
    :ivar manual_action:
    :ivar notify_by_email_action:
    :ivar notify_by_sms_action:
    :ivar notify_by_pager_action:
    :ivar notify_user_action:
    :ivar publishing_action: Description of the whole action to be
        published. &gt;SIRI 2.0
    :ivar extensions: Extension point.
    """

    publish_to_web_action: list[PublishToWebAction] = field(
        default_factory=list,
        metadata={
            "name": "PublishToWebAction",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    publish_to_mobile_action: list[PublishToMobileAction] = field(
        default_factory=list,
        metadata={
            "name": "PublishToMobileAction",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    publish_to_tv_action: list[PublishToTvAction] = field(
        default_factory=list,
        metadata={
            "name": "PublishToTvAction",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    publish_to_alerts_action: list[PublishToAlertsAction] = field(
        default_factory=list,
        metadata={
            "name": "PublishToAlertsAction",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    publish_to_display_action: list[PublishToDisplayAction] = field(
        default_factory=list,
        metadata={
            "name": "PublishToDisplayAction",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    manual_action: list[ManualAction] = field(
        default_factory=list,
        metadata={
            "name": "ManualAction",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    notify_by_email_action: list[NotifyByEmailAction] = field(
        default_factory=list,
        metadata={
            "name": "NotifyByEmailAction",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    notify_by_sms_action: list[NotifyBySmsAction] = field(
        default_factory=list,
        metadata={
            "name": "NotifyBySmsAction",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    notify_by_pager_action: list[NotifyByPagerAction] = field(
        default_factory=list,
        metadata={
            "name": "NotifyByPagerAction",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    notify_user_action: list[NotifyUserAction] = field(
        default_factory=list,
        metadata={
            "name": "NotifyUserAction",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    publishing_action: list[PublishingActionStructure] = field(
        default_factory=list,
        metadata={
            "name": "PublishingAction",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    extensions: Optional[object] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
