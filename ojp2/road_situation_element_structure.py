from dataclasses import dataclass, field
from typing import Optional

from ojp2.actions_structure import ActionsStructure
from ojp2.affects_scope_structure import AffectsScopeStructure
from ojp2.alert_cause import AlertCause
from ojp2.audience_enumeration import AudienceEnumeration
from ojp2.day_type import DayType
from ojp2.defaulted_text_structure import DefaultedTextStructure
from ojp2.environment_reason import EnvironmentReason
from ojp2.environment_sub_reason import EnvironmentSubReason
from ojp2.equipment_reason import EquipmentReason
from ojp2.equipment_sub_reason import EquipmentSubReason
from ojp2.extensions_2 import Extensions2
from ojp2.half_open_timestamp_output_range_structure import (
    HalfOpenTimestampOutputRangeStructure,
)
from ojp2.image_structure import ImageStructure
from ojp2.info_link_structure_2 import InfoLinkStructure2
from ojp2.information_status_enum import InformationStatusEnum
from ojp2.miscellaneous_reason import MiscellaneousReason
from ojp2.miscellaneous_sub_reason import MiscellaneousSubReason
from ojp2.natural_language_string_structure import (
    NaturalLanguageStringStructure,
)
from ojp2.personnel_reason import PersonnelReason
from ojp2.personnel_sub_reason import PersonnelSubReason
from ojp2.probability_of_occurrence_enum import ProbabilityOfOccurrenceEnum
from ojp2.pt_consequences_structure import PtConsequencesStructure
from ojp2.public_event_type_enum import PublicEventTypeEnum
from ojp2.quality_index_enumeration import QualityIndexEnumeration
from ojp2.report_type import ReportType
from ojp2.scope_type_enumeration import ScopeTypeEnumeration
from ojp2.sensitivity_enumeration import SensitivityEnumeration
from ojp2.severity import Severity
from ojp2.situation_element_structure import SituationElementStructure
from ojp2.situation_record import SituationRecord
from ojp2.undefined_reason import UndefinedReason
from ojp2.unknown_reason import UnknownReason
from ojp2.verification_status_enumeration import VerificationStatusEnumeration
from ojp2.workflow_status_enumeration import WorkflowStatusEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class RoadSituationElementStructure(SituationElementStructure):
    """
    Type for individual PT SITUATION.

    :ivar verification: Whether the SITUATION has been verified.
    :ivar progress: ProgressStatus. One of a specified set of overall
        processing states assigned to SITUATION. For example, 'Draft'
        for not yet published; 'Published' for live SITUATIONs; 'Closed'
        indicates a completed SITUATION.
    :ivar quality_index: Assessement of likely correctness of data.
        Default is reliable
    :ivar reality: Whether SITUATION is real or a test.
    :ivar likelihood: Likellihood of a future situation happening.
    :ivar publication: Publishing status one of a specified set of
        substates to which a SITUATION can be assigned.
    :ivar validity_period: Overall inclusive Period of applicability of
        SITUATION.
    :ivar repetitions: situation applies only on the repeated day types
        within the overall validity period(s). For example Sunday.
    :ivar publication_window: Publication Window for SITUATION if
        different from validity period.
    :ivar alert_cause:
    :ivar unknown_reason: DEPRECATED since SIRI 2.1 - use only
        AlertCause.
    :ivar miscellaneous_reason: DEPRECATED since SIRI 2.1 - use only
        AlertCause.
    :ivar personnel_reason: DEPRECATED since SIRI 2.1 - use only
        AlertCause.
    :ivar equipment_reason: DEPRECATED since SIRI 2.1 - use only
        AlertCause.
    :ivar environment_reason: DEPRECATED since SIRI 2.1 - use only
        AlertCause.
    :ivar undefined_reason: DEPRECATED since SIRI 2.1 - use only
        AlertCause.
    :ivar miscellaneous_sub_reason:
    :ivar personnel_sub_reason:
    :ivar equipment_sub_reason:
    :ivar environment_sub_reason:
    :ivar public_event_reason: Structured classification of Public
        Event, from which a standardized message can be generated.
    :ivar reason_name: Textual classification of nature of SITUATION,
        from which a standardized message can be generated. Not normally
        needed, except when TpegReason and PublicEventReason are absent.
        (Unbounded since SIRI 2.0)
    :ivar severity:
    :ivar priority: Arbitrary rating of priority 1-High.
    :ivar sensitivity: Confidentiality of SITUATION.
    :ivar audience: Intended audience of SITUATION.
    :ivar scope_type: Nature of scope, e.g. general, network.
    :ivar report_type:
    :ivar planned: Whether the SITUATION was planned (eg engineering
        works) or unplanned (eg service alteration). Default is 'false',
        i.e. unplanned.
    :ivar keywords: Arbitrary application specific classifiers.
    :ivar secondary_reasons: Additional reasons
    :ivar language: Default language.
    :ivar summary: Summary of SITUATION. If absent should be generated
        from structure elements / and or by condensing Description.
        (Unbounded since SIRI 2.0)
    :ivar description: Description of SITUATION. Should not repeat any
        strap line included in Summary.  (Unbounded since SIRI 2.0)
    :ivar detail: Additional descriptive details about the SITUATION
        (Unbounded since SIRI 2.0).
    :ivar advice: Further advice to passengers.  (Unbounded since SIRI
        2.0)
    :ivar internal: For internal information only, not passenger
        relevant
    :ivar images: Any images associated with SITUATION.
    :ivar info_links: Hyperlinks to other resources associated with
        SITUATION.
    :ivar affects: Structured model identifiying parts of transport
        network affected by SITUATION. OPERATOR and Network values will
        be defaulted to values in general Context unless explicitly
        overridden.
    :ivar consequences: Structured model describing effect of the
        SITUATION on PT system.
    :ivar publishing_actions: Structured model describing distribution
        actions to handle SITUATION. Any actions stated completely
        replace those from Context. If no actions are stated, any
        actions from general Context are used.
    :ivar situation_record: Datex2 SITUATION Record.
    :ivar extensions:
    """

    verification: Optional[VerificationStatusEnumeration] = field(
        default=None,
        metadata={
            "name": "Verification",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    progress: Optional[WorkflowStatusEnumeration] = field(
        default=None,
        metadata={
            "name": "Progress",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    quality_index: Optional[QualityIndexEnumeration] = field(
        default=None,
        metadata={
            "name": "QualityIndex",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    reality: Optional[InformationStatusEnum] = field(
        default=None,
        metadata={
            "name": "Reality",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    likelihood: Optional[ProbabilityOfOccurrenceEnum] = field(
        default=None,
        metadata={
            "name": "Likelihood",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    publication: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Publication",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    validity_period: list[HalfOpenTimestampOutputRangeStructure] = field(
        default_factory=list,
        metadata={
            "name": "ValidityPeriod",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_occurs": 1,
        },
    )
    repetitions: Optional["RoadSituationElementStructure.Repetitions"] = field(
        default=None,
        metadata={
            "name": "Repetitions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    publication_window: list[HalfOpenTimestampOutputRangeStructure] = field(
        default_factory=list,
        metadata={
            "name": "PublicationWindow",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    alert_cause: Optional[AlertCause] = field(
        default=None,
        metadata={
            "name": "AlertCause",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    unknown_reason: Optional[UnknownReason] = field(
        default=None,
        metadata={
            "name": "UnknownReason",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    miscellaneous_reason: Optional[MiscellaneousReason] = field(
        default=None,
        metadata={
            "name": "MiscellaneousReason",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    personnel_reason: Optional[PersonnelReason] = field(
        default=None,
        metadata={
            "name": "PersonnelReason",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    equipment_reason: Optional[EquipmentReason] = field(
        default=None,
        metadata={
            "name": "EquipmentReason",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    environment_reason: Optional[EnvironmentReason] = field(
        default=None,
        metadata={
            "name": "EnvironmentReason",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    undefined_reason: Optional[UndefinedReason] = field(
        default=None,
        metadata={
            "name": "UndefinedReason",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    miscellaneous_sub_reason: Optional[MiscellaneousSubReason] = field(
        default=None,
        metadata={
            "name": "MiscellaneousSubReason",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    personnel_sub_reason: Optional[PersonnelSubReason] = field(
        default=None,
        metadata={
            "name": "PersonnelSubReason",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    equipment_sub_reason: Optional[EquipmentSubReason] = field(
        default=None,
        metadata={
            "name": "EquipmentSubReason",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    environment_sub_reason: Optional[EnvironmentSubReason] = field(
        default=None,
        metadata={
            "name": "EnvironmentSubReason",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    public_event_reason: Optional[PublicEventTypeEnum] = field(
        default=None,
        metadata={
            "name": "PublicEventReason",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    reason_name: list[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "ReasonName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    severity: Optional[Severity] = field(
        default=None,
        metadata={
            "name": "Severity",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    priority: Optional[int] = field(
        default=None,
        metadata={
            "name": "Priority",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    sensitivity: Optional[SensitivityEnumeration] = field(
        default=None,
        metadata={
            "name": "Sensitivity",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    audience: Optional[AudienceEnumeration] = field(
        default=None,
        metadata={
            "name": "Audience",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    scope_type: Optional[ScopeTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "ScopeType",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    report_type: Optional[ReportType] = field(
        default=None,
        metadata={
            "name": "ReportType",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    planned: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Planned",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    keywords: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Keywords",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "tokens": True,
        },
    )
    secondary_reasons: Optional[
        "RoadSituationElementStructure.SecondaryReasons"
    ] = field(
        default=None,
        metadata={
            "name": "SecondaryReasons",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    language: Optional[str] = field(
        default=None,
        metadata={
            "name": "Language",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    summary: list[DefaultedTextStructure] = field(
        default_factory=list,
        metadata={
            "name": "Summary",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    description: list[DefaultedTextStructure] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    detail: list[DefaultedTextStructure] = field(
        default_factory=list,
        metadata={
            "name": "Detail",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    advice: list[DefaultedTextStructure] = field(
        default_factory=list,
        metadata={
            "name": "Advice",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    internal: Optional[DefaultedTextStructure] = field(
        default=None,
        metadata={
            "name": "Internal",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    images: Optional["RoadSituationElementStructure.Images"] = field(
        default=None,
        metadata={
            "name": "Images",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    info_links: Optional["RoadSituationElementStructure.InfoLinks"] = field(
        default=None,
        metadata={
            "name": "InfoLinks",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    affects: Optional[AffectsScopeStructure] = field(
        default=None,
        metadata={
            "name": "Affects",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    consequences: Optional[PtConsequencesStructure] = field(
        default=None,
        metadata={
            "name": "Consequences",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    publishing_actions: Optional[ActionsStructure] = field(
        default=None,
        metadata={
            "name": "PublishingActions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    situation_record: Optional[SituationRecord] = field(
        default=None,
        metadata={
            "name": "SituationRecord",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    extensions: Optional[Extensions2] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )

    @dataclass
    class Repetitions:
        day_type: list[DayType] = field(
            default_factory=list,
            metadata={
                "name": "DayType",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            },
        )

    @dataclass
    class SecondaryReasons:
        """
        :ivar reason: Reason
        """

        reason: list[
            "RoadSituationElementStructure.SecondaryReasons.Reason"
        ] = field(
            default_factory=list,
            metadata={
                "name": "Reason",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            },
        )

        @dataclass
        class Reason:
            """
            :ivar alert_cause:
            :ivar unknown_reason: DEPRECATED since SIRI 2.1 - use only
                AlertCause.
            :ivar miscellaneous_reason: DEPRECATED since SIRI 2.1 - use
                only AlertCause.
            :ivar personnel_reason: DEPRECATED since SIRI 2.1 - use only
                AlertCause.
            :ivar equipment_reason: DEPRECATED since SIRI 2.1 - use only
                AlertCause.
            :ivar environment_reason: DEPRECATED since SIRI 2.1 - use
                only AlertCause.
            :ivar undefined_reason: DEPRECATED since SIRI 2.1 - use only
                AlertCause.
            :ivar miscellaneous_sub_reason:
            :ivar personnel_sub_reason:
            :ivar equipment_sub_reason:
            :ivar environment_sub_reason:
            :ivar public_event_reason: Structured classification of
                Public Event, from which a standardized message can be
                generated.
            :ivar reason_name: Textual classification of nature of
                SITUATION, from which a standardized message can be
                generated. Not normally needed, except when TpegReason
                and PublicEventReason are absent.  (Unbounded since SIRI
                2.0)
            """

            alert_cause: Optional[AlertCause] = field(
                default=None,
                metadata={
                    "name": "AlertCause",
                    "type": "Element",
                    "namespace": "http://www.siri.org.uk/siri",
                },
            )
            unknown_reason: Optional[UnknownReason] = field(
                default=None,
                metadata={
                    "name": "UnknownReason",
                    "type": "Element",
                    "namespace": "http://www.siri.org.uk/siri",
                },
            )
            miscellaneous_reason: Optional[MiscellaneousReason] = field(
                default=None,
                metadata={
                    "name": "MiscellaneousReason",
                    "type": "Element",
                    "namespace": "http://www.siri.org.uk/siri",
                },
            )
            personnel_reason: Optional[PersonnelReason] = field(
                default=None,
                metadata={
                    "name": "PersonnelReason",
                    "type": "Element",
                    "namespace": "http://www.siri.org.uk/siri",
                },
            )
            equipment_reason: Optional[EquipmentReason] = field(
                default=None,
                metadata={
                    "name": "EquipmentReason",
                    "type": "Element",
                    "namespace": "http://www.siri.org.uk/siri",
                },
            )
            environment_reason: Optional[EnvironmentReason] = field(
                default=None,
                metadata={
                    "name": "EnvironmentReason",
                    "type": "Element",
                    "namespace": "http://www.siri.org.uk/siri",
                },
            )
            undefined_reason: Optional[UndefinedReason] = field(
                default=None,
                metadata={
                    "name": "UndefinedReason",
                    "type": "Element",
                    "namespace": "http://www.siri.org.uk/siri",
                },
            )
            miscellaneous_sub_reason: Optional[MiscellaneousSubReason] = field(
                default=None,
                metadata={
                    "name": "MiscellaneousSubReason",
                    "type": "Element",
                    "namespace": "http://www.siri.org.uk/siri",
                },
            )
            personnel_sub_reason: Optional[PersonnelSubReason] = field(
                default=None,
                metadata={
                    "name": "PersonnelSubReason",
                    "type": "Element",
                    "namespace": "http://www.siri.org.uk/siri",
                },
            )
            equipment_sub_reason: Optional[EquipmentSubReason] = field(
                default=None,
                metadata={
                    "name": "EquipmentSubReason",
                    "type": "Element",
                    "namespace": "http://www.siri.org.uk/siri",
                },
            )
            environment_sub_reason: Optional[EnvironmentSubReason] = field(
                default=None,
                metadata={
                    "name": "EnvironmentSubReason",
                    "type": "Element",
                    "namespace": "http://www.siri.org.uk/siri",
                },
            )
            public_event_reason: Optional[PublicEventTypeEnum] = field(
                default=None,
                metadata={
                    "name": "PublicEventReason",
                    "type": "Element",
                    "namespace": "http://www.siri.org.uk/siri",
                },
            )
            reason_name: list[NaturalLanguageStringStructure] = field(
                default_factory=list,
                metadata={
                    "name": "ReasonName",
                    "type": "Element",
                    "namespace": "http://www.siri.org.uk/siri",
                },
            )

    @dataclass
    class Images:
        """
        :ivar image: Image description.
        """

        image: list[ImageStructure] = field(
            default_factory=list,
            metadata={
                "name": "Image",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            },
        )

    @dataclass
    class InfoLinks:
        """
        :ivar info_link: Hyperlink description.
        """

        info_link: list[InfoLinkStructure2] = field(
            default_factory=list,
            metadata={
                "name": "InfoLink",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            },
        )
