from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class ExtensionsStructure:
    """Type for Extensions to schema.

    Wraps an 'any' tag to ensure decidability.

    :ivar any_element: Placeholder for user extensions.
    """

    any_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
