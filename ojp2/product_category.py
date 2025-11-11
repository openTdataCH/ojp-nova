from dataclasses import dataclass

from ojp2.product_category_structure_1 import ProductCategoryStructure1

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class ProductCategory(ProductCategoryStructure1):
    """
    Category for classification of a journey as a Product.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
