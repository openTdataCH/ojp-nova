from dataclasses import dataclass

from ojp2.info_link_structure_1 import InfoLinkStructure1

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


@dataclass
class InfoLink(InfoLinkStructure1):
    """
    Info Link .
    """

    class Meta:
        namespace = "http://www.ifopt.org.uk/ifopt"
