from dataclasses import dataclass
from ojp.reference_type import ReferenceType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class DescriptionReference(ReferenceType):
    """The value of this property is a remote text description of the object.

    The xlink:href attribute of the gml:descriptionReference property
    references the external description.
    """
    class Meta:
        name = "descriptionReference"
        namespace = "http://www.opengis.net/gml/3.2"
