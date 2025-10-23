from dataclasses import dataclass, field
from typing import List, Optional
from ojp.actions_structure import ActionsStructure
from ojp.affects_scope_structure import AffectsScopeStructure
from ojp.audience_enumeration import AudienceEnumeration
from ojp.day_type_enumeration import DayTypeEnumeration
from ojp.defaulted_text_structure import DefaultedTextStructure
from ojp.environment_reason_enumeration import EnvironmentReasonEnumeration
from ojp.environment_sub_reason_enumeration import EnvironmentSubReasonEnumeration
from ojp.equipment_reason_enumeration import EquipmentReasonEnumeration
from ojp.equipment_sub_reason_enumeration import EquipmentSubReasonEnumeration
from ojp.extensions_1 import Extensions1
from ojp.half_open_timestamp_output_range_structure import HalfOpenTimestampOutputRangeStructure
from ojp.image_structure import ImageStructure
from ojp.info_link_structure import InfoLinkStructure
from ojp.information_status_enum import InformationStatusEnum
from ojp.miscellaneous_reason_enumeration import MiscellaneousReasonEnumeration
from ojp.miscellaneous_sub_reason_enumeration import MiscellaneousSubReasonEnumeration
from ojp.natural_language_string_structure import NaturalLanguageStringStructure
from ojp.personnel_reason_enumeration import PersonnelReasonEnumeration
from ojp.personnel_sub_reason_enumeration import PersonnelSubReasonEnumeration
from ojp.probability_of_occurrence_enum import ProbabilityOfOccurrenceEnum
from ojp.pt_consequences_structure import PtConsequencesStructure
from ojp.public_event_type_enum import PublicEventTypeEnum
from ojp.quality_enumeration import QualityEnumeration
from ojp.report_type_enumeration import ReportTypeEnumeration
from ojp.scope_type_enumeration import ScopeTypeEnumeration
from ojp.sensitivity_enumeration import SensitivityEnumeration
from ojp.severity_enumeration import SeverityEnumeration
from ojp.situation_element_structure import SituationElementStructure
from ojp.verification_status_enumeration import VerificationStatusEnumeration
from ojp.workflow_status_enumeration import WorkflowStatusEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class PtSituationElementStructure(SituationElementStructure):
    """
    Type for individual PT SITUATION.

    :ivar verification: Whether the SITUATION has been verified.
    :ivar progress: ProgressStatus. One of a specified set of overall
        processing states assigned to SITUATION. For example, 'Draft'
        for not yet published; 'Published' for live SITUATIONs; 'Closed'
        indicates a completed SITUATION.
    :ivar quality_index: Assessement of likely correctness of data.
    :ivar reality: Whether SITUATION is real or a test.
    :ivar likelihood: Likellihoo of a future sutuation happening.
    :ivar publication: Publishing status one of a specified set of
        substates to which a SITUATION can be assigned.
    :ivar validity_period: Overall inclusive Period of applicability of
        SITUATION.
    :ivar repetitions: situation applies only on the repeated day types
        within the overall validity period(s). For example Sunday.
    :ivar publication_window: Publication Window for SITUATION if
        different from validity period.
    :ivar unknown_reason:
    :ivar miscellaneous_reason:
    :ivar personnel_reason: Personnel reason.
    :ivar equipment_reason:
    :ivar environment_reason: Environment reason.
    :ivar undefined_reason:
    :ivar miscellaneous_sub_reason:
    :ivar personnel_sub_reason: Personnel reason.
    :ivar equipment_sub_reason:
    :ivar environment_sub_reason: Environment reason.
    :ivar public_event_reason: Classifier of Pub;ic Event.
    :ivar reason_name: Text explanation of SITUATION reason. Not
        normally needed.  (Unbounded since SIRI 2.0)
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
    :ivar secondary_reasons: additioanl reasons.
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
    :ivar internal: Further advice to passengers.
    :ivar images: Any images associated with SITUATION.
    :ivar info_links: Hyperlinks to other resources associated with
        SITUATION.
    :ivar affects: Structured model identifiying parts of transport
        network affected by SITUATION. OPERATOR and NETWORK values will
        be defaulted to values in general Context unless explicitly
        overridden.
    :ivar consequences: Structured model describing effect of the
        SITUATION on PT system.
    :ivar publishing_actions: Structured model describing distribution
        actions to handle SITUATION. Any actions stated completely
        replace those from Context. If no actions are stated, any
        actions from general Context are used.
    :ivar extensions:
    """
    verification: Optional[VerificationStatusEnumeration] = field(
        default=None,
        metadata={
            "name": "Verification",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    progress: Optional[WorkflowStatusEnumeration] = field(
        default=None,
        metadata={
            "name": "Progress",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    quality_index: Optional[QualityEnumeration] = field(
        default=None,
        metadata={
            "name": "QualityIndex",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    reality: Optional[InformationStatusEnum] = field(
        default=None,
        metadata={
            "name": "Reality",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    likelihood: Optional[ProbabilityOfOccurrenceEnum] = field(
        default=None,
        metadata={
            "name": "Likelihood",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    publication: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Publication",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    validity_period: List[HalfOpenTimestampOutputRangeStructure] = field(
        default_factory=list,
        metadata={
            "name": "ValidityPeriod",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_occurs": 1,
        }
    )
    repetitions: Optional["PtSituationElementStructure.Repetitions"] = field(
        default=None,
        metadata={
            "name": "Repetitions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    publication_window: Optional[HalfOpenTimestampOutputRangeStructure] = field(
        default=None,
        metadata={
            "name": "PublicationWindow",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    unknown_reason: Optional[str] = field(
        default=None,
        metadata={
            "name": "UnknownReason",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    miscellaneous_reason: Optional[MiscellaneousReasonEnumeration] = field(
        default=None,
        metadata={
            "name": "MiscellaneousReason",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    personnel_reason: Optional[PersonnelReasonEnumeration] = field(
        default=None,
        metadata={
            "name": "PersonnelReason",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    equipment_reason: Optional[EquipmentReasonEnumeration] = field(
        default=None,
        metadata={
            "name": "EquipmentReason",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    environment_reason: Optional[EnvironmentReasonEnumeration] = field(
        default=None,
        metadata={
            "name": "EnvironmentReason",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    undefined_reason: Optional[str] = field(
        default=None,
        metadata={
            "name": "UndefinedReason",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    miscellaneous_sub_reason: Optional[MiscellaneousSubReasonEnumeration] = field(
        default=None,
        metadata={
            "name": "MiscellaneousSubReason",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    personnel_sub_reason: Optional[PersonnelSubReasonEnumeration] = field(
        default=None,
        metadata={
            "name": "PersonnelSubReason",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    equipment_sub_reason: Optional[EquipmentSubReasonEnumeration] = field(
        default=None,
        metadata={
            "name": "EquipmentSubReason",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    environment_sub_reason: Optional[EnvironmentSubReasonEnumeration] = field(
        default=None,
        metadata={
            "name": "EnvironmentSubReason",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    public_event_reason: Optional[PublicEventTypeEnum] = field(
        default=None,
        metadata={
            "name": "PublicEventReason",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    reason_name: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "ReasonName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    severity: Optional[SeverityEnumeration] = field(
        default=None,
        metadata={
            "name": "Severity",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    priority: Optional[int] = field(
        default=None,
        metadata={
            "name": "Priority",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    sensitivity: Optional[SensitivityEnumeration] = field(
        default=None,
        metadata={
            "name": "Sensitivity",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    audience: Optional[AudienceEnumeration] = field(
        default=None,
        metadata={
            "name": "Audience",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    scope_type: Optional[ScopeTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "ScopeType",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    report_type: Optional[ReportTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "ReportType",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    planned: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Planned",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    keywords: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Keywords",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "tokens": True,
        }
    )
    secondary_reasons: Optional["PtSituationElementStructure.SecondaryReasons"] = field(
        default=None,
        metadata={
            "name": "SecondaryReasons",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    language: Optional[str] = field(
        default=None,
        metadata={
            "name": "Language",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    summary: List[DefaultedTextStructure] = field(
        default_factory=list,
        metadata={
            "name": "Summary",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    description: List[DefaultedTextStructure] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    detail: List[DefaultedTextStructure] = field(
        default_factory=list,
        metadata={
            "name": "Detail",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    advice: List[DefaultedTextStructure] = field(
        default_factory=list,
        metadata={
            "name": "Advice",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    internal: Optional[DefaultedTextStructure] = field(
        default=None,
        metadata={
            "name": "Internal",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    images: Optional["PtSituationElementStructure.Images"] = field(
        default=None,
        metadata={
            "name": "Images",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    info_links: Optional["PtSituationElementStructure.InfoLinks"] = field(
        default=None,
        metadata={
            "name": "InfoLinks",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    affects: Optional[AffectsScopeStructure] = field(
        default=None,
        metadata={
            "name": "Affects",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    consequences: Optional[PtConsequencesStructure] = field(
        default=None,
        metadata={
            "name": "Consequences",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    publishing_actions: Optional[ActionsStructure] = field(
        default=None,
        metadata={
            "name": "PublishingActions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    extensions: Optional[Extensions1] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )

    @dataclass
    class Repetitions:
        day_type: List[DayTypeEnumeration] = field(
            default_factory=list,
            metadata={
                "name": "DayType",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            }
        )

    @dataclass
    class SecondaryReasons:
        """
        :ivar reason: Reason.
        """
        reason: List["PtSituationElementStructure.SecondaryReasons.Reason"] = field(
            default_factory=list,
            metadata={
                "name": "Reason",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            }
        )

        @dataclass
        class Reason:
            """
            :ivar unknown_reason:
            :ivar miscellaneous_reason:
            :ivar personnel_reason: Personnel reason.
            :ivar equipment_reason:
            :ivar environment_reason: Environment reason.
            :ivar undefined_reason:
            :ivar miscellaneous_sub_reason:
            :ivar personnel_sub_reason: Personnel reason.
            :ivar equipment_sub_reason:
            :ivar environment_sub_reason: Environment reason.
            :ivar public_event_reason: Classifier of Pub;ic Event.
            :ivar reason_name: Text explanation of SITUATION reason. Not
                normally needed.  (Unbounded since SIRI 2.0)
            """
            unknown_reason: Optional[str] = field(
                default=None,
                metadata={
                    "name": "UnknownReason",
                    "type": "Element",
                    "namespace": "http://www.siri.org.uk/siri",
                }
            )
            miscellaneous_reason: Optional[MiscellaneousReasonEnumeration] = field(
                default=None,
                metadata={
                    "name": "MiscellaneousReason",
                    "type": "Element",
                    "namespace": "http://www.siri.org.uk/siri",
                }
            )
            personnel_reason: Optional[PersonnelReasonEnumeration] = field(
                default=None,
                metadata={
                    "name": "PersonnelReason",
                    "type": "Element",
                    "namespace": "http://www.siri.org.uk/siri",
                }
            )
            equipment_reason: Optional[EquipmentReasonEnumeration] = field(
                default=None,
                metadata={
                    "name": "EquipmentReason",
                    "type": "Element",
                    "namespace": "http://www.siri.org.uk/siri",
                }
            )
            environment_reason: Optional[EnvironmentReasonEnumeration] = field(
                default=None,
                metadata={
                    "name": "EnvironmentReason",
                    "type": "Element",
                    "namespace": "http://www.siri.org.uk/siri",
                }
            )
            undefined_reason: Optional[str] = field(
                default=None,
                metadata={
                    "name": "UndefinedReason",
                    "type": "Element",
                    "namespace": "http://www.siri.org.uk/siri",
                }
            )
            miscellaneous_sub_reason: Optional[MiscellaneousSubReasonEnumeration] = field(
                default=None,
                metadata={
                    "name": "MiscellaneousSubReason",
                    "type": "Element",
                    "namespace": "http://www.siri.org.uk/siri",
                }
            )
            personnel_sub_reason: Optional[PersonnelSubReasonEnumeration] = field(
                default=None,
                metadata={
                    "name": "PersonnelSubReason",
                    "type": "Element",
                    "namespace": "http://www.siri.org.uk/siri",
                }
            )
            equipment_sub_reason: Optional[EquipmentSubReasonEnumeration] = field(
                default=None,
                metadata={
                    "name": "EquipmentSubReason",
                    "type": "Element",
                    "namespace": "http://www.siri.org.uk/siri",
                }
            )
            environment_sub_reason: Optional[EnvironmentSubReasonEnumeration] = field(
                default=None,
                metadata={
                    "name": "EnvironmentSubReason",
                    "type": "Element",
                    "namespace": "http://www.siri.org.uk/siri",
                }
            )
            public_event_reason: Optional[PublicEventTypeEnum] = field(
                default=None,
                metadata={
                    "name": "PublicEventReason",
                    "type": "Element",
                    "namespace": "http://www.siri.org.uk/siri",
                }
            )
            reason_name: List[NaturalLanguageStringStructure] = field(
                default_factory=list,
                metadata={
                    "name": "ReasonName",
                    "type": "Element",
                    "namespace": "http://www.siri.org.uk/siri",
                }
            )

    @dataclass
    class Images:
        """
        :ivar image: Image description.
        """
        image: List[ImageStructure] = field(
            default_factory=list,
            metadata={
                "name": "Image",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            }
        )

    @dataclass
    class InfoLinks:
        """
        :ivar info_link: Hyperlink description.
        """
        info_link: List[InfoLinkStructure] = field(
            default_factory=list,
            metadata={
                "name": "InfoLink",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            }
        )
