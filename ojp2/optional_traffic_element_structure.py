from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from ojp2.cause import Cause
from ojp2.comment import Comment
from ojp2.extension_type import ExtensionType
from ojp2.group_of_locations import GroupOfLocations
from ojp2.impact import Impact
from ojp2.management import Management
from ojp2.probability_of_occurrence_enum import ProbabilityOfOccurrenceEnum
from ojp2.source import Source
from ojp2.validity import Validity

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class OptionalTrafficElementStructure:
    """An event which is not planned by the traffic OPERATOR, which is affecting,
    or has the potential to affect traffic flow.

    This SIRI-SX element embeds the Datex2 TrafficElement, making all
    elements optional because they may alternatvielky be specified by
    common SIRI-SRX SITUATION elements.

    :ivar situation_record_creation_reference: A unique alphanumeric
        reference (either an external reference or GUID) of the
        SITUATIONRecord object (the first version of the record) that
        was created by the original supplier.
    :ivar situation_record_creation_time: The date/time that the
        SITUATIONRecord object (the first version of the record) was
        created by the original supplier.
    :ivar situation_record_observation_time: The date/time that the
        information represented by the current version of the
        SITUATIONRecord was observed by the original (potentially
        external) source of the information.
    :ivar situation_record_version: Each record within a SITUATION may
        iterate through a series of versions during its life time. The
        SITUATION record version uniquely identifies the version of a
        particular record within a SITUATION. It is generated and used
        by systems external to DATEX 2.
    :ivar situation_record_version_time: The date/time that this current
        version of the SITUATIONRecord was written into the database of
        the supplier which is involved in the data exchange.
    :ivar situation_record_first_supplier_version_time: The date/time
        that the current version of the SITUATION Record was written
        into the database of the original supplier in the supply chain.
    :ivar probability_of_occurrence: An assessment of the degree of
        likelihood that the reported event will occur.
    :ivar source:
    :ivar validity:
    :ivar impact: Impact of Road SITUATION as specified by Datex2.
    :ivar cause: Impact of Road SITUATION as specified by Datex2 model.
    :ivar general_public_comment: Datex 2 comments for public use.
    :ivar non_general_public_comment: Ccomments not for public use.
    :ivar group_of_locations: Datex 2 model of where event ois taking
        place on the road.
    :ivar management:
    :ivar situation_record_extension:
    :ivar traffic_element_extension:
    """

    situation_record_creation_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "situationRecordCreationReference",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
            "max_length": 1024,
        },
    )
    situation_record_creation_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "situationRecordCreationTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    situation_record_observation_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "situationRecordObservationTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    situation_record_version: Optional[int] = field(
        default=None,
        metadata={
            "name": "situationRecordVersion",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    situation_record_version_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "situationRecordVersionTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    situation_record_first_supplier_version_time: Optional[XmlDateTime] = (
        field(
            default=None,
            metadata={
                "name": "situationRecordFirstSupplierVersionTime",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "required": True,
            },
        )
    )
    probability_of_occurrence: Optional[ProbabilityOfOccurrenceEnum] = field(
        default=None,
        metadata={
            "name": "probabilityOfOccurrence",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    source: Optional[Source] = field(
        default=None,
        metadata={
            "name": "Source",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    validity: Optional[Validity] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    impact: Optional[Impact] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    cause: Optional[Cause] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    general_public_comment: list[Comment] = field(
        default_factory=list,
        metadata={
            "name": "generalPublicComment",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    non_general_public_comment: list[Comment] = field(
        default_factory=list,
        metadata={
            "name": "nonGeneralPublicComment",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    group_of_locations: Optional[GroupOfLocations] = field(
        default=None,
        metadata={
            "name": "groupOfLocations",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    management: Optional[Management] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    situation_record_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "situationRecordExtension",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    traffic_element_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "trafficElementExtension",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
