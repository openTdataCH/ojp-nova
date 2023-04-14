from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class AssociationName:
    class Meta:
        name = "associationName"
        namespace = "http://www.opengis.net/gml/3.2"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
