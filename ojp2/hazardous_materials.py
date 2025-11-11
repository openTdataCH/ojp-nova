from dataclasses import dataclass, field
from typing import Optional

from ojp2.dangerous_goods_regulations_enum import DangerousGoodsRegulationsEnum
from ojp2.extension_type import ExtensionType
from ojp2.multilingual_string import MultilingualString

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class HazardousMaterials:
    chemical_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "chemicalName",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    dangerous_goods_flash_point: Optional[float] = field(
        default=None,
        metadata={
            "name": "dangerousGoodsFlashPoint",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    dangerous_goods_regulations: Optional[DangerousGoodsRegulationsEnum] = (
        field(
            default=None,
            metadata={
                "name": "dangerousGoodsRegulations",
                "type": "Element",
                "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            },
        )
    )
    hazard_code_identification: Optional[str] = field(
        default=None,
        metadata={
            "name": "hazardCodeIdentification",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "max_length": 1024,
        },
    )
    hazard_code_version_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "hazardCodeVersionNumber",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    hazard_substance_item_page_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "hazardSubstanceItemPageNumber",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "max_length": 1024,
        },
    )
    trem_card_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "tremCardNumber",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "max_length": 1024,
        },
    )
    undg_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "undgNumber",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "max_length": 1024,
        },
    )
    volume_of_dangerous_goods: Optional[float] = field(
        default=None,
        metadata={
            "name": "volumeOfDangerousGoods",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    weight_of_dangerous_goods: Optional[float] = field(
        default=None,
        metadata={
            "name": "weightOfDangerousGoods",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    hazardous_materials_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "hazardousMaterialsExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
