from dataclasses import dataclass, field
from typing import Optional

from ojp2.consequence_content_structure import ConsequenceContentStructure
from ojp2.defaulted_text_structure import DefaultedTextStructure
from ojp2.description_content_structure import DescriptionContentStructure
from ojp2.duration_content_structure import DurationContentStructure
from ojp2.image_structure import ImageStructure
from ojp2.info_link_structure_2 import InfoLinkStructure2
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
from ojp2.reason_content_structure import ReasonContentStructure
from ojp2.recommendation_content_structure import (
    RecommendationContentStructure,
)
from ojp2.remark_content_structure import RemarkContentStructure
from ojp2.summary_content_structure import SummaryContentStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class TextualContentStructure:
    """
    :ivar textual_content_size: Class of size, e.g. L (large), M
        (medium), S (small)
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
    :ivar summary_content: Content for summary of a passenger
        information action
    :ivar reason_content: Content for reason of a passenger information
        action
    :ivar description_content: Content for n descriptions of a passenger
        information action. For hiding / sorting descriptions in end
        devices, a description priority can be set.
    :ivar consequence_content: Content for n consequences of a passenger
        information action. For hiding / sorting descriptions in end
        devices, a consequence priority can be set.
    :ivar recommendation_content: Content for n recommendations of a
        passenger information action. For hiding / sorting descriptions
        in end devices, a recommendation priority can be set.
    :ivar duration_content: Content for the duration of a passenger
        information action.
    :ivar remark_content: Content for n remarks of a passenger
        information action, e,g, "For more information call xy". For
        hiding / sorting descriptions in end devices, a remark priority
        can be set.
    :ivar info_link: Hyperlinks to other resources associated with
        SITUATION.
    :ivar image: Any images associated with SITUATION.
    :ivar internal: for internal information only, not passenger
        relevant
    """

    textual_content_size: list[str] = field(
        default_factory=list,
        metadata={
            "name": "TextualContentSize",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "tokens": True,
        },
    )
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
    summary_content: Optional[SummaryContentStructure] = field(
        default=None,
        metadata={
            "name": "SummaryContent",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    reason_content: Optional[ReasonContentStructure] = field(
        default=None,
        metadata={
            "name": "ReasonContent",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    description_content: list[DescriptionContentStructure] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionContent",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    consequence_content: list[ConsequenceContentStructure] = field(
        default_factory=list,
        metadata={
            "name": "ConsequenceContent",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    recommendation_content: list[RecommendationContentStructure] = field(
        default_factory=list,
        metadata={
            "name": "RecommendationContent",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    duration_content: Optional[DurationContentStructure] = field(
        default=None,
        metadata={
            "name": "DurationContent",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    remark_content: list[RemarkContentStructure] = field(
        default_factory=list,
        metadata={
            "name": "RemarkContent",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    info_link: list[InfoLinkStructure2] = field(
        default_factory=list,
        metadata={
            "name": "InfoLink",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    image: list[ImageStructure] = field(
        default_factory=list,
        metadata={
            "name": "Image",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    internal: list[DefaultedTextStructure] = field(
        default_factory=list,
        metadata={
            "name": "Internal",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
