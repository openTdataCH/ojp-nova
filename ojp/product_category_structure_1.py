from dataclasses import dataclass, field
from typing import List, Optional
from ojp.natural_language_string_structure import NaturalLanguageStringStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class ProductCategoryStructure1:
    """
    Type for TYPE OF PRODUCT CATEGORY description.

    :ivar product_category_code: Identifier of TYPE OF PRODUCT CATEGORY
        classification. SIRI provides a recommended set of values
        covering most usages, intended to be TPEG compatible. See the
        SIRI facilities packaged.
    :ivar name: Name of classification  (Unbounded since SIRI 2.0)
    :ivar icon: Icon used to represent TYPE OF PRODUCT CATEGORY.
    """
    class Meta:
        name = "ProductCategoryStructure"

    product_category_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProductCategoryCode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    name: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_occurs": 1,
        }
    )
    icon: Optional[str] = field(
        default=None,
        metadata={
            "name": "Icon",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
