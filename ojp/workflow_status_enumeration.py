from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class WorkflowStatusEnumeration(Enum):
    """
    Values for Entry Status.
    """
    DRAFT = "draft"
    APPROVED_DRAFT = "approvedDraft"
    OPEN = "open"
    PUBLISHED = "published"
    CLOSING = "closing"
    CLOSED = "closed"
