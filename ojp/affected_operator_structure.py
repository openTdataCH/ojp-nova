from dataclasses import dataclass, field
from typing import List, Optional
from ojp.extensions_1 import Extensions1
from ojp.natural_language_string_structure import NaturalLanguageStringStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class AffectedOperatorStructure:
    """
    Type for Annotated reference to an OPERATOR affected by a SITUATION.

    :ivar operator_ref: Reference to an OPERATOR.
    :ivar operator_name: Public Name of OPERATOR. Can be derived from
        OperatorRef.  (Unbounded since SIRI 2.0)
    :ivar operator_short_name: Short Name for OPERATOR. Can be derived
        from OperatorRef.  (Unbounded since SIRI 2.0)
    :ivar operational_unit_ref: OPERATIONAL UNIT responsible for
        managing services.
    :ivar extensions:
    """
    operator_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "OperatorRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    operator_name: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "OperatorName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    operator_short_name: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "OperatorShortName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    operational_unit_ref: List[str] = field(
        default_factory=list,
        metadata={
            "name": "OperationalUnitRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    extensions: Optional[Extensions1] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
