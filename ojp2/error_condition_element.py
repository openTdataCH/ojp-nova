from dataclasses import dataclass

from ojp2.error_condition_element_structure import (
    ErrorConditionElementStructure,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class ErrorConditionElement(ErrorConditionElementStructure):
    """
    Element fror an erroc condition  (for use in WSDL.)
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
