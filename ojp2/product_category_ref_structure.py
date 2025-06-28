from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class ProductCategoryRefStructure:
    """
    Type for reference to a TYPE OF PRODUCT CATEGORY.
    """

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
