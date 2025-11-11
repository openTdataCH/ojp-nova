from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class IncludeTranslations:
    """Whether additional translations of text names are to be included in
    elements.

    If 'false', then only one element should be returned.  Default is
    'false'. Where multiple values are returned The first element
    returned will be used as the default value.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: bool = field(
        default=False,
        metadata={
            "required": True,
        },
    )
