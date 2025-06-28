from dataclasses import dataclass

from ojp2.facility_change_structure import FacilityChangeStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class FacilityChangeElement(FacilityChangeStructure):
    """A change to the availaibility of EQUIPMENT.

    Basic structure defined in the first 1.0 SIRI XSd.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
