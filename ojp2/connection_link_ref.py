from dataclasses import dataclass

from ojp2.connection_link_ref_structure import ConnectionLinkRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class ConnectionLinkRef(ConnectionLinkRefStructure):
    """
    Reference to a CONNECTION link.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
