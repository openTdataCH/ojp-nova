from dataclasses import dataclass, field
from typing import Optional
from ojp.international_text_structure import InternationalTextStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class ProductCategoryStructure2:
    """Product category based on NeTEx/SIRI.

    A product category is a classification for VEHICLE JOURNEYs to
    express some common properties of journeys for marketing and fare
    products.

    :ivar name: Full name of this product category, e.g. "Autoreisezug"
        in Switzerland or "Dampfschiff"
    :ivar short_name: Short name or acronym of the product category,
        likely to be published, e.g. "BAV", "ARZ", "TGV". The product
        category is more important for publication in Switzerland than
        Mode / Submode.
    :ivar product_category_ref: A reference to the product category.
        This is the internal code used within the reference frameworks
        (NeTEx, SIRI). It is usually not displayed, but interpreted by
        the technical system, e.g. "ch:1:TypeOfProductCategory:ARZ"
        (Autoreisezug in Switzerland) or
        "ch:1:TypeOfProductCategory:BAV".
    """
    class Meta:
        name = "ProductCategoryStructure"

    name: Optional[InternationalTextStructure] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    short_name: Optional[InternationalTextStructure] = field(
        default=None,
        metadata={
            "name": "ShortName",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    product_category_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProductCategoryRef",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
