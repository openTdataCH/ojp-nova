from dataclasses import dataclass
from ojp.natural_language_place_name_structure import NaturalLanguagePlaceNameStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class OriginName(NaturalLanguagePlaceNameStructure):
    """
    The name of the origin of the journey; used to help identify the VEHICLE
    JOURNEY on arrival boards.
    """
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
