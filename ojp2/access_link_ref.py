from dataclasses import dataclass

from ojp2.access_link_ref_structure import AccessLinkRefStructure

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


@dataclass
class AccessLinkRef(AccessLinkRefStructure):
    """
    Reference to an ACCESS link.
    """

    class Meta:
        namespace = "http://www.ifopt.org.uk/ifopt"
