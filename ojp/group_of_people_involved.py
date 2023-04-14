from dataclasses import dataclass, field
from typing import Optional
from ojp.extension_type import ExtensionType
from ojp.injury_status_type_enum import InjuryStatusTypeEnum
from ojp.involvement_roles_enum import InvolvementRolesEnum
from ojp.person_category_enum import PersonCategoryEnum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class GroupOfPeopleInvolved:
    number_of_people: Optional[int] = field(
        default=None,
        metadata={
            "name": "numberOfPeople",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
    injury_status: Optional[InjuryStatusTypeEnum] = field(
        default=None,
        metadata={
            "name": "injuryStatus",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
    involvement_role: Optional[InvolvementRolesEnum] = field(
        default=None,
        metadata={
            "name": "involvementRole",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
    category_of_people_involved: Optional[PersonCategoryEnum] = field(
        default=None,
        metadata={
            "name": "categoryOfPeopleInvolved",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
    group_of_people_involved_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "groupOfPeopleInvolvedExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
