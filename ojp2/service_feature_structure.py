from dataclasses import dataclass, field
from typing import Optional

from ojp2.natural_language_string_structure import (
    NaturalLanguageStringStructure,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class ServiceFeatureStructure:
    """
    Type for Service Feature description.

    :ivar service_feature_code: Identifier of classification. SIRI
        provides a recommended set of values covering most usages,
        intended to be TPEG compatible. See the SIRI facilities
        packaged.
    :ivar name: Name of classification.  (Unbounded since SIRI 2.0)
    :ivar icon: Icon associated with feature.
    """

    service_feature_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ServiceFeatureCode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    name: list[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_occurs": 1,
        },
    )
    icon: Optional[str] = field(
        default=None,
        metadata={
            "name": "Icon",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
