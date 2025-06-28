from dataclasses import dataclass, field

from ojp2.info_link import InfoLink

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


@dataclass
class InfoLinksStructure:
    """
    Type for collection of info links.
    """

    info_link: list[InfoLink] = field(
        default_factory=list,
        metadata={
            "name": "InfoLink",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
            "min_occurs": 1,
        },
    )
