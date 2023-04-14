from dataclasses import dataclass, field
from typing import List, Optional
from ojp.consequence_content_structure import ConsequenceContentStructure
from ojp.defaulted_text_structure import DefaultedTextStructure
from ojp.description_content_structure import DescriptionContentStructure
from ojp.duration_content_structure import DurationContentStructure
from ojp.image_structure import ImageStructure
from ojp.info_link_structure import InfoLinkStructure
from ojp.manual_action import ManualAction
from ojp.notify_by_email_action import NotifyByEmailAction
from ojp.notify_by_pager_action import NotifyByPagerAction
from ojp.notify_by_sms_action import NotifyBySmsAction
from ojp.notify_user_action import NotifyUserAction
from ojp.publish_to_alerts_action import PublishToAlertsAction
from ojp.publish_to_display_action import PublishToDisplayAction
from ojp.publish_to_mobile_action import PublishToMobileAction
from ojp.publish_to_tv_action import PublishToTvAction
from ojp.publish_to_web_action import PublishToWebAction
from ojp.reason_content_structure import ReasonContentStructure
from ojp.recommendation_content_structure import RecommendationContentStructure
from ojp.remark_content_structure import RemarkContentStructure
from ojp.summary_content_structure import SummaryContentStructure

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
    textual_content_size: List[str] = field(
        default_factory=list,
        metadata={
            "name": "TextualContentSize",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "tokens": True,
        }
    )
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
    publish_to_tv_action: List[PublishToTvAction] = field(
        default_factory=list,
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
    publish_to_display_action: List[PublishToDisplayAction] = field(
        default_factory=list,
        metadata={
            "name": "PublishToDisplayAction",
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
    notify_by_sms_action: List[NotifyBySmsAction] = field(
        default_factory=list,
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
    summary_content: Optional[SummaryContentStructure] = field(
        default=None,
        metadata={
            "name": "SummaryContent",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    reason_content: Optional[ReasonContentStructure] = field(
        default=None,
        metadata={
            "name": "ReasonContent",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    description_content: List[DescriptionContentStructure] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionContent",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    consequence_content: List[ConsequenceContentStructure] = field(
        default_factory=list,
        metadata={
            "name": "ConsequenceContent",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    recommendation_content: List[RecommendationContentStructure] = field(
        default_factory=list,
        metadata={
            "name": "RecommendationContent",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    duration_content: Optional[DurationContentStructure] = field(
        default=None,
        metadata={
            "name": "DurationContent",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    remark_content: List[RemarkContentStructure] = field(
        default_factory=list,
        metadata={
            "name": "RemarkContent",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    info_link: List[InfoLinkStructure] = field(
        default_factory=list,
        metadata={
            "name": "InfoLink",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    image: List[ImageStructure] = field(
        default_factory=list,
        metadata={
            "name": "Image",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    internal: List[DefaultedTextStructure] = field(
        default_factory=list,
        metadata={
            "name": "Internal",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
