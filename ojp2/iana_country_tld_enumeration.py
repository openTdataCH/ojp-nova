from enum import Enum

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


class IanaCountryTldEnumeration(Enum):
    """
    Allowed values for classifying NPTG Localities.

    :cvar AC: Ascension Island.
    :cvar AD: Andorra.
    :cvar AE: United Arab Emirates.
    :cvar AF: Afghanistan.
    :cvar AG: Antigua and Barbuda.
    :cvar AI: Anguilla.
    :cvar AL: Albania.
    :cvar AM: Armenia.
    :cvar AN: Netherlands Antilles.
    :cvar AO: Angola.
    :cvar AQ: Antarctica.
    :cvar AR: Argentina.
    :cvar AS: American Samoa.
    :cvar AT: Austria.
    :cvar AU: Australia.
    :cvar AW: Aruba.
    :cvar AZ: Azerbaijan.
    :cvar AX: Aland Islands.
    :cvar BA: Bosnia and Herzegovina.
    :cvar BB: Barbados.
    :cvar BD: Bangladesh.
    :cvar BE: Belgium.
    :cvar BF: Burkina Faso.
    :cvar BG: Bulgaria.
    :cvar BH: Bahrain.
    :cvar BI: Burundi.
    :cvar BJ: Benin.
    :cvar BM: Bermuda.
    :cvar BN: Brunei Darussalam.
    :cvar BO: Bolivia.
    :cvar BR: Brazil.
    :cvar BS: Bahamas.
    :cvar BT: Bhutan.
    :cvar BV: Bouvet Island.
    :cvar BW: Botswana.
    :cvar BY: Belarus.
    :cvar BZ: Belize.
    :cvar CA: Canada.
    :cvar CC: Cocos (Keeling) Islands.
    :cvar CD: Congo, The Democratic Republic of the.
    :cvar CF: Central African Republic.
    :cvar CG: Congo, Republic of.
    :cvar CH: Switzerland.
    :cvar CI: Cote d'Ivoire.
    :cvar CK: Cook Islands.
    :cvar CL: Chile.
    :cvar CM: Cameroon.
    :cvar CN: China.
    :cvar CO: Colombia.
    :cvar CR: Costa Rica.
    :cvar CS: Serbia and Montenegro.
    :cvar CU: Cuba.
    :cvar CV: Cape Verde.
    :cvar CX: Christmas Island.
    :cvar CY: Cyprus.
    :cvar CZ: Czech Republic.
    :cvar DE: Germany.
    :cvar DJ: Djibouti.
    :cvar DK: Denmark.
    :cvar DM: Dominica.
    :cvar DO: Dominican Republic.
    :cvar DZ: Algeria.
    :cvar EC: Ecuador.
    :cvar EE: Estonia.
    :cvar EG: Egypt.
    :cvar EH: Western Sahara.
    :cvar ER: Eritrea.
    :cvar ES: Spain.
    :cvar ET: Ethiopia.
    :cvar EU: European Union.
    :cvar FI: Finland.
    :cvar FJ: Fiji.
    :cvar FK: Falkland Islands (Malvinas)
    :cvar FM: Micronesia, Federal State of.
    :cvar FO: Faroe Islands.
    :cvar FR: France.
    :cvar GA: Gabon.
    :cvar GB: United Kingdom.
    :cvar GD: Grenada.
    :cvar GE: Georgia.
    :cvar GF: French Guiana.
    :cvar GG: Guernsey.
    :cvar GH: Ghana.
    :cvar GI: Gibraltar.
    :cvar GL: Greenland.
    :cvar GM: Gambia.
    :cvar GN: Guinea.
    :cvar GP: Guadeloupe.
    :cvar GQ: Equatorial Guinea.
    :cvar GR: Greece.
    :cvar GS: South Georgia and the South Sandwich Islands.
    :cvar GT: Guatemala.
    :cvar GU: Guam.
    :cvar GW: Guinea-Bissau.
    :cvar GY: Guyana.
    :cvar HK: Hong Kong.
    :cvar HM: Heard and McDonald Islands.
    :cvar HN: Honduras.
    :cvar HR: Croatia/Hrvatska.
    :cvar HT: Haiti.
    :cvar HU: Hungary.
    :cvar ID: Indonesia.
    :cvar IE: Ireland.
    :cvar IL: Israel.
    :cvar IM: Isle of Man.
    :cvar IN: India.
    :cvar IO: British Indian Ocean Territory.
    :cvar IQ: Iraq
    :cvar IR: Iran, Islamic Republic of.
    :cvar IS: Iceland.
    :cvar IT: Italy.
    :cvar JE: Jersey.
    :cvar JM: Jamaica.
    :cvar JO: Jordan.
    :cvar JP: Japan.
    :cvar KE: Kenya.
    :cvar KG: Kyrgyzstan.
    :cvar KH: Cambodia.
    :cvar KI: Kiribati.
    :cvar KM: Comoros.
    :cvar KN: Saint Kitts and Nevis.
    :cvar KP: Korea, Democratic People's Republic.
    :cvar KR: Korea, Republic of.
    :cvar KW: Kuwait.
    :cvar KY: Cayman Islands.
    :cvar KZ: Kazakhstan.
    :cvar LA: Lao People's Democratic Republic.
    :cvar LB: Lebanon.
    :cvar LC: Saint Lucia.
    :cvar LI: Liechtenstein.
    :cvar LK: Sri Lanka.
    :cvar LR: Liberia.
    :cvar LS: Lesotho.
    :cvar LT: Lithuania.
    :cvar LU: Luxembourg.
    :cvar LV: Latvia.
    :cvar LY: Libyan Arab Jamahiriya.
    :cvar MA: Morocco.
    :cvar MC: Monaco.
    :cvar MD: Moldova, Republic of.
    :cvar MG: Madagascar.
    :cvar MH: Marshall Islands.
    :cvar MK: Macedonia, The Former Yugoslav Republic of.
    :cvar ML: Mali.
    :cvar MM: Myanmar.
    :cvar MN: Mongolia.
    :cvar MO: Macau.
    :cvar MP: Northern Mariana Islands.
    :cvar MQ: Martinique.
    :cvar MR: Mauritania.
    :cvar MS: Montserrat.
    :cvar MT: Malta.
    :cvar MU: Mauritius.
    :cvar MV: Maldives.
    :cvar MW: Malawi.
    :cvar MX: Mexico.
    :cvar MY: Malaysia.
    :cvar MZ: Mozambique.
    :cvar NA: Namibia.
    :cvar NC: New Caledonia.
    :cvar NE: Niger.
    :cvar NF: Norfolk Island.
    :cvar NG: Nigeria.
    :cvar NI: Nicaragua.
    :cvar NL: Netherlands.
    :cvar NO: Norway.
    :cvar NP: Nepal.
    :cvar NR: Nauru.
    :cvar NU: Niue.
    :cvar NZ: New Zealand.
    :cvar OM: Oman.
    :cvar PA: Panama.
    :cvar PE: Peru.
    :cvar PF: French Polynesia.
    :cvar PG: Papua New Guinea.
    :cvar PH: Philippines.
    :cvar PK: Pakistan.
    :cvar PL: Poland.
    :cvar PM: Saint Pierre and Miquelon.
    :cvar PN: Pitcairn Island.
    :cvar PR: Puerto Rico.
    :cvar PS: Palestinian Territories.
    :cvar PT: Portugal.
    :cvar PW: Palau.
    :cvar PY: Paraguay.
    :cvar QA: Qatar.
    :cvar RE: Reunion Island.
    :cvar RO: Romania.
    :cvar RU: Russian Federation.
    :cvar RW: Rwanda.
    :cvar SA: Saudi Arabia.
    :cvar SB: Solomon Islands.
    :cvar SC: Seychelles.
    :cvar SD: Sudan.
    :cvar SE: Sweden.
    :cvar SG: Singapore.
    :cvar SH: Saint Helena.
    :cvar SI: Slovenia.
    :cvar SJ: Svalbard and Jan Mayen Islands.
    :cvar SK: Slovak Republic.
    :cvar SL: Sierra Leone.
    :cvar SM: San Marino.
    :cvar SN: Senegal.
    :cvar SO: Somalia.
    :cvar SR: Suriname.
    :cvar ST: Sao Tome and Principe.
    :cvar SV: El Salvador.
    :cvar SY: Syrian Arab Republic.
    :cvar SZ: Swaziland.
    :cvar TC: Turks and Caicos Islands.
    :cvar TD: Chad.
    :cvar TF: French Southern Territories.
    :cvar TG: Togo.
    :cvar TH: Thailand.
    :cvar TJ: Tajikistan.
    :cvar TK: Tokelau.
    :cvar TL: Timor-Leste.
    :cvar TM: Turkmenistan.
    :cvar TN: Tunisia.
    :cvar TO: Tonga.
    :cvar TP: East Timor.
    :cvar TR: Turkey.
    :cvar TT: Trinidad and Tobago.
    :cvar TV: Tuvalu.
    :cvar TW: Taiwan.
    :cvar TZ: Tanzania.
    :cvar UA: Ukraine.
    :cvar UG: Uganda.
    :cvar UK: United Kingdom.
    :cvar UM: United States Minor Outlying Islands.
    :cvar US: United States.
    :cvar UY: Uruguay.
    :cvar UZ: Uzbekistan.
    :cvar VA: Holy See (Vatican City State)
    :cvar VC: Saint Vincent and the Grenadines.
    :cvar VE: Venezuela.
    :cvar VG: Virgin Islands, British.
    :cvar VI: Virgin Islands, Us.
    :cvar VN: Vietnam.
    :cvar VU: Vanuatu.
    :cvar WF: Wallis and Futuna Islands.
    :cvar WS: Samoa.
    :cvar YE: Yemen.
    :cvar YT: Mayotte.
    :cvar YU: Yugoslavia.
    :cvar ZA: South Africa.
    :cvar ZM: Zambia.
    :cvar ZW: Zimbabwe.
    """

    AC = "ac"
    AD = "ad"
    AE = "ae"
    AF = "af"
    AG = "ag"
    AI = "ai"
    AL = "al"
    AM = "am"
    AN = "an"
    AO = "ao"
    AQ = "aq"
    AR = "ar"
    AS = "as"
    AT = "at"
    AU = "au"
    AW = "aw"
    AZ = "az"
    AX = "ax"
    BA = "ba"
    BB = "bb"
    BD = "bd"
    BE = "be"
    BF = "bf"
    BG = "bg"
    BH = "bh"
    BI = "bi"
    BJ = "bj"
    BM = "bm"
    BN = "bn"
    BO = "bo"
    BR = "br"
    BS = "bs"
    BT = "bt"
    BV = "bv"
    BW = "bw"
    BY = "by"
    BZ = "bz"
    CA = "ca"
    CC = "cc"
    CD = "cd"
    CF = "cf"
    CG = "cg"
    CH = "ch"
    CI = "ci"
    CK = "ck"
    CL = "cl"
    CM = "cm"
    CN = "cn"
    CO = "co"
    CR = "cr"
    CS = "cs"
    CU = "cu"
    CV = "cv"
    CX = "cx"
    CY = "cy"
    CZ = "cz"
    DE = "de"
    DJ = "dj"
    DK = "dk"
    DM = "dm"
    DO = "do"
    DZ = "dz"
    EC = "ec"
    EE = "ee"
    EG = "eg"
    EH = "eh"
    ER = "er"
    ES = "es"
    ET = "et"
    EU = "eu"
    FI = "fi"
    FJ = "fj"
    FK = "fk"
    FM = "fm"
    FO = "fo"
    FR = "fr"
    GA = "ga"
    GB = "gb"
    GD = "gd"
    GE = "ge"
    GF = "gf"
    GG = "gg"
    GH = "gh"
    GI = "gi"
    GL = "gl"
    GM = "gm"
    GN = "gn"
    GP = "gp"
    GQ = "gq"
    GR = "gr"
    GS = "gs"
    GT = "gt"
    GU = "gu"
    GW = "gw"
    GY = "gy"
    HK = "hk"
    HM = "hm"
    HN = "hn"
    HR = "hr"
    HT = "ht"
    HU = "hu"
    ID = "id"
    IE = "ie"
    IL = "il"
    IM = "im"
    IN = "in"
    IO = "io"
    IQ = "iq"
    IR = "ir"
    IS = "is"
    IT = "it"
    JE = "je"
    JM = "jm"
    JO = "jo"
    JP = "jp"
    KE = "ke"
    KG = "kg"
    KH = "kh"
    KI = "ki"
    KM = "km"
    KN = "kn"
    KP = "kp"
    KR = "kr"
    KW = "kw"
    KY = "ky"
    KZ = "kz"
    LA = "la"
    LB = "lb"
    LC = "lc"
    LI = "li"
    LK = "lk"
    LR = "lr"
    LS = "ls"
    LT = "lt"
    LU = "lu"
    LV = "lv"
    LY = "ly"
    MA = "ma"
    MC = "mc"
    MD = "md"
    MG = "mg"
    MH = "mh"
    MK = "mk"
    ML = "ml"
    MM = "mm"
    MN = "mn"
    MO = "mo"
    MP = "mp"
    MQ = "mq"
    MR = "mr"
    MS = "ms"
    MT = "mt"
    MU = "mu"
    MV = "mv"
    MW = "mw"
    MX = "mx"
    MY = "my"
    MZ = "mz"
    NA = "na"
    NC = "nc"
    NE = "ne"
    NF = "nf"
    NG = "ng"
    NI = "ni"
    NL = "nl"
    NO = "no"
    NP = "np"
    NR = "nr"
    NU = "nu"
    NZ = "nz"
    OM = "om"
    PA = "pa"
    PE = "pe"
    PF = "pf"
    PG = "pg"
    PH = "ph"
    PK = "pk"
    PL = "pl"
    PM = "pm"
    PN = "pn"
    PR = "pr"
    PS = "ps"
    PT = "pt"
    PW = "pw"
    PY = "py"
    QA = "qa"
    RE = "re"
    RO = "ro"
    RU = "ru"
    RW = "rw"
    SA = "sa"
    SB = "sb"
    SC = "sc"
    SD = "sd"
    SE = "se"
    SG = "sg"
    SH = "sh"
    SI = "si"
    SJ = "sj"
    SK = "sk"
    SL = "sl"
    SM = "sm"
    SN = "sn"
    SO = "so"
    SR = "sr"
    ST = "st"
    SV = "sv"
    SY = "sy"
    SZ = "sz"
    TC = "tc"
    TD = "td"
    TF = "tf"
    TG = "tg"
    TH = "th"
    TJ = "tj"
    TK = "tk"
    TL = "tl"
    TM = "tm"
    TN = "tn"
    TO = "to"
    TP = "tp"
    TR = "tr"
    TT = "tt"
    TV = "tv"
    TW = "tw"
    TZ = "tz"
    UA = "ua"
    UG = "ug"
    UK = "uk"
    UM = "um"
    US = "us"
    UY = "uy"
    UZ = "uz"
    VA = "va"
    VC = "vc"
    VE = "ve"
    VG = "vg"
    VI = "vi"
    VN = "vn"
    VU = "vu"
    WF = "wf"
    WS = "ws"
    YE = "ye"
    YT = "yt"
    YU = "yu"
    ZA = "za"
    ZM = "zm"
    ZW = "zw"
