from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class RelatedToEnumeration(Enum):
    """
    Values for Type of Source.
    """
    CAUSE = "cause"
    EFFECT = "effect"
    UPDATE = "update"
    SUPERCEDES = "supercedes"
    SUPERCEDED_BY = "supercededBy"
    ASSOCIATED = "associated"
