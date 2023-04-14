from dataclasses import dataclass
from ojp.curve_property_type import CurvePropertyType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class CurveProperty(CurvePropertyType):
    """This property element either references a curve via the XLink-attributes
    or contains the curve element.

    curveProperty is the predefined property which may be used by GML
    Application Schemas whenever a GML feature has a property with a
    value that is substitutable for AbstractCurve.
    """
    class Meta:
        name = "curveProperty"
        namespace = "http://www.opengis.net/gml/3.2"
