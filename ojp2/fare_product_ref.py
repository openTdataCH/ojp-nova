from dataclasses import dataclass

from ojp2.fare_product_ref_structure import FareProductRefStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class FareProductRef(FareProductRefStructure):
    """
    Reference to a FareProduct.
    """

    class Meta:
        namespace = "http://www.vdv.de/ojp"
