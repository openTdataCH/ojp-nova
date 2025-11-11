from dataclasses import dataclass

from ojp2.facility_condition_structure import FacilityConditionStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class FacilityConditionElement(FacilityConditionStructure):
    """
    Description of any change concerning a MONITORED FACILITY New structure defined
    in SIRI XSD 1.1 for Facilities Management.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
