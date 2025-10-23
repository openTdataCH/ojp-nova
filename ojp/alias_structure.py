from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


@dataclass
class AliasStructure:
    """
    Alternative Private Code.

    :ivar private_code: Alternative identifier.
    :ivar identifier_type: Type of Identifier.
    """
    private_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrivateCode",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
            "required": True,
        }
    )
    identifier_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "IdentifierType",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
        }
    )
