from dataclasses import dataclass

from ojp2.product_category_ref_structure import ProductCategoryRefStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class ProductCategoryRef(ProductCategoryRefStructure):
    """Reference to a product category.

    Product categories should be defined once and used uniformly in all
    channels (e.g., NeTEx, SIRI, OJP).
    """

    class Meta:
        namespace = "http://www.vdv.de/ojp"
