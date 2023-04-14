from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class ProductCategoryRef:
    """Reference to a product category.

    Product categories should be defined once and used uniformly in all
    channels (e.g. NeTEx, SIRI, OJP).
    """
    class Meta:
        namespace = "http://www.vdv.de/ojp"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
