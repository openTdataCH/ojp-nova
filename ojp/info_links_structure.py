from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


@dataclass
class InfoLinksStructure:
    """
    Type for collection of info links.
    """
    info_link: List[str] = field(
        default_factory=list,
        metadata={
            "name": "InfoLink",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
            "min_occurs": 1,
        }
    )
