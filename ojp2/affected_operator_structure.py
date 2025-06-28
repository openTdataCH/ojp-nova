from dataclasses import dataclass, field
from typing import Optional

from ojp2.extensions_2 import Extensions2
from ojp2.natural_language_string_structure import (
    NaturalLanguageStringStructure,
)
from ojp2.operational_unit_ref_structure import OperationalUnitRefStructure
from ojp2.operator_ref_structure import OperatorRefStructure

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

    operator_ref: Optional[OperatorRefStructure] = field(
        default=None,
        metadata={
            "name": "OperatorRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    operator_name: list[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "OperatorName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    operator_short_name: list[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "OperatorShortName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    operational_unit_ref: list[OperationalUnitRefStructure] = field(
        default_factory=list,
        metadata={
            "name": "OperationalUnitRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    extensions: Optional[Extensions2] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
