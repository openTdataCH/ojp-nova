from dataclasses import dataclass
from ojp.natural_language_place_name_structure import NaturalLanguagePlaceNameStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class ViaName(NaturalLanguagePlaceNameStructure):
    """Names of VIA points, used to help identify the LINEfor example, Luton to
    Luton via Sutton.

    Currently 3 in VDV. Should only be included if the detail level was
    requested.
    """
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
