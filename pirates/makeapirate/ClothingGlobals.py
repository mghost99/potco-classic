from pandac.PandaModules import VBase4
from pirates.piratesbase import PLocalizer
from pirates.piratesbase import PiratesGlobals
import random
HAT = 0
SHIRT = 1
VEST = 2
COAT = 3
PANT = 4
BELT = 5
SOCK = 6
SHOE = 7
CLOTHING_NUMBER = {
    'HAT': HAT,
    'SHIRT': SHIRT,
    'VEST': VEST,
    'COAT': COAT,
    'BELT': BELT,
    'PANT': PANT,
    'SHOE': SHOE}
CLOTHING_STRING = {
    HAT: 'HAT',
    SHIRT: 'SHIRT',
    VEST: 'VEST',
    COAT: 'COAT',
    BELT: 'BELT',
    PANT: 'PANT',
    SHOE: 'SHOE'}
SELECTION_CHOICES = {
    'DEFAULT': {
        'MALE': {
            'FACE': [
                0,
                1,
                2,
                3],
            'HAIR': [
                0,
                1,
                2,
                5,
                6,
                7,
                8,
                9,
                10,
                11,
                12,
                13],
            'HAT': {
                0: [
                    0],
                2: [
                    0],
                6: [
                    0],
                7: [
                    0],
                8: [
                    0]},
            'SHIRT': {
                1: [
                    0,
                    1,
                    2,
                    3,
                    4],
                2: [
                    0,
                    1,
                    3],
                3: [
                    0,
                    1,
                    2],
                4: [
                    1],
                6: [
                    0,
                    1,
                    2,
                    3],
                7: [
                    1,
                    2],
                8: [
                    2]},
            'VEST': {
                0: [
                    0],
                1: [
                    0,
                    1,
                    2,
                    4],
                2: [
                    0,
                    2,
                    4]},
            'COAT': {
                0: [
                    0],
                1: [
                    0],
                2: [
                    0]},
            'PANT': {
                0: [
                    0,
                    1,
                    2,
                    3],
                1: [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9,
                    10]},
            'BELT': {
                0: [
                    0],
                1: [
                    0],
                2: [
                    0],
                3: [
                    0],
                4: [
                    0],
                5: [
                    0]},
            'SHOE': {
                0: [
                    0],
                1: [
                    0,
                    1,
                    2,
                    3],
                2: [
                    0,
                    1,
                    2,
                    3]}},
        'FEMALE': {
            'FACE': [
                0,
                1,
                2,
                3],
            'HAIR': [
                0,
                1,
                2,
                3,
                4,
                5,
                6,
                7,
                8,
                9,
                10,
                11,
                12,
                13,
                14,
                15,
                16],
            'HAT': {
                0: [
                    0],
                1: [
                    0],
                3: [
                    0],
                5: [
                    0],
                6: [
                    0]},
            'SHIRT': {
                0: [
                    0,
                    1,
                    2,
                    3],
                1: [
                    0,
                    1,
                    2,
                    3],
                2: [
                    0,
                    1,
                    2,
                    3],
                3: [
                    1,
                    2,
                    3],
                4: [
                    0,
                    1,
                    2,
                    3]},
            'VEST': {
                0: [
                    0],
                1: [
                    0,
                    1,
                    2,
                    3],
                2: [
                    0,
                    1,
                    2,
                    3],
                3: [
                    0,
                    1,
                    2],
                4: [
                    0,
                    1,
                    2]},
            'COAT': {
                0: [
                    0],
                1: [
                    0,
                    1],
                2: [
                    0,
                    1,
                    2]},
            'PANT': {
                0: [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5],
                1: [
                    0,
                    1,
                    2,
                    3,
                    4],
                2: [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6]},
            'BELT': {
                0: [
                    0],
                1: [
                    0],
                2: [
                    0],
                3: [
                    0],
                4: [
                    0],
                5: [
                    0],
                6: [
                    0],
                7: [
                    0],
                8: [
                    0],
                9: [
                    0],
                10: [
                    0]},
            'SHOE': {
                0: [
                    0],
                1: [
                    0,
                    1,
                    2,
                    3],
                2: [
                    0,
                    1,
                    2,
                    3],
                3: [
                    0,
                    1,
                    2,
                    3,
                    4],
                4: [
                    0,
                    1,
                    2,
                    3]}}},
    'NPC': {
        'MALE': {
            'FACE': [
                0,
                1,
                2,
                3,
                4,
                5,
                6],
            'HAIR': [
                0,
                1,
                2,
                5,
                6,
                7,
                8,
                9,
                10,
                11,
                12,
                13],
            'HAT': {
                0: [
                    0],
                1: [
                    0],
                2: [
                    0,
                    1,
                    2,
                    3],
                3: [
                    0],
                4: [
                    0],
                5: [
                    0],
                6: [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5],
                7: [
                    0,
                    1,
                    2,
                    3,
                    4],
                8: [
                    0,
                    1,
                    2],
                9: [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6]},
            'SHIRT': {
                0: [
                    0],
                1: [
                    0,
                    1,
                    2,
                    3,
                    4],
                2: [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9,
                    10,
                    11,
                    12],
                3: [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7],
                4: [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6],
                5: [
                    0,
                    1,
                    2],
                6: [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8],
                7: [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7],
                8: [
                    0,
                    1,
                    2],
                9: [
                    0,
                    1,
                    2],
                10: [
                    0]},
            'VEST': {
                0: [
                    0],
                1: [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8],
                2: [
                    0,
                    1,
                    2,
                    3,
                    4],
                3: [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5]},
            'COAT': {
                0: [
                    0],
                1: [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9,
                    10,
                    11,
                    12,
                    13,
                    14],
                2: [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7],
                3: [
                    0],
                4: [
                    0]},
            'PANT': {
                0: [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9,
                    10,
                    11,
                    12],
                1: [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9,
                    10,
                    12,
                    13,
                    14,
                    15],
                2: [
                    0,
                    1,
                    2,
                    3,
                    4],
                3: [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8],
                4: [
                    0],
                5: [
                    0],
                6: [
                    0,
                    1,
                    2]},
            'BELT': {
                0: [
                    0],
                1: [
                    0],
                2: [
                    0],
                3: [
                    0],
                4: [
                    0],
                5: [
                    0],
                6: [
                    0],
                7: [
                    0],
                8: [
                    0],
                9: [
                    0],
                10: [
                    0],
                11: [
                    0],
                12: [
                    0],
                13: [
                    0],
                14: [
                    0],
                15: [
                    0],
                16: [
                    0],
                17: [
                    0],
                18: [
                    0],
                19: [
                    0]},
            'SHOE': {
                0: [
                    0],
                1: [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9],
                2: [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7],
                3: [
                    0],
                4: [
                    0],
                5: [
                    0]}},
        'FEMALE': {
            'FACE': [
                0,
                1,
                2,
                3,
                4],
            'HAIR': [
                0,
                1,
                2,
                3,
                4,
                5,
                6,
                7,
                8,
                9,
                10,
                11,
                12,
                13,
                14,
                15,
                16,
                17,
                18,
                19],
            'HAT': {
                0: [
                    0],
                1: [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6],
                2: [
                    0],
                3: [
                    0],
                4: [
                    0],
                5: [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5],
                6: [
                    0,
                    1,
                    2,
                    3,
                    4]},
            'SHIRT': {
                0: [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6],
                1: [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6],
                2: [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6],
                3: [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9],
                4: [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6],
                5: [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6],
                6: [
                    0,
                    1,
                    2,
                    3]},
            'VEST': {
                0: [
                    0],
                1: [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9,
                    10],
                2: [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9,
                    10],
                3: [
                    0,
                    1,
                    2,
                    4,
                    5,
                    6],
                4: [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5]},
            'COAT': {
                0: [
                    0],
                1: [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9],
                2: [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8],
                3: [
                    0]},
            'PANT': {
                0: [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9,
                    10,
                    11,
                    12,
                    13,
                    14,
                    15],
                1: [
                    0,
                    1,
                    2,
                    3,
                    4,
                    6,
                    7,
                    8,
                    9,
                    10,
                    11,
                    12],
                2: [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9,
                    10,
                    11,
                    12,
                    13],
                3: [
                    0,
                    1],
                4: [
                    0,
                    1],
                5: [
                    0]},
            'BELT': {
                0: [
                    0],
                1: [
                    0],
                2: [
                    0],
                3: [
                    0],
                4: [
                    0],
                5: [
                    0],
                6: [
                    0],
                7: [
                    0],
                8: [
                    0],
                9: [
                    0],
                10: [
                    0],
                11: [
                    0],
                12: [
                    0],
                13: [
                    0],
                14: [
                    0],
                15: [
                    0],
                16: [
                    0],
                17: [
                    0]},
            'SHOE': {
                0: [
                    0],
                1: [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9],
                2: [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7],
                3: [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8],
                4: [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7],
                5: [
                    0]}}}}
textures = {
    'MALE': {
        'HAT': [
            [
                [
                    'hat_none',
                    VBase4(1.0, 1.0, 1.0, 1.0)]],
            [
                [
                    'PM_hat_captain_leather',
                    VBase4(36 / 255.0, 26 / 255.0, 9 / 255.0, 1.0)]],
            [
                [
                    'PM_hat_tricorn_brown',
                    VBase4(43 / 255.0, 48 / 255.0, 62 / 255.0, 1.0)],
                [
                    'PM_hat_tricorn_orange',
                    VBase4(125 / 255.0, 59 / 255.0, 37 / 255.0, 1.0)],
                [
                    'PM_hat_tricorn_black_skull',
                    VBase4(33 / 255.0, 37 / 255.0, 36 / 255.0, 1.0)],
                [
                    'PM_hat_tricorn_navy_goldtrim',
                    VBase4(32 / 255.0, 51 / 255.0, 78 / 255.0, 1.0)]],
            [
                [
                    'PM_hat_navy_redcoat',
                    VBase4(63 / 255.0, 63 / 255.0, 63 / 255.0, 1.0)]],
            [
                [
                    'PM_navy_hat_india',
                    VBase4(42 / 255.0, 42 / 255.0, 42 / 255.0, 1.0)]],
            [
                [
                    'PM_hat_admiral',
                    VBase4(49 / 255.0, 49 / 255.0, 49 / 255.0, 1.0)]],
            [
                [
                    'PM_hat_bandana_plain',
                    VBase4(149 / 255.0, 149 / 255.0, 149 / 255.0, 1.0)],
                [
                    'PM_hat_bandana_full_blue',
                    VBase4(192 / 255.0, 192 / 255.0, 192 / 255.0, 1.0)],
                [
                    'PM_hat_bandana_full_skullcrossbones',
                    VBase4(47 / 255.0, 47 / 255.0, 47 / 255.0, 1.0)],
                [
                    'PM_hat_bandanna_full_blue_patches',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_hat_bandanna_full_blue_zigzag',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_hat_bandana_full_polkadot_basic_outfit',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'pir_t_clo_upt_bandana_thanks08',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'PM_hat_bandana_plain',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_hat_bandana_full_blue',
                    VBase4(192 / 255.0, 192 / 255.0, 192 / 255.0, 1.0)],
                [
                    'PM_hat_bandana_full_skullcrossbones',
                    VBase4(47 / 255.0, 47 / 255.0, 47 / 255.0, 1.0)],
                [
                    'PM_hat_bandanna_full_blue_patches',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_hat_bandanna_full_blue_zigzag',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'PM_hat_beanie_plain',
                    VBase4(96 / 255.0, 91 / 255.0, 82 / 255.0, 1.0)],
                [
                    'PM_hat_beanie_black_crossbones',
                    VBase4(12 / 255.0, 10 / 255.0, 11 / 255.0, 1.0)],
                [
                    'PM_hat_beanie_blue_skull',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'PM_hat_barbossa+PM_hat_barbossa_feather',
                    VBase4(43 / 255.0, 48 / 255.0, 62 / 255.0, 1.0)],
                [
                    'PM_hat_barb_style_brown+PM_hat_barb_style_brown_feather',
                    VBase4(78 / 255.0, 64 / 255.0, 55 / 255.0, 1.0)],
                [
                    'PM_hat_barossa_style_hat_blue_knit_band+PM_hat_barossa_style_hat_blue_knit_band_feather',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_hat_barossa_style_hat_brown_buttons+PM_hat_barossa_style_hat_brown_buttons_feather',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_hat_barossa_style_hat_brown_purple_feather+PM_hat_barossa_style_hat_brown_purple_feather_feather',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_hat_barbossa_advanced_outfit+PM_hat_barbossa_advanced_outfit_feather',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_hat_barbossa_intermediate_outfit+PM_hat_barbossa_intermediate_outfit_feather',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]]],
        'SHIRT': [
            [
                [
                    'PM_none',
                    VBase4(1.0, 1.0, 1.0, 1.0)]],
            [
                [
                    'PM_shirt_tanktop_sweatstained',
                    VBase4(180 / 255.0, 178 / 255.0, 178 / 255.0, 1.0)],
                [
                    'PM_shirt_tanktop_stripes',
                    VBase4(179 / 255.0, 164 / 255.0, 147 / 255.0, 1.0)],
                [
                    'PM_shirt_tanktop_plain',
                    VBase4(228 / 255.0, 227 / 255.0, 227 / 255.0, 1.0)],
                [
                    'PM_shirt_tanktop_buttons',
                    VBase4(192 / 255.0, 165 / 255.0, 154 / 255.0, 1.0)],
                [
                    'PM_shirt_tanktop_suspenders',
                    VBase4(218 / 255.0, 200 / 255.0, 174 / 255.0, 1.0)]],
            [
                [
                    'PM_shirt_nosleeves_stripe',
                    VBase4(145 / 255.0, 123 / 255.0, 94 / 255.0, 1.0)],
                [
                    'PM_shirt_nosleeves_ties',
                    VBase4(193 / 255.0, 200 / 255.0, 201 / 255.0, 1.0)],
                [
                    'PM_shirt_nosleeves_leatherfront',
                    VBase4(169 / 255.0, 177 / 255.0, 185 / 255.0, 1.0)],
                [
                    'PM_shirt_nosleeves_centerseam',
                    VBase4(234 / 255.0, 233 / 255.0, 211 / 255.0, 1.0)],
                [
                    'PM_shirt_nosleeves_bluethreebutton',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_shirt_nosleeves_palegreen',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_shirt_nosleeves_purplesidebuckle',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_shirt_nosleeves_salmon',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_shirt_nosleeves_flax_brown',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_shirt_nosleeves_silk_blue',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_shirt_nosleeves_silk_red',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_shirt_nosleeves_silk_white',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_shirt_nosleeves_advanced_outfit',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'PM_shirt_short_round_frontlacing',
                    VBase4(79 / 255.0, 85 / 255.0, 90 / 255.0, 1.0)],
                [
                    'PM_shirt_short_round_frontbuttons',
                    VBase4(70 / 255.0, 51 / 255.0, 38 / 255.0, 1.0)],
                [
                    'PM_shirt_short_round_stripes',
                    VBase4(131 / 255.0, 126 / 255.0, 137 / 255.0, 1.0)],
                [
                    'PM_shirt_short_round_leather_cloth',
                    VBase4(227 / 255.0, 194 / 255.0, 132 / 255.0, 1.0)],
                [
                    'PM_shirt_short_round_blue_whitecollar',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_shirt_short_round_cloth_black',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_shirt_short_round_cloth_caramel',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_shirt_short_round_darkbrown_buckle',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'PM_shirt_shared_cloth_metal_buttons',
                    VBase4(169 / 255.0, 170 / 255.0, 169 / 255.0, 1.0)],
                [
                    'PM_shirt_shared_cloth_plain1',
                    VBase4(172 / 255.0, 172 / 255.0, 172 / 255.0, 1.0)],
                [
                    'PM_shirt_shared_cloth_plain2',
                    VBase4(162 / 255.0, 164 / 255.0, 162 / 255.0, 1.0)],
                [
                    'PM_shirt_shared_cloth_browncollar',
                    VBase4(175 / 255.0, 162 / 255.0, 144 / 255.0, 1.0)],
                [
                    'PM_shirt_shared_cloth_fabricwaistband',
                    VBase4(110 / 255.0, 110 / 255.0, 98 / 255.0, 1.0)],
                [
                    'PM_shirt_shared_cloth_leatherwaistband',
                    VBase4(123 / 255.0, 85 / 255.0, 80 / 255.0, 1.0)],
                [
                    'PM_shirt_shared_cloth_yellowcollar',
                    VBase4(116 / 255.0, 161 / 255.0, 158 / 255.0, 1.0)]],
            [
                [
                    'PM_shirt_shared_cloth_metal_buttons',
                    VBase4(169 / 255.0, 170 / 255.0, 169 / 255.0, 1.0)],
                [
                    'PM_shirt_shared_cloth_plain1',
                    VBase4(172 / 255.0, 172 / 255.0, 172 / 255.0, 1.0)],
                [
                    'PM_shirt_shared_cloth_plain2',
                    VBase4(162 / 255.0, 164 / 255.0, 162 / 255.0, 1.0)],
                [
                    'PM_shirt_shared_cloth_browncollar',
                    VBase4(175 / 255.0, 162 / 255.0, 144 / 255.0, 1.0)],
                [
                    'PM_shirt_shared_cloth_fabricwaistband',
                    VBase4(110 / 255.0, 110 / 255.0, 98 / 255.0, 1.0)],
                [
                    'PM_shirt_shared_cloth_leatherwaistband',
                    VBase4(123 / 255.0, 85 / 255.0, 80 / 255.0, 1.0)],
                [
                    'PM_shirt_shared_cloth_yellowcollar',
                    VBase4(116 / 255.0, 161 / 255.0, 158 / 255.0, 1.0)]],
            [
                [
                    'PM_shirt_long_sleeve_puffy_ClothWithTies',
                    VBase4(170 / 255.0, 161 / 255.0, 142 / 255.0, 1.0)],
                [
                    'PM_shirt_long_sleeve_puffy_cloth_brown_leather',
                    VBase4(154 / 255.0, 146 / 255.0, 132 / 255.0, 1.0)],
                [
                    'PM_shirt_long_sleeve_puffy_plain',
                    VBase4(210 / 255.0, 216 / 255.0, 220 / 255.0, 1.0)],
                [
                    'PM_shirt_long_sleeve_puffy_center_tie',
                    VBase4(207 / 255.0, 192 / 255.0, 161 / 255.0, 1.0)],
                [
                    'PM_shirt_long_sleeve_puffy_cream_orangevest',
                    VBase4(95 / 255.0, 47 / 255.0, 17 / 255.0, 1.0)],
                [
                    'PM_shirt_long_sleeve_puffy_white_brownpillowvest',
                    VBase4(77 / 255.0, 48 / 255.0, 27 / 255.0, 1.0)],
                [
                    'PM_shirt_long_sleeve_puffy_white_brownvest',
                    VBase4(36 / 255.0, 26 / 255.0, 20 / 255.0, 1.0)],
                [
                    'PM_shirt_long_sleeve_puffy_white_redvest',
                    VBase4(89 / 255.0, 21 / 255.0, 30 / 255.0, 1.0)],
                [
                    'PM_shirt_long_sleeve_puffy_intermediate_outfit',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'PM_shirt_shared_cloth_metal_buttons',
                    VBase4(169 / 255.0, 170 / 255.0, 169 / 255.0, 1.0)],
                [
                    'PM_shirt_shared_cloth_plain1',
                    VBase4(172 / 255.0, 172 / 255.0, 172 / 255.0, 1.0)],
                [
                    'PM_shirt_shared_cloth_plain2',
                    VBase4(162 / 255.0, 164 / 255.0, 162 / 255.0, 1.0)],
                [
                    'PM_shirt_shared_cloth_browncollar',
                    VBase4(175 / 255.0, 162 / 255.0, 144 / 255.0, 1.0)],
                [
                    'PM_shirt_shared_cloth_fabricwaistband',
                    VBase4(110 / 255.0, 110 / 255.0, 98 / 255.0, 1.0)],
                [
                    'PM_shirt_shared_cloth_leatherwaistband',
                    VBase4(123 / 255.0, 85 / 255.0, 80 / 255.0, 1.0)],
                [
                    'PM_shirt_shared_cloth_yellowcollar',
                    VBase4(116 / 255.0, 161 / 255.0, 158 / 255.0, 1.0)],
                [
                    'PM_shirt_long_sleeve_puffy_tan_basic_outfit',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'PM_shirt_shared_cloth_metal_buttons',
                    VBase4(169 / 255.0, 170 / 255.0, 169 / 255.0, 1.0)],
                [
                    'PM_shirt_shared_cloth_plain1',
                    VBase4(172 / 255.0, 172 / 255.0, 172 / 255.0, 1.0)],
                [
                    'PM_shirt_shared_cloth_plain2',
                    VBase4(162 / 255.0, 164 / 255.0, 162 / 255.0, 1.0)]],
            [
                [
                    'PM_shirt_apron',
                    VBase4(82 / 255.0, 88 / 255.0, 93 / 255.0, 1.0)],
                [
                    'PM_shirt_apron_black',
                    VBase4(82 / 255.0, 88 / 255.0, 93 / 255.0, 1.0)],
                [
                    'PM_shirt_apron_black',
                    VBase4(82 / 255.0, 88 / 255.0, 93 / 255.0, 1.0)]],
            [
                [
                    'PM_shirt_shared_cloth_dealer',
                    VBase4(162 / 255.0, 164 / 255.0, 162 / 255.0, 1.0)]]],
        'VEST': [
            [
                [
                    'PM_none',
                    VBase4(1.0, 1.0, 1.0, 1.0)]],
            [
                [
                    'PM_vest_open_leather_silk',
                    VBase4(172 / 255.0, 108 / 255.0, 60 / 255.0, 1.0)],
                [
                    'PM_vest_open_PatchworkDark',
                    VBase4(104 / 255.0, 112 / 255.0, 107 / 255.0, 1.0)],
                [
                    'PM_vest_open_belts',
                    VBase4(96 / 255.0, 75 / 255.0, 53 / 255.0, 1.0)],
                [
                    'PM_vest_open_clasp',
                    VBase4(91 / 255.0, 109 / 255.0, 109 / 255.0, 1.0)],
                [
                    'PM_vest_open_buttons',
                    VBase4(70 / 255.0, 98 / 255.0, 108 / 255.0, 1.0)],
                [
                    'PM_vest_open_blue_silverbuttons',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_vest_open_brown_blacklapel',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_vest_open_brown_redscarf',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_vest_open_green_blacklapel',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'PM_vest_closed_silk_stripe_lapel',
                    VBase4(118 / 255.0, 101 / 255.0, 73 / 255.0, 1.0)],
                [
                    'PM_vest_closed_clasp',
                    VBase4(151 / 255.0, 127 / 255.0, 101 / 255.0, 1.0)],
                [
                    'PM_vest_closed_lapel',
                    VBase4(187 / 255.0, 158 / 255.0, 108 / 255.0, 1.0)],
                [
                    'PM_vest_closed_leathertop',
                    VBase4(198 / 255.0, 190 / 255.0, 168 / 255.0, 1.0)],
                [
                    'PM_vest_closed_stripe',
                    VBase4(174 / 255.0, 163 / 255.0, 163 / 255.0, 1.0)],
                [
                    'PM_vest_closed_advanced_outfit',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'PM_vest_long_closed_a',
                    VBase4(145 / 255.0, 141 / 255.0, 130 / 255.0, 1.0)],
                [
                    'PM_vest_long_closed_brown_whitecollar',
                    VBase4(71 / 255.0, 37 / 255.0, 3 / 255.0, 1.0)],
                [
                    'PM_vest_long_closed_rust',
                    VBase4(76 / 255.0, 30 / 255.0, 14 / 255.0, 1.0)],
                [
                    'PM_vest_long_closed_white_ropebelt',
                    VBase4(92 / 255.0, 91 / 255.0, 79 / 255.0, 1.0)],
                [
                    'PM_vest_long_closed_yellowgreen_stripes',
                    VBase4(110 / 255.0, 93 / 255.0, 39 / 255.0, 1.0)],
                [
                    'PM_vest_long_closed_intermediate_outfit',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]]],
        'COAT': [
            [
                [
                    'PM_none',
                    VBase4(1.0, 1.0, 1.0, 1.0)]],
            [
                [
                    'PM_coat_long_braidsandfloralpattern',
                    VBase4(91 / 255.0, 76 / 255.0, 59 / 255.0, 1.0)],
                [
                    'PM_coat_long_braids_embroidery',
                    VBase4(67 / 255.0, 61 / 255.0, 41 / 255.0, 1.0)],
                [
                    'PM_coat_long_cloth_lighttrim',
                    VBase4(143 / 255.0, 144 / 255.0, 164 / 255.0, 1.0)],
                [
                    'PM_coat_long_darktrim_backties',
                    VBase4(93 / 255.0, 79 / 255.0, 53 / 255.0, 1.0)],
                [
                    'PM_coat_long_fabric_leatherbelt',
                    VBase4(32 / 255.0, 44 / 255.0, 27 / 255.0, 1.0)],
                [
                    'PM_coat_long_french',
                    VBase4(41 / 255.0, 36 / 255.0, 38 / 255.0, 1.0)],
                [
                    'PM_coat_long_leather',
                    VBase4(43 / 255.0, 28 / 255.0, 15 / 255.0, 1.0)],
                [
                    'PM_coat_long_afro',
                    VBase4(86 / 255.0, 74 / 255.0, 41 / 255.0, 1.0)],
                [
                    'PM_coat_long_taupe',
                    VBase4(64 / 255.0, 54 / 255.0, 49 / 255.0, 1.0)],
                [
                    'PM_coat_long_brown',
                    VBase4(69 / 255.0, 42 / 255.0, 21 / 255.0, 1.0)],
                [
                    'PM_coat_long_blue_yellowtrim',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_coat_long_gold_blackbuttons',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_coat_long_green_yellowtrim',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_coat_long_red_yellowtrim',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_coat_long_advanced_outfit',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'PM_coat_short_blackwithstitching',
                    VBase4(22 / 255.0, 23 / 255.0, 25 / 255.0, 1.0)],
                [
                    'PM_coat_short_cloth_darkleather_goldtrim',
                    VBase4(85 / 255.0, 86 / 255.0, 60 / 255.0, 1.0)],
                [
                    'PM_coat_short_dark_stringtiesback',
                    VBase4(59 / 255.0, 61 / 255.0, 63 / 255.0, 1.0)],
                [
                    'PM_coat_short_red_blackleathertrim',
                    VBase4(130 / 255.0, 31 / 255.0, 27 / 255.0, 1.0)],
                [
                    'PM_coat_short_wool_brownleathertrim',
                    VBase4(117 / 255.0, 104 / 255.0, 77 / 255.0, 1.0)],
                [
                    'PM_coat_short_yellow_blacklapel',
                    VBase4(121 / 255.0, 88 / 255.0, 40 / 255.0, 1.0)],
                [
                    'PM_coat_short_purple_blackcollar',
                    VBase4(79 / 255.0, 48 / 255.0, 58 / 255.0, 1.0)],
                [
                    'PM_coat_short_blue_goldtrim',
                    VBase4(33 / 255.0, 51 / 255.0, 59 / 255.0, 1.0)]],
            [
                [
                    'PM_navy_coat',
                    VBase4(148 / 255.0, 29 / 255.0, 29 / 255.0, 1.0)]],
            [
                [
                    'PM_navy_coat_india',
                    VBase4(31 / 255.0, 33 / 255.0, 31 / 255.0, 1.0)]]],
        'PANT': [
            [
                [
                    'PM_pant_long_pants_tucked_LeatherGoldButtons',
                    VBase4(83 / 255.0, 70 / 255.0, 53 / 255.0, 1.0)],
                [
                    'PM_pant_long_pants_tucked_leathergoldbuttons_nopatch',
                    VBase4(131 / 255.0, 106 / 255.0, 71 / 255.0, 1.0)],
                [
                    'PM_pant_long_pants_tucked_cotton_leathersidepocket',
                    VBase4(154 / 255.0, 164 / 255.0, 170 / 255.0, 1.0)],
                [
                    'PM_pant_long_pants_tucked_leather_buttonfront',
                    VBase4(63 / 255.0, 63 / 255.0, 63 / 255.0, 1.0)],
                [
                    'PM_pant_long_pants_tucked_cloth_leatherstripes',
                    VBase4(79 / 255.0, 79 / 255.0, 79 / 255.0, 1.0)],
                [
                    'PM_pant_long_pants_tucked_leather_miniknives',
                    VBase4(79 / 255.0, 79 / 255.0, 79 / 255.0, 1.0)],
                [
                    'PM_pant_long_pants_tucked_black_yellowtrim',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_pant_long_pants_tucked_blue_stripes',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_pant_long_pants_tucked_brown_sidebuttons',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_pant_long_pants_tucked_greygreen',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_pant_long_pants_tucked_red_sidebones',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_pant_long_pants_tucked_red_yellowstripes',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_pant_long_pants_tucked_advanced_outfit',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'PM_pant_long_pants_untucked_plain3',
                    VBase4(138 / 255.0, 138 / 255.0, 138 / 255.0, 1.0)],
                [
                    'PM_pant_long_pants_untucked_celticbuttons',
                    VBase4(183 / 255.0, 165 / 255.0, 178 / 255.0, 1.0)],
                [
                    'PM_pant_long_pants_untucked_twotone',
                    VBase4(186 / 255.0, 182 / 255.0, 187 / 255.0, 1.0)],
                [
                    'PM_pant_long_pants_untucked_onetone',
                    VBase4(178 / 255.0, 177 / 255.0, 179 / 255.0, 1.0)],
                [
                    'PM_pant_long_pants_untucked_leatherpocket_trim',
                    VBase4(116 / 255.0, 101 / 255.0, 70 / 255.0, 1.0)],
                [
                    'PM_pant_long_pants_untucked_leather_skullsnaps_suede',
                    VBase4(213 / 255.0, 186 / 255.0, 140 / 255.0, 1.0)],
                [
                    'PM_pant_long_pants_untucked_leather_skullsnaps_no_cuff',
                    VBase4(218 / 255.0, 191 / 255.0, 145 / 255.0, 1.0)],
                [
                    'PM_pant_long_pants_untucked_leather_skullsnaps_no_stripe',
                    VBase4(218 / 255.0, 191 / 255.0, 145 / 255.0, 1.0)],
                [
                    'PM_pant_long_pants_untucked_plain1',
                    VBase4(137 / 255.0, 124 / 255.0, 97 / 255.0, 1.0)],
                [
                    'PM_pant_long_pants_untucked_plain2',
                    VBase4(61 / 255.0, 66 / 255.0, 64 / 255.0, 1.0)],
                [
                    'PM_pant_long_pants_untucked_leather_plain',
                    VBase4(131 / 255.0, 117 / 255.0, 107 / 255.0, 1.0)],
                [
                    'zomb_long_pants_untucked',
                    VBase4(144 / 255.0, 135 / 255.0, 111 / 255.0, 1.0)],
                [
                    'PM_pant_long_pants_untucked_bluegreensash',
                    VBase4(44 / 255.0, 66 / 255.0, 64 / 255.0, 1.0)],
                [
                    'PM_pant_long_pants_untucked_greenbronzesash',
                    VBase4(41 / 255.0, 37 / 255.0, 16 / 255.0, 1.0)],
                [
                    'PM_pant_long_pants_untucked_blue_basic_outfit',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_pant_long_pants_untucked_intermediate_outfit',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'PM_pant_shorts_threesidebuttons',
                    VBase4(94 / 255.0, 92 / 255.0, 69 / 255.0, 1.0)],
                [
                    'PM_pant_shorts_3ties',
                    VBase4(184 / 255.0, 160 / 255.0, 107 / 255.0, 1.0)],
                [
                    'PM_pant_shorts_1buttonflap',
                    VBase4(224 / 255.0, 213 / 255.0, 205 / 255.0, 1.0)],
                [
                    'PM_pant_shorts_3buckle',
                    VBase4(122 / 255.0, 122 / 255.0, 99 / 255.0, 1.0)],
                [
                    'PM_pant_shorts_browncloth',
                    VBase4(52 / 255.0, 30 / 255.0, 9 / 255.0, 1.0)]],
            [
                [
                    'PM_pant_short_pants_twotonewithsash',
                    VBase4(92 / 255.0, 108 / 255.0, 126 / 255.0, 1.0)],
                [
                    'PM_pant_short_pants_sidepocket',
                    VBase4(126 / 255.0, 109 / 255.0, 97 / 255.0, 1.0)],
                [
                    'PM_pant_short_pants_simplecanvas',
                    VBase4(190 / 255.0, 177 / 255.0, 149 / 255.0, 1.0)],
                [
                    'PM_pant_short_pants_sideleather',
                    VBase4(203 / 255.0, 184 / 255.0, 163 / 255.0, 1.0)],
                [
                    'PM_pant_short_pants_blue_white_top',
                    VBase4(33 / 255.0, 45 / 255.0, 84 / 255.0, 1.0)],
                [
                    'PM_pant_short_pants_brown_cloth',
                    VBase4(52 / 255.0, 30 / 255.0, 9 / 255.0, 1.0)],
                [
                    'PM_pant_short_pants_light_brown',
                    VBase4(125 / 255.0, 87 / 255.0, 43 / 255.0, 1.0)],
                [
                    'PM_pant_short_pants_rust',
                    VBase4(77 / 255.0, 36 / 255.0, 18 / 255.0, 1.0)],
                [
                    'PM_pant_short_pants_slate',
                    VBase4(55 / 255.0, 71 / 255.0, 79 / 255.0, 1.0)]],
            [
                [
                    'PM_navy_pants',
                    VBase4(156 / 255.0, 145 / 255.0, 132 / 255.0, 1.0)]],
            [
                [
                    'PM_navy_coat_india',
                    VBase4(31 / 255.0, 33 / 255.0, 31 / 255.0, 1.0)]],
            [
                [
                    'PM_pant_apron',
                    VBase4(145 / 255.0, 130 / 255.0, 102 / 255.0, 1.0)],
                [
                    'PM_pant_apron_black',
                    VBase4(145 / 255.0, 130 / 255.0, 102 / 255.0, 1.0)],
                [
                    'PM_pant_apron_black',
                    VBase4(145 / 255.0, 130 / 255.0, 102 / 255.0, 1.0)]]],
        'BELT': [
            [
                [
                    'PM_none',
                    VBase4(1.0, 1.0, 1.0, 1.0)]],
            [
                [
                    'PM_belt_sash_plain',
                    VBase4(195 / 255.0, 193 / 255.0, 188 / 255.0, 1.0)]],
            [
                [
                    'PM_belt_sash_celticbuckle',
                    VBase4(108 / 255.0, 97 / 255.0, 93 / 255.0, 1.0)]],
            [
                [
                    'PM_belt_strap_oval+PM_belt_buckle_oval',
                    VBase4(65 / 255.0, 43 / 255.0, 1 / 255.0, 1.0)]],
            [
                [
                    'PM_belt_strap_LeatherBrown+PM_belt_buckle_SkullGold',
                    VBase4(40 / 255.0, 30 / 255.0, 20 / 255.0, 1.0)]],
            [
                [
                    'PM_belt_strap_black+PM_belt_buckle_square',
                    VBase4(24 / 255.0, 10 / 255.0, 2 / 255.0, 1.0)]],
            [
                [
                    'PM_belt_strap_blackleather_01+PM_belt_buckle_goldskull_01',
                    VBase4(23 / 255.0, 23 / 255.0, 24 / 255.0, 1.0)]],
            [
                [
                    'PM_belt_strap_brownleather_01+PM_belt_buckle_ovalgold_01',
                    VBase4(41 / 255.0, 29 / 255.0, 14 / 255.0, 1.0)]],
            [
                [
                    'PM_belt_strap_blackleather_01+PM_belt_buckle_ovalgold_02',
                    VBase4(23 / 255.0, 23 / 255.0, 24 / 255.0, 1.0)]],
            [
                [
                    'PM_belt_sash_bluegold',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'PM_belt_sash_goldtassel',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'PM_belt_sash_pink',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'PM_belt_sash_red',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'PM_belt_strap_oval_gold_brownleather+PM_belt_buckle_oval_gold_brownleather',
                    VBase4(23 / 255.0, 23 / 255.0, 24 / 255.0, 1.0)]],
            [
                [
                    'PM_belt_strap_oval_goldskull_blackleather+PM_belt_buckle_oval_goldskull_blackleather',
                    VBase4(23 / 255.0, 23 / 255.0, 24 / 255.0, 1.0)]],
            [
                [
                    'PM_belt_strap_square_sculpture_blackbutton+PM_belt_buckle_square_sculpture_blackbutton',
                    VBase4(24 / 255.0, 10 / 255.0, 2 / 255.0, 1.0)]],
            [
                [
                    'PM_belt_strap_square_silver_blueleather+PM_belt_buckle_square_silver_blueleather',
                    VBase4(24 / 255.0, 10 / 255.0, 2 / 255.0, 1.0)]],
            [
                [
                    'PM_belt_sash_red_basic_outfit+PM_belt_sash_red_basic_outfit',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'PM_belt_strap_square_advanced_outfit+PM_belt_buckle_square_advanced_outfit',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'PM_belt_strap_square_advanced_outfit+PM_belt_buckle_square_intermediate_outfit',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]]],
        'SHOE': [
            [
                [
                    'PM_none',
                    VBase4(1.0, 1.0, 1.0, 1.0)]],
            [
                [
                    'PM_shoe_tall_boots_TanWithFlap',
                    VBase4(40 / 255.0, 32 / 255.0, 24 / 255.0, 1.0)],
                [
                    'PM_shoe_tall_boots_2buckle',
                    VBase4(17 / 255.0, 16 / 255.0, 14 / 255.0, 1.0)],
                [
                    'PM_shoe_tall_boots_lace',
                    VBase4(60 / 255.0, 47 / 255.0, 33 / 255.0, 1.0)],
                [
                    'PM_shoe_tall_boots_leatherlower',
                    VBase4(35 / 255.0, 27 / 255.0, 24 / 255.0, 1.0)],
                [
                    'PM_shoe_tall_boots_black_furtop',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_shoe_tall_boots_blue_straps',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_shoe_tall_boots_brown_furtop',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_shoe_tall_boots_brown_laces',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_shoe_tall_boots_advanced_outfit',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_shoe_tall_boots_intermediate_outfit',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'PM_shoe_medium_boots_laced',
                    VBase4(5 / 255.0, 5 / 255.0, 5 / 255.0, 1.0)],
                [
                    'PM_shoe_medium_boots_buckle',
                    VBase4(36 / 255.0, 34 / 255.0, 31 / 255.0, 1.0)],
                [
                    'PM_shoe_medium_boots_lacefront',
                    VBase4(35 / 255.0, 29 / 255.0, 24 / 255.0, 1.0)],
                [
                    'PM_shoe_medium_boots_plain',
                    VBase4(36 / 255.0, 32 / 255.0, 27 / 255.0, 1.0)],
                [
                    'PM_shoe_medium_boots_brown',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_shoe_medium_boots_brown_greentops',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_shoe_medium_boots_light_brown',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'PM_shoe_medium_boots_blue_basic_outfit',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'PM_navy_shoes',
                    VBase4(63 / 255.0, 58 / 255.0, 48 / 255.0, 1.0)]],
            [
                [
                    'PM_navy_shoe_india',
                    VBase4(16 / 255.0, 16 / 255.0, 16 / 255.0, 1.0)]],
            [
                [
                    'PM_none',
                    VBase4(1.0, 1.0, 1.0, 1.0)]]] },
    'FEMALE': {
        'HAT': [
            [
                [
                    'hat_none',
                    VBase4(1.0, 1.0, 1.0, 1.0)]],
            [
                [
                    'FP_hat_dress_base+FP_hat_dress_feather',
                    VBase4(118 / 255.0, 104 / 255.0, 70 / 255.0, 1.0)],
                [
                    'FP_hat_dress_blue_purplefeather+FP_hat_dress_blue_purplefeather_feather',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_hat_dress_green_stringband+FP_hat_dress_green_stringband_feather',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_hat_dress_pink_bluefeather+FP_hat_dress_pink_bluefeather_feather',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_hat_dress_purple_butterfly+FP_hat_dress_purple_butterfly_feather',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_hat_dress_advanced_outfit+FP_hat_dress_advanced_outfit_feather',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_hat_dress_intermediate_outfit+FP_hat_dress_intermediate_outfit_feather',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'FP_hat_navy_redcoat',
                    VBase4(21 / 255.0, 20 / 255.0, 23 / 255.0, 1.0)]],
            [
                [
                    'FP_navy_hat+FP_hat_dress_feather',
                    VBase4(122 / 255.0, 100 / 255.0, 65 / 255.0, 1.0)]],
            [
                [
                    'FP_hat_worker',
                    VBase4(162 / 255.0, 162 / 255.0, 162 / 255.0, 1.0)]],
            [
                [
                    'FP_hat_bandana',
                    VBase4(192 / 255.0, 192 / 255.0, 192 / 255.0, 1.0)],
                [
                    'FP_hat_bandana_full_blue',
                    VBase4(111 / 255.0, 148 / 255.0, 148 / 255.0, 1.0)],
                [
                    'FP_hat_bandana_full_skullcrossbones',
                    VBase4(29 / 255.0, 29 / 255.0, 29 / 255.0, 1.0)],
                [
                    'FP_hat_bandana_full_purple',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_hat_bandana_full_redstripes',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_hat_bandana_full_polkadot_basic_outfit',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'pir_t_clo_upt_bandana_thanks08',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'FP_hat_bandana',
                    VBase4(192 / 255.0, 192 / 255.0, 192 / 255.0, 1.0)],
                [
                    'FP_hat_bandana_full_blue',
                    VBase4(111 / 255.0, 148 / 255.0, 148 / 255.0, 1.0)],
                [
                    'FP_hat_bandana_full_skullcrossbones',
                    VBase4(29 / 255.0, 29 / 255.0, 29 / 255.0, 1.0)],
                [
                    'FP_hat_bandana_full_purple',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_hat_bandana_full_redstripes',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]]],
        'SHIRT': [
            [
                [
                    'FP_shirt_short_sleeve_stitch',
                    VBase4(181 / 255.0, 180 / 255.0, 168 / 255.0, 1.0)],
                [
                    'FP_shirt_short_sleeve_3button',
                    VBase4(171 / 255.0, 112 / 255.0, 94 / 255.0, 1.0)],
                [
                    'FP_shirt_short_sleeve_collar',
                    VBase4(152 / 255.0, 164 / 255.0, 144 / 255.0, 1.0)],
                [
                    'FP_shirt_short_sleeve_ties',
                    VBase4(142 / 255.0, 134 / 255.0, 150 / 255.0, 1.0)],
                [
                    'FP_shirt_short_sleeve_bluelace',
                    VBase4(80 / 255.0, 101 / 255.0, 111 / 255.0, 1.0)],
                [
                    'FP_shirt_short_sleeve_pinkwhite',
                    VBase4(113 / 255.0, 85 / 255.0, 100 / 255.0, 1.0)],
                [
                    'FP_shirt_short_sleeve_yellowgold',
                    VBase4(150 / 255.0, 131 / 255.0, 91 / 255.0, 1.0)]],
            [
                [
                    'FP_shirt_short_sleeve_puffy_smFrontLacing',
                    VBase4(195 / 255.0, 205 / 255.0, 174 / 255.0, 1.0)],
                [
                    'FP_shirt_short_sleeve_puffy_2ties',
                    VBase4(224 / 255.0, 207 / 255.0, 182 / 255.0, 1.0)],
                [
                    'FP_shirt_short_sleeve_puffy_3button',
                    VBase4(151 / 255.0, 153 / 255.0, 135 / 255.0, 1.0)],
                [
                    'FP_shirt_short_sleeve_puffy_front_bow',
                    VBase4(157 / 255.0, 106 / 255.0, 110 / 255.0, 1.0)],
                [
                    'FP_shirt_short_sleeve_puffy_lightgreen',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_shirt_short_sleeve_puffy_powderblue',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_shirt_short_sleeve_puffy_red_creamtrim',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'FP_shirt_long_sleeve_puffy_collarbuttons',
                    VBase4(104 / 255.0, 100 / 255.0, 83 / 255.0, 1.0)],
                [
                    'FP_shirt_long_sleeve_puffy_broach',
                    VBase4(192 / 255.0, 146 / 255.0, 140 / 255.0, 1.0)],
                [
                    'FP_shirt_long_sleeve_puffy_front_tie',
                    VBase4(173 / 255.0, 181 / 255.0, 198 / 255.0, 1.0)],
                [
                    'FP_shirt_long_sleeve_puffy_stitch',
                    VBase4(95 / 255.0, 103 / 255.0, 94 / 255.0, 1.0)],
                [
                    'FP_shirt_long_sleeve_puffy_blue_whitecuffs',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_shirt_long_sleeve_puffy_olivegreen',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_shirt_long_sleeve_puffy_purple_whitecuffs',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'FP_shirt_long_sleeve_lowcut_leather_corset_ruffles',
                    VBase4(211 / 255.0, 194 / 255.0, 165 / 255.0, 1.0)],
                [
                    'FP_shirt_long_sleeve_lowcut_3button',
                    VBase4(103 / 255.0, 106 / 255.0, 93 / 255.0, 1.0)],
                [
                    'FP_shirt_long_sleeve_lowcut_ruffles',
                    VBase4(208 / 255.0, 192 / 255.0, 161 / 255.0, 1.0)],
                [
                    'FP_shirt_long_sleeve_lowcut_ties',
                    VBase4(201 / 255.0, 179 / 255.0, 148 / 255.0, 1.0)],
                [
                    'FP_shirt_long_sleeve_lowcut_brown_greensleeves',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_shirt_long_sleeve_lowcut_pink_whitecollar',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_shirt_long_sleeve_lowcut_white_greysleeves',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_shirt_long_sleeve_lowcut_tan_basic_outfit',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_shirt_long_sleeve_lowcut_intermediate_outfit',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_shirt_long_sleeve_lowcut_advanced_outfit',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'FP_shirt_long_sleeve_collar_lacesleeve',
                    VBase4(170 / 255.0, 166 / 255.0, 177 / 255.0, 1.0)],
                [
                    'FP_shirt_long_sleeve_collar_collarbuttons',
                    VBase4(81 / 255.0, 93 / 255.0, 78 / 255.0, 1.0)],
                [
                    'FP_shirt_long_sleeve_collar_largestripes',
                    VBase4(107 / 255.0, 65 / 255.0, 64 / 255.0, 1.0)],
                [
                    'FP_shirt_long_sleeve_collar_stitches',
                    VBase4(89 / 255.0, 96 / 255.0, 94 / 255.0, 1.0)],
                [
                    'FP_shirt_long_sleeve_collar_white_brownvest',
                    VBase4(86 / 255.0, 57 / 255.0, 34 / 255.0, 1.0)],
                [
                    'FP_shirt_long_sleeve_collar_white_greenvest',
                    VBase4(54 / 255.0, 56 / 255.0, 56 / 255.0, 1.0)],
                [
                    'FP_shirt_long_sleeve_collar_white_redvest',
                    VBase4(74 / 255.0, 26 / 255.0, 35 / 255.0, 1.0)]],
            [
                [
                    'FP_shirt_long_sleeve_tall_collar_leather_vest_fleur',
                    VBase4(174 / 255.0, 162 / 255.0, 132 / 255.0, 1.0)],
                [
                    'FP_shirt_long_sleeve_tall_collar_buttons',
                    VBase4(187 / 255.0, 179 / 255.0, 156 / 255.0, 1.0)],
                [
                    'FP_shirt_long_sleeve_tall_collar_stitch',
                    VBase4(149 / 255.0, 138 / 255.0, 113 / 255.0, 1.0)],
                [
                    'FP_shirt_long_sleeve_tall_collar_ties',
                    VBase4(237 / 255.0, 228 / 255.0, 203 / 255.0, 1.0)],
                [
                    'FP_shirt_long_sleeve_tall_collar_green',
                    VBase4(97 / 255.0, 115 / 255.0, 39 / 255.0, 1.0)],
                [
                    'FP_shirt_long_sleeve_tall_collar_lightblue',
                    VBase4(93 / 255.0, 116 / 255.0, 125 / 255.0, 1.0)],
                [
                    'FP_shirt_long_sleeve_tall_collar_purplewhite',
                    VBase4(137 / 255.0, 121 / 255.0, 156 / 255.0, 1.0)]],
            [
                [
                    'FP_gypsy_dress_a',
                    VBase4(151 / 255.0, 85 / 255.0, 23 / 255.0, 1.0)],
                [
                    'FP_gypsy_dress_b',
                    VBase4(86 / 255.0, 43 / 255.0, 29 / 255.0, 1.0)],
                [
                    'FP_bartender_dress_a',
                    VBase4(79 / 255.0, 89 / 255.0, 115 / 255.0, 1.0)],
                [
                    'FP_shopkeeps_dress_a',
                    VBase4(79 / 255.0, 89 / 255.0, 115 / 255.0, 1.0)]]],
        'VEST': [
            [
                [
                    'FP_none',
                    VBase4(1.0, 1.0, 1.0, 1.0)]],
            [
                [
                    'FP_vest_closed_clothtwobutton',
                    VBase4(169 / 255.0, 176 / 255.0, 180 / 255.0, 1.0)],
                [
                    'FP_vest_closed_plain',
                    VBase4(188 / 255.0, 191 / 255.0, 165 / 255.0, 1.0)],
                [
                    'FP_vest_closed_stripes',
                    VBase4(162 / 255.0, 170 / 255.0, 175 / 255.0, 1.0)],
                [
                    'FP_vest_closed_ties',
                    VBase4(178 / 255.0, 141 / 255.0, 108 / 255.0, 1.0)],
                [
                    'FP_vest_closed_browngold',
                    VBase4(80 / 255.0, 35 / 255.0, 27 / 255.0, 1.0)],
                [
                    'FP_vest_closed_brownpurple',
                    VBase4(96 / 255.0, 42 / 255.0, 50 / 255.0, 1.0)],
                [
                    'FP_vest_closed_lightgreen',
                    VBase4(93 / 255.0, 91 / 255.0, 57 / 255.0, 1.0)],
                [
                    'FP_vest_closed_redblack',
                    VBase4(23 / 255.0, 15 / 255.0, 15 / 255.0, 1.0)],
                [
                    'FP_vest_closed_whiteblue',
                    VBase4(53 / 255.0, 63 / 255.0, 70 / 255.0, 1.0)],
                [
                    'FP_vest_closed_yellowgreen',
                    VBase4(104 / 255.0, 78 / 255.0, 26 / 255.0, 1.0)],
                [
                    'FP_vest_closed_advanced_outfit',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'FP_vest_lowcut_clothtwobutton',
                    VBase4(159 / 255.0, 170 / 255.0, 182 / 255.0, 1.0)],
                [
                    'FP_vest_lowcut_onebutton',
                    VBase4(212 / 255.0, 169 / 255.0, 123 / 255.0, 1.0)],
                [
                    'FP_vest_lowcut_stripes',
                    VBase4(143 / 255.0, 136 / 255.0, 92 / 255.0, 1.0)],
                [
                    'FP_vest_lowcut_ties',
                    VBase4(155 / 255.0, 61 / 255.0, 51 / 255.0, 1.0)],
                [
                    'FP_vest_lowcut_bluegold',
                    VBase4(51 / 255.0, 79 / 255.0, 89 / 255.0, 1.0)],
                [
                    'FP_vest_lowcut_browngold',
                    VBase4(103 / 255.0, 47 / 255.0, 28 / 255.0, 1.0)],
                [
                    'FP_vest_lowcut_greenyellow',
                    VBase4(41 / 255.0, 79 / 255.0, 49 / 255.0, 1.0)],
                [
                    'FP_vest_lowcut_lightyellow',
                    VBase4(116 / 255.0, 116 / 255.0, 55 / 255.0, 1.0)],
                [
                    'FP_vest_lowcut_purplegold',
                    VBase4(64 / 255.0, 45 / 255.0, 90 / 255.0, 1.0)],
                [
                    'FP_vest_lowcut_redblack',
                    VBase4(76 / 255.0, 6 / 255.0, 7 / 255.0, 1.0)],
                [
                    'FP_vest_lowcut_intermediate_outfit',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'FP_corset_high_LeatherStraps',
                    VBase4(82 / 255.0, 82 / 255.0, 82 / 255.0, 1.0)],
                [
                    'FP_corset_high_FrillyLacy',
                    VBase4(127 / 255.0, 69 / 255.0, 63 / 255.0, 1.0)],
                [
                    'FP_corset_high_SimpleCanvas',
                    VBase4(118 / 255.0, 106 / 255.0, 61 / 255.0, 1.0)],
                [
                    'zomb_corset_low_fourlaces',
                    VBase4(121 / 255.0, 124 / 255.0, 103 / 255.0, 1.0)],
                [
                    'FP_corset_high_bluegray',
                    VBase4(67 / 255.0, 78 / 255.0, 84 / 255.0, 1.0)],
                [
                    'FP_corset_high_lightblue',
                    VBase4(96 / 255.0, 112 / 255.0, 117 / 255.0, 1.0)],
                [
                    'FP_corset_high_yellow',
                    VBase4(126 / 255.0, 124 / 255.0, 83 / 255.0, 1.0)]],
            [
                [
                    'FP_corset_low_fourlaces',
                    VBase4(142 / 255.0, 78 / 255.0, 18 / 255.0, 1.0)],
                [
                    'FP_corset_low_print',
                    VBase4(110 / 255.0, 130 / 255.0, 150 / 255.0, 1.0)],
                [
                    'FP_corset_low_ribs',
                    VBase4(243 / 255.0, 224 / 255.0, 186 / 255.0, 1.0)],
                [
                    'FP_corset_low_blue_whitecross',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_corset_low_green_goldbuttons',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_corset_low_white_redvest',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'FP_navy_vest',
                    VBase4(183 / 255.0, 177 / 255.0, 165 / 255.0, 1.0)]]],
        'COAT': [
            [
                [
                    'FP_none',
                    VBase4(1.0, 1.0, 1.0, 1.0)]],
            [
                [
                    'FP_coat_long_patchwork',
                    VBase4(189 / 255.0, 178 / 255.0, 145 / 255.0, 1.0)],
                [
                    'FP_coat_long_2button',
                    VBase4(179 / 255.0, 155 / 255.0, 130 / 255.0, 1.0)],
                [
                    'FP_coat_long_3buttonstripes',
                    VBase4(85 / 255.0, 94 / 255.0, 97 / 255.0, 1.0)],
                [
                    'FP_coat_long_pockets',
                    VBase4(126 / 255.0, 81 / 255.0, 70 / 255.0, 1.0)],
                [
                    'FP_coat_long_browngold',
                    VBase4(64 / 255.0, 51 / 255.0, 27 / 255.0, 1.0)],
                [
                    'FP_coat_long_black_whitesleeves',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_coat_long_blue_white_collar',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_coat_long_red_whitesleeves',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_coat_long_purple',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_coat_long_advanced_outfit',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'FP_coat_short_crocodileskin',
                    VBase4(104 / 255.0, 102 / 255.0, 68 / 255.0, 1.0)],
                [
                    'FP_coat_short_buttons',
                    VBase4(83 / 255.0, 81 / 255.0, 77 / 255.0, 1.0)],
                [
                    'FP_coat_short_pockets',
                    VBase4(134 / 255.0, 110 / 255.0, 80 / 255.0, 1.0)],
                [
                    'FP_coat_short_stripes',
                    VBase4(153 / 255.0, 131 / 255.0, 95 / 255.0, 1.0)],
                [
                    'FP_coat_short_bluegold',
                    VBase4(40 / 255.0, 45 / 255.0, 56 / 255.0, 1.0)],
                [
                    'FP_coat_short_blue_black_trim',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_coat_short_gold_black_trim',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_coat_short_grey_gold_buttons',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_coat_short_white_gold_filagree',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'FP_navy_coat',
                    VBase4(148 / 255.0, 29 / 255.0, 29 / 255.0, 1.0)]]],
        'PANT': [
            [
                [
                    'FP_pant_short_pants_patchwork',
                    VBase4(109 / 255.0, 119 / 255.0, 114 / 255.0, 1.0)],
                [
                    'FP_pant_short_pants_4buttonflap',
                    VBase4(88 / 255.0, 76 / 255.0, 60 / 255.0, 1.0)],
                [
                    'FP_pant_short_pants_frontties',
                    VBase4(54 / 255.0, 58 / 255.0, 58 / 255.0, 1.0)],
                [
                    'FP_pant_short_pants_largesidestripe',
                    VBase4(81 / 255.0, 65 / 255.0, 66 / 255.0, 1.0)],
                [
                    'FP_pant_short_pants_stitch',
                    VBase4(116 / 255.0, 110 / 255.0, 89 / 255.0, 1.0)],
                [
                    'FP_pant_short_pants_striped',
                    VBase4(151 / 255.0, 133 / 255.0, 106 / 255.0, 1.0)],
                [
                    'FP_pant_short_pants_red',
                    VBase4(90 / 255.0, 27 / 255.0, 27 / 255.0, 1.0)],
                [
                    'FP_pant_short_pants_blue_goldbuttons',
                    VBase4(22 / 255.0, 43 / 255.0, 58 / 255.0, 1.0)],
                [
                    'FP_pant_short_pants_brightred',
                    VBase4(92 / 255.0, 13 / 255.0, 12 / 255.0, 1.0)],
                [
                    'FP_pant_short_pants_brown',
                    VBase4(58 / 255.0, 53 / 255.0, 39 / 255.0, 1.0)],
                [
                    'FP_pant_short_pants_green_goldbuttons',
                    VBase4(48 / 255.0, 74 / 255.0, 32 / 255.0, 1.0)],
                [
                    'FP_pant_short_pants_greenstripes',
                    VBase4(23 / 255.0, 44 / 255.0, 43 / 255.0, 1.0)],
                [
                    'FP_pant_short_pants_purple',
                    VBase4(43 / 255.0, 29 / 255.0, 42 / 255.0, 1.0)],
                [
                    'FP_pant_short_pants_blue_basic_outfit',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_pant_short_pants_advanced_outfit',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_pant_short_pants_intermediate_outfit',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'FP_pant_shorts_patchwork',
                    VBase4(53 / 255.0, 44 / 255.0, 30 / 255.0, 1.0)],
                [
                    'FP_pant_shorts_fronttie',
                    VBase4(69 / 255.0, 73 / 255.0, 77 / 255.0, 1.0)],
                [
                    'FP_pant_shorts_lightcloth',
                    VBase4(110 / 255.0, 94 / 255.0, 82 / 255.0, 1.0)],
                [
                    'FP_pant_shorts_sidebuttons',
                    VBase4(56 / 255.0, 59 / 255.0, 39 / 255.0, 1.0)],
                [
                    'FP_pant_shorts_sideties',
                    VBase4(78 / 255.0, 57 / 255.0, 51 / 255.0, 1.0)],
                [
                    'zomb_pant_shorts_sidebuttons',
                    VBase4(144 / 255.0, 135 / 255.0, 111 / 255.0, 1.0)],
                [
                    'FP_pant_shorts_greed_sidebutton',
                    VBase4(73 / 255.0, 80 / 255.0, 45 / 255.0, 1.0)],
                [
                    'FP_pant_shorts_blue_stripes',
                    VBase4(44 / 255.0, 59 / 255.0, 70 / 255.0, 1.0)],
                [
                    'FP_pant_shorts_brownsilver',
                    VBase4(71 / 255.0, 54 / 255.0, 43 / 255.0, 1.0)],
                [
                    'FP_pant_shorts_pinkgold',
                    VBase4(96 / 255.0, 49 / 255.0, 53 / 255.0, 1.0)],
                [
                    'FP_pant_shorts_purplegold',
                    VBase4(69 / 255.0, 55 / 255.0, 99 / 255.0, 1.0)],
                [
                    'FP_pant_shorts_redblack',
                    VBase4(33 / 255.0, 37 / 255.0, 41 / 255.0, 1.0)],
                [
                    'FP_pant_shorts_redgold',
                    VBase4(117 / 255.0, 20 / 255.0, 20 / 255.0, 1.0)]],
            [
                [
                    'FP_pant_skirt_tan',
                    VBase4(176 / 255.0, 165 / 255.0, 128 / 255.0, 1.0)],
                [
                    'FP_pant_skirt_patchwork',
                    VBase4(107 / 255.0, 103 / 255.0, 67 / 255.0, 1.0)],
                [
                    'FP_pant_skirt_layered',
                    VBase4(110 / 255.0, 63 / 255.0, 51 / 255.0, 1.0)],
                [
                    'FP_pant_skirt_leathertrim',
                    VBase4(151 / 255.0, 138 / 255.0, 99 / 255.0, 1.0)],
                [
                    'FP_pant_skirt_slip',
                    VBase4(187 / 255.0, 179 / 255.0, 160 / 255.0, 1.0)],
                [
                    'FP_pant_skirt_plain',
                    VBase4(115 / 255.0, 132 / 255.0, 137 / 255.0, 1.0)],
                [
                    'FP_pant_skirt_print',
                    VBase4(100 / 255.0, 123 / 255.0, 110 / 255.0, 1.0)],
                [
                    'FP_pant_skirt_red',
                    VBase4(94 / 255.0, 28 / 255.0, 26 / 255.0, 1.0)],
                [
                    'FP_pant_skirt_brown',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_pant_skirt_green',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_pant_skirt_lightblue',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_pant_skirt_pink',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_pant_skirt_red_whitebelt',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_pant_skirt_yellow',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'FP_gypsy_dress_a',
                    VBase4(151 / 255.0, 85 / 255.0, 23 / 255.0, 1.0)],
                [
                    'FP_gypsy_dress_b',
                    VBase4(86 / 255.0, 43 / 255.0, 29 / 255.0, 1.0)]],
            [
                [
                    'FP_bartender_dress_a',
                    VBase4(79 / 255.0, 89 / 255.0, 115 / 255.0, 1.0)],
                [
                    'FP_shopkeeps_dress_a',
                    VBase4(79 / 255.0, 89 / 255.0, 115 / 255.0, 1.0)]],
            [
                [
                    'FP_navy_pants',
                    VBase4(230 / 255.0, 230 / 255.0, 230 / 255.0, 1.0)]]],
        'BELT': [
            [
                [
                    'FP_none',
                    VBase4(1.0, 1.0, 1.0, 1.0)]],
            [
                [
                    'FP_belt_sash_goldbuckle',
                    VBase4(97 / 255.0, 90 / 255.0, 85 / 255.0, 1.0)]],
            [
                [
                    'FP_belt_sash_pattern',
                    VBase4(46 / 255.0, 48 / 255.0, 17 / 255.0, 1.0)]],
            [
                [
                    'FP_belt_sash_tassles',
                    VBase4(58 / 255.0, 42 / 255.0, 26 / 255.0, 1.0)]],
            [
                [
                    'FP_belt_sash_goldbuckle',
                    VBase4(97 / 255.0, 90 / 255.0, 85 / 255.0, 1.0)]],
            [
                [
                    'FP_belt_strap_black+FP_belt_buckle_square_dark',
                    VBase4(24 / 255.0, 10 / 255.0, 2 / 255.0, 1.0)]],
            [
                [
                    'FP_belt_strap_RivetsSkullBuckle+FP_belt_buckle_square',
                    VBase4(31 / 255.0, 23 / 255.0, 13 / 255.0, 1.0)]],
            [
                [
                    'FP_belt_strap_cloth+FP_belt_buckle_corners',
                    VBase4(35 / 255.0, 39 / 255.0, 4 / 255.0, 1.0)]],
            [
                [
                    'FP_belt_strap_studs+FP_belt_buckle_circles',
                    VBase4(41 / 255.0, 35 / 255.0, 19 / 255.0, 1.0)]],
            [
                [
                    'FP_belt_strap_ties+FP_belt_buckle_pattern',
                    VBase4(49 / 255.0, 33 / 255.0, 12 / 255.0, 1.0)]],
            [
                [
                    'FP_belt_strap_weave+FP_belt_buckle_weave',
                    VBase4(52 / 255.0, 43 / 255.0, 27 / 255.0, 1.0)]],
            [
                [
                    'FP_belt_sash_blue_belt',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'FP_belt_sash_red_furtrim',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'FP_belt_strap_square_brown_silvertrim+FP_belt_buckle_square_brown_silvertrim',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'FP_belt_strap_square_gold_design+FP_belt_buckle_square_gold_design',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'FP_belt_sash_red_basic_outfit',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'FP_belt_strap_square_advanced_outfit+FP_belt_buckle_square_advanced_outfit',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'FP_belt_strap_square_intermediate_outfit+FP_belt_buckle_square_intermediate_outfit',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]]],
        'SHOE': [
            [
                [
                    'FP_none',
                    VBase4(1.0, 1.0, 1.0, 1.0)]],
            [
                [
                    'FP_shoe_short_boots_celticpattern',
                    VBase4(32 / 255.0, 28 / 255.0, 23 / 255.0, 1.0)],
                [
                    'FP_shoe_short_boots_3buckle',
                    VBase4(33 / 255.0, 27 / 255.0, 11 / 255.0, 1.0)],
                [
                    'FP_shoe_short_boots_plain',
                    VBase4(34 / 255.0, 25 / 255.0, 18 / 255.0, 1.0)],
                [
                    'FP_shoe_short_boots_weave',
                    VBase4(34 / 255.0, 31 / 255.0, 20 / 255.0, 1.0)],
                [
                    'FP_shoe_short_boots_black_torntop',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_shoe_short_boots_brown_sidebuttons',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_shoe_short_boots_brown_sidelaces',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_shoe_short_boots_brown_stitching',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_shoe_short_boots_blue_basic_outfit',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_shoe_short_boots_advanced_outfit',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'FP_shoe_medium_boots_BuckleSkullSole',
                    VBase4(23 / 255.0, 14 / 255.0, 5 / 255.0, 1.0)],
                [
                    'FP_shoe_medium_boots_studs',
                    VBase4(23 / 255.0, 23 / 255.0, 20 / 255.0, 1.0)],
                [
                    'FP_shoe_medium_boots_ties',
                    VBase4(9 / 255.0, 8 / 255.0, 7 / 255.0, 1.0)],
                [
                    'FP_shoe_medium_boots_weavebuckle',
                    VBase4(18 / 255.0, 12 / 255.0, 1 / 255.0, 1.0)],
                [
                    'FP_shoe_medium_boots_black-topstitch',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_shoe_medium_boots_brown-sidestitch',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_shoe_medium_boots_orange',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_shoe_medium_boots_purple',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'FP_shoe_knee_high_boots_brown',
                    VBase4(20 / 255.0, 17 / 255.0, 14 / 255.0, 1.0)],
                [
                    'FP_shoe_knee_high_boots_smallchains',
                    VBase4(5 / 255.0, 5 / 255.0, 9 / 255.0, 1.0)],
                [
                    'FP_shoe_knee_high_boots_buckle',
                    VBase4(17 / 255.0, 15 / 255.0, 12 / 255.0, 1.0)],
                [
                    'FP_shoe_knee_high_boots_plain',
                    VBase4(47 / 255.0, 35 / 255.0, 14 / 255.0, 1.0)],
                [
                    'FP_shoe_knee_high_boots_ties',
                    VBase4(36 / 255.0, 24 / 255.0, 8 / 255.0, 1.0)],
                [
                    'FP_shoe_knee_high_boots_blue',
                    VBase4(30 / 255.0, 44 / 255.0, 56 / 255.0, 1.0)],
                [
                    'FP_shoe_knee_high_boots_burgundy',
                    VBase4(54 / 255.0, 16 / 255.0, 21 / 255.0, 1.0)],
                [
                    'FP_shoe_knee_high_boots_lightgreen',
                    VBase4(72 / 255.0, 82 / 255.0, 51 / 255.0, 1.0)],
                [
                    'FP_shoe_knee_high_boots_tan',
                    VBase4(87 / 255.0, 70 / 255.0, 37 / 255.0, 1.0)]],
            [
                [
                    'FP_shoe_tall_boots_celticstraps',
                    VBase4(17 / 255.0, 16 / 255.0, 11 / 255.0, 1.0)],
                [
                    'FP_shoe_tall_boots_1buckle',
                    VBase4(25 / 255.0, 22 / 255.0, 17 / 255.0, 1.0)],
                [
                    'FP_shoe_tall_boots_plain',
                    VBase4(60 / 255.0, 42 / 255.0, 16 / 255.0, 1.0)],
                [
                    'FP_shoe_tall_boots_weave',
                    VBase4(30 / 255.0, 17 / 255.0, 14 / 255.0, 1.0)],
                [
                    'FP_shoe_tall_boots_blue_stitches',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_shoe_tall_boots_red_anklebelts',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_shoe_tall_boots_teal_stitches',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)],
                [
                    'FP_shoe_tall_boots_intermediate_outfit',
                    VBase4(255 / 255.0, 255 / 255.0, 255 / 255.0, 1.0)]],
            [
                [
                    'FP_navy_shoes',
                    VBase4(63 / 255.0, 58 / 255.0, 48 / 255.0, 1.0)]]]}}
navy_coat_geoms = [
    3,
    4]
shopkeep_pant_geoms = [
    6]
quickConfirmSet = set()
for gender in list(textures.keys()):
    if gender == 'MALE':
        genderName = 'm'
    elif gender == 'FEMALE':
        genderName = 'f'
    
    clothing = textures[gender]
    for clothingType in list(clothing.keys()):
        models = clothing[clothingType]
        for i in range(len(models)):
            for j in range(len(models[i])):
                quickConfirmSet.add((genderName, clothingType, i, j))


def printList():
    for gender in textures:
        for type in textures[gender]:
            for item in textures[gender][type]:
                for subtype in item:
                    outVal = [
                        int(subtype[1].getX() * 256),
                        int(subtype[1].getY() * 256),
                        int(subtype[1].getZ() * 256)]
                    print(str(subtype[0]), str(outVal))


def printList2():
    for gender in textures:
        for type in textures[gender]:
            for item in textures[gender][type]:
                for subtype in item:
                    print(str(subtype[0]))


HAT_START_RANGE_MALE = 0
SHIRT_START_RANGE_MALE = 10000
VEST_START_RANGE_MALE = 20000
COAT_START_RANGE_MALE = 30000
PANT_START_RANGE_MALE = 40000
BELT_START_RANGE_MALE = 50000
SOCK_START_RANGE_MALE = 60000
SHOE_START_RANGE_MALE = 70000
HAT_START_RANGE_FEMALE = 80000
SHIRT_START_RANGE_FEMALE = 90000
VEST_START_RANGE_FEMALE = 100000
COAT_START_RANGE_FEMALE = 110000
PANT_START_RANGE_FEMALE = 130000
BELT_START_RANGE_FEMALE = 140000
SOCK_START_RANGE_FEMALE = 150000
SHOE_START_RANGE_FEMALE = 160000
clothingLookupTable = {}


def generateLookup():
    global clothingLookupTable
    hatCounterMale = HAT_START_RANGE_MALE
    shirtCounterMale = SHIRT_START_RANGE_MALE
    vestCounterMale = VEST_START_RANGE_MALE
    coatCounterMale = COAT_START_RANGE_MALE
    pantCounterMale = PANT_START_RANGE_MALE
    beltCounterMale = BELT_START_RANGE_MALE
    sockCounterMale = SOCK_START_RANGE_MALE
    shoeCounterMale = SHOE_START_RANGE_MALE
    hatCounterFemale = HAT_START_RANGE_FEMALE
    shirtCounterFemale = SHIRT_START_RANGE_FEMALE
    vestCounterFemale = VEST_START_RANGE_FEMALE
    coatCounterFemale = COAT_START_RANGE_FEMALE
    pantCounterFemale = PANT_START_RANGE_FEMALE
    beltCounterFemale = BELT_START_RANGE_FEMALE
    sockCounterFemale = SOCK_START_RANGE_FEMALE
    shoeCounterFemale = SHOE_START_RANGE_FEMALE
    for item in SELECTION_CHOICES['DEFAULT']['MALE']['HAT']:
        for tex in SELECTION_CHOICES['DEFAULT']['MALE']['HAT'][item]:
            clothingLookupTable[hatCounterMale] = [
                HAT,
                item,
                tex,
                0]
            hatCounterMale += 1

    for item in SELECTION_CHOICES['DEFAULT']['MALE']['SHIRT']:
        for tex in SELECTION_CHOICES['DEFAULT']['MALE']['SHIRT'][item]:
            clothingLookupTable[shirtCounterMale] = [
                SHIRT,
                item,
                tex,
                0]
            shirtCounterMale += 1

    for item in SELECTION_CHOICES['DEFAULT']['MALE']['VEST']:
        for tex in SELECTION_CHOICES['DEFAULT']['MALE']['VEST'][item]:
            clothingLookupTable[vestCounterMale] = [
                VEST,
                item,
                tex,
                0]
            vestCounterMale += 1
    
    for item in SELECTION_CHOICES['DEFAULT']['MALE']['COAT']:
        for tex in SELECTION_CHOICES['DEFAULT']['MALE']['COAT'][item]:
            clothingLookupTable[coatCounterMale] = [
                COAT,
                item,
                tex,
                0]
            coatCounterMale += 1

    for item in SELECTION_CHOICES['DEFAULT']['MALE']['PANT']:
        for tex in SELECTION_CHOICES['DEFAULT']['MALE']['PANT'][item]:
            clothingLookupTable[pantCounterMale] = [
                PANT,
                item,
                tex,
                0]
            pantCounterMale += 1
    
    for item in SELECTION_CHOICES['DEFAULT']['MALE']['BELT']:
        for tex in SELECTION_CHOICES['DEFAULT']['MALE']['BELT'][item]:
            clothingLookupTable[beltCounterMale] = [
                BELT,
                item,
                tex,
                0]
            beltCounterMale += 1

    for item in SELECTION_CHOICES['DEFAULT']['MALE']['SHOE']:
        for tex in SELECTION_CHOICES['DEFAULT']['MALE']['SHOE'][item]:
            clothingLookupTable[shoeCounterMale] = [
                SHOE,
                item,
                tex,
                0]
            shoeCounterMale += 1

    for item in SELECTION_CHOICES['DEFAULT']['FEMALE']['HAT']:
        for tex in SELECTION_CHOICES['DEFAULT']['FEMALE']['HAT'][item]:
            clothingLookupTable[hatCounterFemale] = [
                HAT,
                item,
                tex,
                0]
            hatCounterFemale += 1

    for item in SELECTION_CHOICES['DEFAULT']['FEMALE']['SHIRT']:
        for tex in SELECTION_CHOICES['DEFAULT']['FEMALE']['SHIRT'][item]:
            clothingLookupTable[shirtCounterFemale] = [
                SHIRT,
                item,
                tex,
                0]
            shirtCounterFemale += 1
    
    for item in SELECTION_CHOICES['DEFAULT']['FEMALE']['VEST']:
        for tex in SELECTION_CHOICES['DEFAULT']['FEMALE']['VEST'][item]:
            clothingLookupTable[vestCounterFemale] = [
                VEST,
                item,
                tex,
                0]
            vestCounterFemale += 1

    for item in SELECTION_CHOICES['DEFAULT']['FEMALE']['COAT']:
        for tex in SELECTION_CHOICES['DEFAULT']['FEMALE']['COAT'][item]:
            clothingLookupTable[coatCounterFemale] = [
                COAT,
                item,
                tex,
                0]
            coatCounterFemale += 1

    for item in SELECTION_CHOICES['DEFAULT']['FEMALE']['PANT']:
        for tex in SELECTION_CHOICES['DEFAULT']['FEMALE']['PANT'][item]:
            clothingLookupTable[pantCounterFemale] = [
                PANT,
                item,
                tex,
                0]
            pantCounterFemale += 1

    for item in SELECTION_CHOICES['DEFAULT']['FEMALE']['BELT']:
        for tex in SELECTION_CHOICES['DEFAULT']['FEMALE']['BELT'][item]:
            clothingLookupTable[beltCounterFemale] = [
                BELT,
                item,
                tex,
                0]
            beltCounterFemale += 1

    for item in SELECTION_CHOICES['DEFAULT']['FEMALE']['SHOE']:
        for tex in SELECTION_CHOICES['DEFAULT']['FEMALE']['SHOE'][item]:
            clothingLookupTable[shoeCounterFemale] = [
                SHOE,
                item,
                tex,
                0]
            shoeCounterFemale += 1

generateLookup()

def getRandomClothingColor(level):
    max_drop = 30
    if random.randint(0, 10) < 8:
        max_drop = 20 + int(level / 4)
        if max_drop > 30:
            max_drop = 30

    return random.randint(20, max_drop)


def getRandomClothingDrop(level, gender):
    if gender == 'm':
        itemId = random.choice(dropItems['m'])
    else:
        itemId = random.choice(dropItems['f'])
    return itemId


def getItemById(itemId):
    if itemId in list(UNIQUE_ID.keys()):
        return UNIQUE_ID[itemId]
    else:
        return 0

TYPE_INDEX = 0

def getItemType(itemId):
    item = getItemById(itemId)
    return item[TYPE_INDEX]


def getItemTypeName(itemId):
    itemType = getItemType(itemId)
    if itemType == 0:
        return PLocalizer.Hat
    elif itemType == 1:
        return PLocalizer.Shirt
    elif itemType == 2:
        return PLocalizer.Vest
    elif itemType == 3:
        return PLocalizer.Coat
    elif itemType == 4:
        return PLocalizer.Pants
    elif itemType == 5:
        return PLocalizer.Belt
    elif itemType == 6:
        return PLocalizer.Belt
    else:
        return PLocalizer.Shoes

newClothing = [
    5,
    6,
    7,
    8,
    9,
    10,
    10019,
    10020,
    10021,
    10022,
    10023,
    10024,
    10025,
    10026,
    10027,
    10028,
    10029,
    20008,
    20009,
    20010,
    20011,
    20012,
    20013,
    20014,
    30003,
    30004,
    30005,
    30006,
    30007,
    30008,
    30009,
    30010,
    30011,
    30012,
    30013,
    30014,
    30015,
    30016,
    30017,
    30018,
    40015,
    40016,
    40017,
    40018,
    80005,
    80006,
    80007,
    90019,
    90020,
    90021,
    90022,
    90023,
    90024,
    90025,
    90026,
    90027,
    90028,
    90029,
    90030,
    90031,
    100015,
    100016,
    100017,
    100018,
    100019,
    100020,
    100021,
    100022,
    100023,
    100024,
    100025,
    100026,
    100027,
    100028,
    100029,
    110006,
    110007,
    110008,
    110009,
    110010,
    130018,
    130019,
    130020,
    130021,
    130022,
    130023,
    130024,
    160018,
    160019,
    160020,
    160021]
stores = {
    PiratesGlobals.PORT_ROYAL_ALL: {
        1: [
            0],
        2: [
            0],
        3: [
            0],
        4: [
            0],
        5: [
            0],
        6: [
            0],
        7: [
            0],
        8: [
            0],
        9: [
            0],
        10: [
            0],
        14: [
            0],
        10000: [
            0],
        10001: [
            0],
        10002: [
            0],
        10003: [
            0],
        10004: [
            0],
        10005: [
            0],
        10006: [
            0],
        10007: [
            0],
        10008: [
            0],
        10009: [
            0],
        10010: [
            0],
        10011: [
            0],
        10012: [
            0],
        10013: [
            0],
        10014: [
            0],
        10015: [
            0],
        10016: [
            0],
        10017: [
            0],
        10018: [
            0],
        10019: [
            0],
        10020: [
            0],
        10021: [
            0],
        10022: [
            0],
        10023: [
            0],
        10024: [
            0],
        10025: [
            0],
        10026: [
            0],
        10027: [
            0],
        10028: [
            0],
        10029: [
            0],
        20001: [
            0],
        20002: [
            0],
        20003: [
            0],
        20004: [
            0],
        20005: [
            0],
        20006: [
            0],
        20007: [
            0],
        20008: [
            0],
        20009: [
            0],
        20010: [
            0],
        20011: [
            0],
        20012: [
            0],
        20013: [
            0],
        20014: [
            0],
        30001: [
            0],
        30002: [
            0],
        30003: [
            0],
        30004: [
            0],
        30005: [
            0],
        30006: [
            0],
        30007: [
            0],
        30008: [
            0],
        30009: [
            0],
        30010: [
            0],
        30011: [
            0],
        30012: [
            0],
        30013: [
            0],
        30014: [
            0],
        30015: [
            0],
        30016: [
            0],
        30017: [
            0],
        30018: [
            0],
        40000: [
            0],
        40001: [
            0],
        40002: [
            0],
        40003: [
            0],
        40004: [
            0],
        40005: [
            0],
        40006: [
            0],
        40007: [
            0],
        40008: [
            0],
        40009: [
            0],
        40010: [
            0],
        40011: [
            0],
        40012: [
            0],
        40013: [
            0],
        40014: [
            0],
        40015: [
            0],
        40016: [
            0],
        40017: [
            0],
        40018: [
            0],
        50001: [
            0],
        50002: [
            0],
        50003: [
            0],
        50004: [
            0],
        50005: [
            0],
        70001: [
            0],
        70002: [
            0],
        70003: [
            0],
        70004: [
            0],
        70005: [
            0],
        70006: [
            0],
        70007: [
            0],
        70008: [
            0],
        80001: [
            0],
        80002: [
            0],
        80003: [
            0],
        80004: [
            0],
        80005: [
            0],
        80006: [
            0],
        80007: [
            0],
        80011: [
            0],
        90001: [
            0],
        90002: [
            0],
        90003: [
            0],
        90004: [
            0],
        90005: [
            0],
        90006: [
            0],
        90007: [
            0],
        90008: [
            0],
        90009: [
            0],
        90010: [
            0],
        90011: [
            0],
        90012: [
            0],
        90013: [
            0],
        90014: [
            0],
        90015: [
            0],
        90016: [
            0],
        90017: [
            0],
        90018: [
            0],
        90019: [
            0],
        90020: [
            0],
        90021: [
            0],
        90022: [
            0],
        90023: [
            0],
        90024: [
            0],
        90025: [
            0],
        90026: [
            0],
        90027: [
            0],
        90028: [
            0],
        90029: [
            0],
        90030: [
            0],
        90031: [
            0],
        90032: [
            0],
        100001: [
            0],
        100002: [
            0],
        100003: [
            0],
        100004: [
            0],
        100005: [
            0],
        100006: [
            0],
        100007: [
            0],
        100008: [
            0],
        100009: [
            0],
        100010: [
            0],
        100011: [
            0],
        100012: [
            0],
        100013: [
            0],
        100014: [
            0],
        100015: [
            0],
        100016: [
            0],
        100017: [
            0],
        100018: [
            0],
        100019: [
            0],
        100020: [
            0],
        100021: [
            0],
        100022: [
            0],
        100023: [
            0],
        100024: [
            0],
        100025: [
            0],
        100026: [
            0],
        100027: [
            0],
        100028: [
            0],
        100029: [
            0],
        110001: [
            0],
        110002: [
            0],
        110003: [
            0],
        110004: [
            0],
        110005: [
            0],
        110006: [
            0],
        110007: [
            0],
        110008: [
            0],
        110009: [
            0],
        110010: [
            0],
        130000: [
            0],
        130001: [
            0],
        130002: [
            0],
        130003: [
            0],
        130004: [
            0],
        130005: [
            0],
        130006: [
            0],
        130007: [
            0],
        130008: [
            0],
        130009: [
            0],
        130010: [
            0],
        130011: [
            0],
        130012: [
            0],
        130013: [
            0],
        130014: [
            0],
        130015: [
            0],
        130016: [
            0],
        130017: [
            0],
        130018: [
            0],
        130019: [
            0],
        130020: [
            0],
        130021: [
            0],
        130022: [
            0],
        130023: [
            0],
        130024: [
            0],
        140001: [
            0],
        140002: [
            0],
        140003: [
            0],
        140004: [
            0],
        140005: [
            0],
        140006: [
            0],
        140007: [
            0],
        140008: [
            0],
        140009: [
            0],
        140010: [
            0],
        160001: [
            0],
        160002: [
            0],
        160003: [
            0],
        160004: [
            0],
        160005: [
            0],
        160006: [
            0],
        160007: [
            0],
        160008: [
            0],
        160009: [
            0],
        160010: [
            0],
        160011: [
            0],
        160012: [
            0],
        160013: [
            0],
        160014: [
            0],
        160015: [
            0],
        160016: [
            0],
        160017: [
            0],
        160018: [
            0],
        160019: [
            0],
        160020: [
            0],
        160021: [
            0] },
    PiratesGlobals.PORT_ROYAL_DEFAULTS: {
        1: [
            0],
        2: [
            0],
        3: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        4: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        6: [
            0],
        14: [
            0],
        10000: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        10001: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        10002: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        10003: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        10004: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        10005: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        10006: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        10007: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        10008: [
            0],
        10009: [
            0],
        10010: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        10011: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        10012: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        10013: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        10014: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        10015: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        10016: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        10017: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        10018: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        20001: [
            0],
        20002: [
            0],
        20003: [
            0],
        20004: [
            0],
        20005: [
            0],
        20006: [
            0],
        20007: [
            0],
        30001: [
            0],
        30002: [
            0],
        40000: [
            0],
        40001: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        40002: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        40003: [
            0],
        40004: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        40005: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        40006: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        40007: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        40008: [
            0],
        40009: [
            0],
        40010: [
            0],
        40011: [
            0],
        40012: [
            0],
        40013: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        40014: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        50001: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        50002: [
            0],
        50003: [
            0],
        50004: [
            0],
        50005: [
            0],
        70001: [
            0],
        70002: [
            0],
        70003: [
            0],
        70004: [
            0],
        70005: [
            0],
        70006: [
            0],
        70007: [
            0],
        70008: [
            0],
        80001: [
            0],
        80002: [
            0],
        80003: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        80004: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        80005: [
            0],
        80011: [
            0],
        90032: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        90001: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        90002: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        90003: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        90004: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        90005: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        90006: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        90007: [
            0],
        90008: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        90009: [
            0],
        90010: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        90011: [
            0],
        90012: [
            0],
        90013: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        90014: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        90015: [
            0],
        90016: [
            0],
        90017: [
            0],
        90018: [
            0],
        100001: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        100002: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        100003: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        100004: [
            0],
        100005: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        100006: [
            0],
        100007: [
            0],
        100008: [
            0],
        100009: [
            0],
        100010: [
            0],
        100011: [
            0],
        100012: [
            0],
        100013: [
            0],
        100014: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        110001: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        110002: [
            0],
        110003: [
            0],
        110004: [
            0],
        110005: [
            0],
        130000: [
            0],
        130001: [
            0],
        130002: [
            0],
        130003: [
            0],
        130004: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        130005: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        130006: [
            0],
        130007: [
            0],
        130008: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        130009: [
            0],
        130010: [
            0],
        130011: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        130012: [
            0],
        130013: [
            0],
        130014: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        130015: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        130016: [
            0],
        130017: [
            0],
        140001: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        140002: [
            0],
        140003: [
            0],
        140004: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        140005: [
            0],
        140006: [
            0],
        140007: [
            0],
        140008: [
            0],
        140009: [
            0],
        140010: [
            0],
        160001: [
            0],
        160002: [
            0],
        160003: [
            0],
        160004: [
            0],
        160005: [
            0],
        160006: [
            0],
        160007: [
            0],
        160008: [
            0],
        160009: [
            0],
        160010: [
            0],
        160011: [
            0],
        160012: [
            0],
        160013: [
            0],
        160014: [
            0],
        160015: [
            0],
        160016: [
            0],
        160017: [
            0] },
    PiratesGlobals.PORT_ROYAL_THRIFT: {
        1: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        4: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        10: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        6: [
            0],
        14: [
            0],
        10000: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        10002: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        10011: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        10012: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        10019: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        10020: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        10021: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        10022: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        20001: [
            0],
        20002: [
            0],
        20003: [
            0],
        20008: [
            0],
        20009: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        30001: [
            0],
        30002: [
            0],
        30003: [
            0],
        30004: [
            0],
        30005: [
            0],
        30006: [
            0],
        30007: [
            0],
        30008: [
            0],
        30009: [
            0],
        30010: [
            0],
        30011: [
            0],
        30012: [
            0],
        30013: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        30014: [
            0],
        30015: [
            0],
        30016: [
            0],
        30017: [
            0],
        30018: [
            0],
        40000: [
            0],
        40001: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        40004: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        40007: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        40015: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        50001: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        50005: [
            0],
        70001: [
            0],
        70002: [
            0],
        70003: [
            0],
        80004: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        80006: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        80007: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        80005: [
            0],
        80011: [
            0],
        90001: [
            0],
        90002: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        90003: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        90005: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        90032: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        90019: [
            0],
        90020: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        90021: [
            0],
        100001: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        100002: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        100003: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        100004: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        100014: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        100015: [
            0],
        110001: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        110002: [
            0],
        110006: [
            0],
        110008: [
            0],
        110007: [
            0],
        110009: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        110010: [
            0],
        130000: [
            0],
        130001: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        130002: [
            0],
        130003: [
            0],
        130004: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        130018: [
            0],
        130019: [
            0],
        140001: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        140003: [
            0],
        140004: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        160001: [
            0],
        160002: [
            0],
        160003: [
            0],
        160004: [
            0],
        160018: [
            0] },
    PiratesGlobals.TORTUGA_DEFAULTS: {
        3: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        7: [
            0],
        9: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        6: [
            0],
        14: [
            0],
        10001: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        10003: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        10004: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        10006: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        10007: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        10024: [
            0],
        10025: [
            0],
        10026: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        10027: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        20004: [
            0],
        20005: [
            0],
        20010: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        20013: [
            0],
        30001: [
            0],
        30002: [
            0],
        30003: [
            0],
        30004: [
            0],
        30005: [
            0],
        30006: [
            0],
        30007: [
            0],
        30008: [
            0],
        30009: [
            0],
        30010: [
            0],
        30011: [
            0],
        30012: [
            0],
        30013: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        30014: [
            0],
        30015: [
            0],
        30016: [
            0],
        30017: [
            0],
        30018: [
            0],
        40002: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        40005: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        40008: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        40009: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        40016: [
            0],
        50002: [
            0],
        50004: [
            0],
        70004: [
            0],
        70006: [
            0],
        70007: [
            0],
        70008: [
            0],
        80002: [
            0],
        80003: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        80006: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        80007: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        80005: [
            0],
        80011: [
            0],
        90004: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        90006: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        90007: [
            0],
        90009: [
            0],
        90010: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        90023: [
            0],
        90024: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        90025: [
            0],
        90026: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        100005: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        100006: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        100009: [
            0],
        100010: [
            0],
        100016: [
            0],
        100017: [
            0],
        100018: [
            0],
        100027: [
            0],
        100028: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        100029: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        110003: [
            0],
        110004: [
            0],
        110006: [
            0],
        110008: [
            0],
        110007: [
            0],
        110009: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        110010: [
            0],
        130005: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        130006: [
            0],
        130007: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        130012: [
            0],
        130013: [
            0],
        130020: [
            0],
        130021: [
            0],
        130022: [
            0],
        140002: [
            0],
        140005: [
            0],
        140006: [
            0],
        160005: [
            0],
        160006: [
            0],
        160012: [
            0],
        160013: [
            0],
        160019: [
            0] },
    PiratesGlobals.CUBA_DEFAULTS: {
        3: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        5: [
            0],
        7: [
            0],
        6: [
            0],
        14: [
            0],
        10009: [
            0],
        10010: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        10013: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        10014: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        10016: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        10024: [
            0],
        10025: [
            0],
        10028: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        10029: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        20006: [
            0],
        20010: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        20012: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        30001: [
            0],
        30002: [
            0],
        30003: [
            0],
        30004: [
            0],
        30005: [
            0],
        30006: [
            0],
        30007: [
            0],
        30008: [
            0],
        30009: [
            0],
        30010: [
            0],
        30011: [
            0],
        30012: [
            0],
        30013: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        30014: [
            0],
        30015: [
            0],
        30016: [
            0],
        30017: [
            0],
        30018: [
            0],
        40003: [
            0],
        40010: [
            0],
        40011: [
            0],
        40012: [
            0],
        40014: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        40017: [
            0],
        50002: [
            0],
        50004: [
            0],
        70004: [
            0],
        70006: [
            0],
        70007: [
            0],
        70008: [
            0],
        80002: [
            0],
        80003: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        80006: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        80007: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        80005: [
            0],
        80011: [
            0],
        90008: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        90011: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        90013: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        90014: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        90018: [
            0],
        90027: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        90028: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        90029: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        100007: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        100008: [
            0],
        100011: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        100019: [
            0],
        100020: [
            0],
        100021: [
            0],
        110003: [
            0],
        110004: [
            0],
        110006: [
            0],
        110008: [
            0],
        110007: [
            0],
        110009: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        110010: [
            0],
        130008: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        130009: [
            0],
        130010: [
            0],
        130011: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        130023: [
            0],
        140009: [
            0],
        140010: [
            0],
        160007: [
            0],
        160008: [
            0],
        160009: [
            0],
        160011: [
            0],
        160020: [
            0] },
    PiratesGlobals.DEL_FUEGO_DEFAULTS: {
        2: [
            0],
        8: [
            0],
        6: [
            0],
        14: [
            0],
        10005: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        10008: [
            0],
        10015: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        10017: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        10018: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        10023: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        20007: [
            0],
        20011: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        20014: [
            0],
        30001: [
            0],
        30002: [
            0],
        30003: [
            0],
        30004: [
            0],
        30005: [
            0],
        30006: [
            0],
        30007: [
            0],
        30008: [
            0],
        30009: [
            0],
        30010: [
            0],
        30011: [
            0],
        30012: [
            0],
        30013: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        30014: [
            0],
        30015: [
            0],
        30016: [
            0],
        30017: [
            0],
        30018: [
            0],
        40013: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        40006: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        40018: [
            0],
        50003: [
            0],
        50004: [
            0],
        70005: [
            0],
        80001: [
            0],
        80006: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        80007: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        80005: [
            0],
        80011: [
            0],
        90012: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        90015: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        90016: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        90017: [
            0],
        90022: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        90030: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        90031: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        100012: [
            0],
        100013: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        100014: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        100022: [
            0],
        100023: [
            0],
        100024: [
            0],
        100025: [
            0],
        100026: [
            0],
        110005: [
            0],
        110006: [
            0],
        110008: [
            0],
        110007: [
            0],
        110009: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        110010: [
            0],
        130014: [
            0],
        130015: [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20],
        130016: [
            0],
        130017: [
            0],
        130024: [
            0],
        140007: [
            0],
        140008: [
            0],
        160010: [
            0],
        160014: [
            0],
        160015: [
            0],
        160016: [
            0],
        160017: [
            0],
        160021: [
            0] } }
dropItems = {
    'm': [
        3,
        4,
        9,
        10,
        10000,
        10001,
        10002,
        10003,
        10004,
        10005,
        10006,
        10007,
        10010,
        10011,
        10012,
        10013,
        10014,
        10015,
        10016,
        10017,
        10018,
        10019,
        10020,
        10021,
        10022,
        10023,
        10026,
        10027,
        10028,
        10029,
        20009,
        20010,
        20011,
        20012,
        20014,
        30013,
        40001,
        40002,
        40004,
        40005,
        40006,
        40007,
        40013,
        40014,
        40015,
        50001],
    'f': [
        80003,
        80004,
        80006,
        80007,
        90001,
        90002,
        90003,
        90004,
        90005,
        90006,
        90008,
        90010,
        90013,
        90014,
        90020,
        90022,
        90024,
        90026,
        90027,
        90028,
        90029,
        90030,
        90031,
        90032,
        100001,
        100002,
        100003,
        100005,
        100014,
        100028,
        100029,
        110001,
        110009,
        130004,
        130005,
        130008,
        130011,
        130014,
        130015,
        140001,
        140004] }
BASIC_OUTFIT_PART_A = 0
BASIC_OUTFIT_PART_B = 1
BASIC_OUTFIT_PART_C = 2
BASIC_OUTFIT_PART_D = 3
BASIC_OUTFIT_PART_E = 4
INTERMEDIATE_OUTFIT_PART_A = 5
INTERMEDIATE_OUTFIT_PART_B = 6
INTERMEDIATE_OUTFIT_PART_C = 7
INTERMEDIATE_OUTFIT_PART_D = 8
INTERMEDIATE_OUTFIT_PART_E = 9
INTERMEDIATE_OUTFIT_PART_F = 10
ADVANCED_OUTFIT_PART_A = 11
ADVANCED_OUTFIT_PART_B = 12
ADVANCED_OUTFIT_PART_C = 13
ADVANCED_OUTFIT_PART_D = 14
ADVANCED_OUTFIT_PART_E = 15
ADVANCED_OUTFIT_PART_F = 16
ADVANCED_OUTFIT_PART_G = 17
questDrops = {
    BASIC_OUTFIT_PART_A: {
        'm': [
            11,
            0],
        'f': [
            80008,
            0] },
    BASIC_OUTFIT_PART_B: {
        'm': [
            10030,
            0],
        'f': [
            90033,
            0] },
    BASIC_OUTFIT_PART_C: {
        'm': [
            40019,
            0],
        'f': [
            130025,
            0] },
    BASIC_OUTFIT_PART_D: {
        'm': [
            50006,
            0],
        'f': [
            140011,
            0] },
    BASIC_OUTFIT_PART_E: {
        'm': [
            70009,
            0],
        'f': [
            160022,
            0] },
    INTERMEDIATE_OUTFIT_PART_A: {
        'm': [
            12,
            0],
        'f': [
            80009,
            0] },
    INTERMEDIATE_OUTFIT_PART_B: {
        'm': [
            10031,
            0],
        'f': [
            90034,
            0] },
    INTERMEDIATE_OUTFIT_PART_C: {
        'm': [
            20015,
            0],
        'f': [
            100030,
            0] },
    INTERMEDIATE_OUTFIT_PART_D: {
        'm': [
            40020,
            0],
        'f': [
            130026,
            0] },
    INTERMEDIATE_OUTFIT_PART_E: {
        'm': [
            50007,
            0],
        'f': [
            140012,
            0] },
    INTERMEDIATE_OUTFIT_PART_F: {
        'm': [
            70010,
            0],
        'f': [
            160023,
            0] },
    ADVANCED_OUTFIT_PART_A: {
        'm': [
            13,
            0],
        'f': [
            80010,
            0] },
    ADVANCED_OUTFIT_PART_B: {
        'm': [
            10032,
            0],
        'f': [
            90035,
            0] },
    ADVANCED_OUTFIT_PART_C: {
        'm': [
            20016,
            0],
        'f': [
            100031,
            0] },
    ADVANCED_OUTFIT_PART_D: {
        'm': [
            30019,
            0],
        'f': [
            110011,
            0] },
    ADVANCED_OUTFIT_PART_E: {
        'm': [
            40021,
            0],
        'f': [
            130027,
            0] },
    ADVANCED_OUTFIT_PART_F: {
        'm': [
            50008,
            0],
        'f': [
            140013,
            0] },
    ADVANCED_OUTFIT_PART_G: {
        'm': [
            70011,
            0],
        'f': [
            160024,
            0] } }
quest_items = [
    11,
    10030,
    40019,
    50006,
    70009,
    12,
    10031,
    20015,
    40020,
    50007,
    70010,
    13,
    10032,
    20016,
    30019,
    40021,
    50008,
    70011,
    80008,
    90033,
    130025,
    140011,
    160022,
    80009,
    90034,
    100030,
    130026,
    140012,
    160023,
    80010,
    90035,
    100031,
    110011,
    130027,
    140013,
    160024]
colorCostScaler = {
  0: 1.0,
  1: 1.1,
  2: 1.2,
  3: 1.3,
  4: 1.4,
  5: 1.5,
  6: 1.6,
  7: 1.7,
  8: 1.8,
  9: 1.9,
  10: 2.0,
  11: 2.1,
  12: 2.2,
  13: 2.3,
  14: 2.4,
  15: 2.5,
  16: 2.6,
  17: 2.7,
  18: 2.8,
  19: 2.9,
  20: 3.0,
  21: 3.1,
  22: 3.2,
  23: 3.3,
  24: 3.4,
  25: 3.5,
  26: 3.6,
  27: 3.7,
  28: 3.8,
  29: 3.9,
  30: 4.0}
UNIQUE_ID = {
    1: [
        0,
        8,
        0,
        0,
        0,
        100,
        PLocalizer.Hat,
        PLocalizer.ClothingStrings.get(0),
        None],
    2: [
        0,
        2,
        0,
        0,
        0,
        300,
        PLocalizer.Hat,
        PLocalizer.ClothingStrings.get(1),
        None],
    3: [
        0,
        6,
        0,
        0,
        0,
        150,
        PLocalizer.Hat,
        PLocalizer.ClothingStrings.get(2),
        None],
    4: [
        0,
        7,
        0,
        0,
        0,
        100,
        PLocalizer.Hat,
        PLocalizer.ClothingStrings.get(3),
        None],
    5: [
        0,
        9,
        0,
        0,
        0,
        500,
        PLocalizer.Hat,
        PLocalizer.ClothingStrings.get(37),
        None],
    6: [
        0,
        6,
        2,
        0,
        0,
        0,
        PLocalizer.Hat,
        PLocalizer.ClothingStrings.get(4),
        PiratesGlobals.FREEHATWEEK],
    7: [
        0,
        1,
        0,
        0,
        0,
        1000,
        PLocalizer.Hat,
        PLocalizer.ClothingStrings.get(38),
        None],
    8: [
        0,
        5,
        0,
        0,
        0,
        1500,
        PLocalizer.Hat,
        PLocalizer.ClothingStrings.get(39),
        None],
    9: [
        0,
        6,
        1,
        0,
        0,
        500,
        PLocalizer.Hat,
        PLocalizer.ClothingStrings.get(2),
        None],
    10: [
        0,
        7,
        1,
        0,
        0,
        400,
        PLocalizer.Hat,
        PLocalizer.ClothingStrings.get(3),
        None],
    11: [
        0,
        6,
        5,
        0,
        0,
        500,
        PLocalizer.Hat,
        PLocalizer.ClothingStrings.get(57),
        None],
    12: [
        0,
        9,
        6,
        0,
        0,
        1000,
        PLocalizer.Hat,
        PLocalizer.ClothingStrings.get(58),
        None],
    13: [
        0,
        9,
        5,
        0,
        0,
        1500,
        PLocalizer.Hat,
        PLocalizer.ClothingStrings.get(59),
        None],
    14: [
        0,
        6,
        6,
        0,
        0,
        0,
        PLocalizer.Hat,
        PLocalizer.ClothingStrings.get(93),
        PiratesGlobals.FREEITEMTHANKSGIVING],
    10000: [
        1,
        1,
        0,
        0,
        0,
        200,
        PLocalizer.Shirt,
        PLocalizer.ClothingStrings.get(5),
        None],
    10001: [
        1,
        1,
        1,
        0,
        0,
        250,
        PLocalizer.Shirt,
        PLocalizer.ClothingStrings.get(6),
        None],
    10002: [
        1,
        1,
        2,
        0,
        0,
        200,
        PLocalizer.Shirt,
        PLocalizer.ClothingStrings.get(5),
        None],
    10003: [
        1,
        1,
        3,
        0,
        0,
        250,
        PLocalizer.Shirt,
        PLocalizer.ClothingStrings.get(5),
        None],
    10004: [
        1,
        1,
        4,
        0,
        0,
        300,
        PLocalizer.Shirt,
        PLocalizer.ClothingStrings.get(7),
        None],
    10005: [
        1,
        2,
        0,
        0,
        0,
        400,
        PLocalizer.Shirt,
        PLocalizer.ClothingStrings.get(6),
        None],
    10006: [
        1,
        2,
        1,
        0,
        0,
        300,
        PLocalizer.Shirt,
        PLocalizer.ClothingStrings.get(8),
        None],
    10007: [
        1,
        2,
        3,
        0,
        0,
        300,
        PLocalizer.Shirt,
        PLocalizer.ClothingStrings.get(8),
        None],
    10008: [
        1,
        3,
        0,
        0,
        0,
        500,
        PLocalizer.Shirt,
        PLocalizer.ClothingStrings.get(9),
        None],
    10009: [
        1,
        3,
        1,
        0,
        0,
        300,
        PLocalizer.Shirt,
        PLocalizer.ClothingStrings.get(10),
        None],
    10010: [
        1,
        3,
        2,
        0,
        0,
        300,
        PLocalizer.Shirt,
        PLocalizer.ClothingStrings.get(11),
        None],
    10011: [
        1,
        4,
        1,
        0,
        0,
        200,
        PLocalizer.Shirt,
        PLocalizer.ClothingStrings.get(10),
        None],
    10012: [
        1,
        6,
        0,
        0,
        0,
        200,
        PLocalizer.Shirt,
        PLocalizer.ClothingStrings.get(12),
        None],
    10013: [
        1,
        6,
        1,
        0,
        0,
        250,
        PLocalizer.Shirt,
        PLocalizer.ClothingStrings.get(12),
        None],
    10014: [
        1,
        6,
        2,
        0,
        0,
        300,
        PLocalizer.Shirt,
        PLocalizer.ClothingStrings.get(12),
        None],
    10015: [
        1,
        6,
        3,
        0,
        0,
        350,
        PLocalizer.Shirt,
        PLocalizer.ClothingStrings.get(13),
        None],
    10016: [
        1,
        7,
        1,
        0,
        0,
        300,
        PLocalizer.Shirt,
        PLocalizer.ClothingStrings.get(12),
        None],
    10017: [
        1,
        7,
        2,
        0,
        0,
        400,
        PLocalizer.Shirt,
        PLocalizer.ClothingStrings.get(14),
        None],
    10018: [
        1,
        8,
        2,
        0,
        0,
        500,
        PLocalizer.Shirt,
        PLocalizer.ClothingStrings.get(15),
        None],
    10019: [
        1,
        4,
        0,
        0,
        0,
        600,
        PLocalizer.Shirt,
        PLocalizer.ClothingStrings.get(9),
        None],
    10020: [
        1,
        5,
        0,
        0,
        0,
        600,
        PLocalizer.Shirt,
        PLocalizer.ClothingStrings.get(40),
        None],
    10021: [
        1,
        7,
        0,
        0,
        0,
        600,
        PLocalizer.Shirt,
        PLocalizer.ClothingStrings.get(13),
        None],
    10022: [
        1,
        8,
        0,
        0,
        0,
        600,
        PLocalizer.Shirt,
        PLocalizer.ClothingStrings.get(41),
        None],
    10023: [
        1,
        10,
        0,
        0,
        0,
        1000,
        PLocalizer.Shirt,
        PLocalizer.ClothingStrings.get(42),
        None],
    10024: [
        1,
        2,
        2,
        0,
        0,
        750,
        PLocalizer.Shirt,
        PLocalizer.ClothingStrings.get(8),
        None],
    10025: [
        1,
        3,
        3,
        0,
        0,
        750,
        PLocalizer.Shirt,
        PLocalizer.ClothingStrings.get(9),
        None],
    10026: [
        1,
        5,
        1,
        0,
        0,
        600,
        PLocalizer.Shirt,
        PLocalizer.ClothingStrings.get(40),
        None],
    10027: [
        1,
        8,
        1,
        0,
        0,
        600,
        PLocalizer.Shirt,
        PLocalizer.ClothingStrings.get(41),
        None],
    10028: [
        1,
        4,
        2,
        0,
        0,
        600,
        PLocalizer.Shirt,
        PLocalizer.ClothingStrings.get(9),
        None],
    10029: [
        1,
        5,
        2,
        0,
        0,
        600,
        PLocalizer.Shirt,
        PLocalizer.ClothingStrings.get(40),
        None],
    10030: [
        1,
        7,
        7,
        0,
        0,
        500,
        PLocalizer.Shirt,
        PLocalizer.ClothingStrings.get(60),
        None],
    10031: [
        1,
        6,
        8,
        0,
        0,
        1000,
        PLocalizer.Shirt,
        PLocalizer.ClothingStrings.get(61),
        None],
    10032: [
        1,
        2,
        12,
        0,
        0,
        1500,
        PLocalizer.Shirt,
        PLocalizer.ClothingStrings.get(62),
        None],
    20001: [
        2,
        1,
        0,
        0,
        0,
        200,
        PLocalizer.Vest,
        PLocalizer.ClothingStrings.get(16),
        None],
    20002: [
        2,
        1,
        1,
        0,
        0,
        200,
        PLocalizer.Vest,
        PLocalizer.ClothingStrings.get(16),
        None],
    20003: [
        2,
        1,
        2,
        0,
        0,
        250,
        PLocalizer.Vest,
        PLocalizer.ClothingStrings.get(16),
        None],
    20004: [
        2,
        1,
        4,
        0,
        0,
        300,
        PLocalizer.Vest,
        PLocalizer.ClothingStrings.get(16),
        None],
    20005: [
        2,
        2,
        0,
        0,
        0,
        300,
        PLocalizer.Vest,
        PLocalizer.ClothingStrings.get(17),
        None],
    20006: [
        2,
        2,
        2,
        0,
        0,
        300,
        PLocalizer.Vest,
        PLocalizer.ClothingStrings.get(17),
        None],
    20007: [
        2,
        2,
        4,
        0,
        0,
        400,
        PLocalizer.Vest,
        PLocalizer.ClothingStrings.get(17),
        None],
    20008: [
        2,
        1,
        3,
        0,
        0,
        500,
        PLocalizer.Vest,
        PLocalizer.ClothingStrings.get(43),
        None],
    20009: [
        2,
        2,
        1,
        0,
        0,
        500,
        PLocalizer.Vest,
        PLocalizer.ClothingStrings.get(44),
        None],
    20010: [
        2,
        2,
        3,
        0,
        0,
        750,
        PLocalizer.Vest,
        PLocalizer.ClothingStrings.get(45),
        None],
    20011: [
        2,
        3,
        0,
        0,
        0,
        1000,
        PLocalizer.Vest,
        PLocalizer.ClothingStrings.get(46),
        None],
    20012: [
        2,
        3,
        3,
        0,
        0,
        900,
        PLocalizer.Vest,
        PLocalizer.ClothingStrings.get(47),
        None],
    20013: [
        2,
        3,
        1,
        0,
        0,
        900,
        PLocalizer.Vest,
        PLocalizer.ClothingStrings.get(47),
        None],
    20014: [
        2,
        3,
        2,
        0,
        0,
        900,
        PLocalizer.Vest,
        PLocalizer.ClothingStrings.get(47),
        None],
    20015: [
        2,
        3,
        5,
        0,
        0,
        1000,
        PLocalizer.Vest,
        PLocalizer.ClothingStrings.get(63),
        None],
    20016: [
        2,
        2,
        5,
        0,
        0,
        1500,
        PLocalizer.Vest,
        PLocalizer.ClothingStrings.get(64),
        None],
    30001: [
        3,
        1,
        0,
        0,
        0,
        500,
        PLocalizer.Coat,
        PLocalizer.ClothingStrings.get(18),
        None],
    30002: [
        3,
        2,
        0,
        0,
        0,
        300,
        PLocalizer.Coat,
        PLocalizer.ClothingStrings.get(19),
        None],
    30003: [
        3,
        1,
        1,
        0,
        0,
        1500,
        PLocalizer.Coat,
        PLocalizer.ClothingStrings.get(48),
        None],
    30004: [
        3,
        1,
        2,
        0,
        0,
        1500,
        PLocalizer.Coat,
        PLocalizer.ClothingStrings.get(48),
        None],
    30005: [
        3,
        1,
        3,
        0,
        0,
        1500,
        PLocalizer.Coat,
        PLocalizer.ClothingStrings.get(48),
        None],
    30006: [
        3,
        1,
        4,
        0,
        0,
        1500,
        PLocalizer.Coat,
        PLocalizer.ClothingStrings.get(48),
        None],
    30007: [
        3,
        1,
        5,
        0,
        0,
        2000,
        PLocalizer.Coat,
        PLocalizer.ClothingStrings.get(48),
        None],
    30008: [
        3,
        1,
        6,
        0,
        0,
        2500,
        PLocalizer.Coat,
        PLocalizer.ClothingStrings.get(48),
        None],
    30009: [
        3,
        1,
        7,
        0,
        0,
        3000,
        PLocalizer.Coat,
        PLocalizer.ClothingStrings.get(48),
        None],
    30010: [
        3,
        1,
        8,
        0,
        0,
        1500,
        PLocalizer.Coat,
        PLocalizer.ClothingStrings.get(48),
        None],
    30011: [
        3,
        1,
        9,
        0,
        0,
        1500,
        PLocalizer.Coat,
        PLocalizer.ClothingStrings.get(48),
        None],
    30012: [
        3,
        2,
        1,
        0,
        0,
        1200,
        PLocalizer.Coat,
        PLocalizer.ClothingStrings.get(49),
        None],
    30013: [
        3,
        2,
        2,
        0,
        0,
        600,
        PLocalizer.Coat,
        PLocalizer.ClothingStrings.get(49),
        None],
    30014: [
        3,
        2,
        3,
        0,
        0,
        1200,
        PLocalizer.Coat,
        PLocalizer.ClothingStrings.get(49),
        None],
    30015: [
        3,
        2,
        4,
        0,
        0,
        1200,
        PLocalizer.Coat,
        PLocalizer.ClothingStrings.get(49),
        None],
    30016: [
        3,
        2,
        5,
        0,
        0,
        1200,
        PLocalizer.Coat,
        PLocalizer.ClothingStrings.get(49),
        None],
    30017: [
        3,
        2,
        6,
        0,
        0,
        1200,
        PLocalizer.Coat,
        PLocalizer.ClothingStrings.get(49),
        None],
    30018: [
        3,
        2,
        7,
        0,
        0,
        1200,
        PLocalizer.Coat,
        PLocalizer.ClothingStrings.get(49),
        None],
    30019: [
        3,
        1,
        14,
        0,
        0,
        1500,
        PLocalizer.Coat,
        PLocalizer.ClothingStrings.get(65),
        None],
    40000: [
        4,
        0,
        0,
        0,
        0,
        200,
        PLocalizer.Pants,
        PLocalizer.ClothingStrings.get(20),
        None],
    40001: [
        4,
        0,
        1,
        0,
        0,
        200,
        PLocalizer.Pants,
        PLocalizer.ClothingStrings.get(20),
        None],
    40002: [
        4,
        0,
        2,
        0,
        0,
        250,
        PLocalizer.Pants,
        PLocalizer.ClothingStrings.get(20),
        None],
    40003: [
        4,
        0,
        3,
        0,
        0,
        250,
        PLocalizer.Pants,
        PLocalizer.ClothingStrings.get(20),
        None],
    40004: [
        4,
        1,
        0,
        0,
        0,
        200,
        PLocalizer.Pants,
        PLocalizer.ClothingStrings.get(20),
        None],
    40005: [
        4,
        1,
        1,
        0,
        0,
        300,
        PLocalizer.Pants,
        PLocalizer.ClothingStrings.get(21),
        None],
    40006: [
        4,
        1,
        2,
        0,
        0,
        400,
        PLocalizer.Pants,
        PLocalizer.ClothingStrings.get(21),
        None],
    40007: [
        4,
        1,
        3,
        0,
        0,
        200,
        PLocalizer.Pants,
        PLocalizer.ClothingStrings.get(20),
        None],
    40008: [
        4,
        1,
        4,
        0,
        0,
        300,
        PLocalizer.Pants,
        PLocalizer.ClothingStrings.get(20),
        None],
    40009: [
        4,
        1,
        5,
        0,
        0,
        300,
        PLocalizer.Pants,
        PLocalizer.ClothingStrings.get(20),
        None],
    40010: [
        4,
        1,
        6,
        0,
        0,
        300,
        PLocalizer.Pants,
        PLocalizer.ClothingStrings.get(20),
        None],
    40011: [
        4,
        1,
        7,
        0,
        0,
        300,
        PLocalizer.Pants,
        PLocalizer.ClothingStrings.get(20),
        None],
    40012: [
        4,
        1,
        8,
        0,
        0,
        300,
        PLocalizer.Pants,
        PLocalizer.ClothingStrings.get(20),
        None],
    40013: [
        4,
        1,
        9,
        0,
        0,
        350,
        PLocalizer.Pants,
        PLocalizer.ClothingStrings.get(21),
        None],
    40014: [
        4,
        1,
        10,
        0,
        0,
        300,
        PLocalizer.Pants,
        PLocalizer.ClothingStrings.get(20),
        None],
    40015: [
        4,
        0,
        4,
        0,
        0,
        750,
        PLocalizer.Pants,
        PLocalizer.ClothingStrings.get(50),
        None],
    40016: [
        4,
        0,
        5,
        0,
        0,
        750,
        PLocalizer.Pants,
        PLocalizer.ClothingStrings.get(51),
        None],
    40017: [
        4,
        1,
        12,
        0,
        0,
        750,
        PLocalizer.Pants,
        PLocalizer.ClothingStrings.get(51),
        None],
    40018: [
        4,
        1,
        13,
        0,
        0,
        750,
        PLocalizer.Pants,
        PLocalizer.ClothingStrings.get(51),
        None],
    40019: [
        4,
        1,
        14,
        0,
        0,
        500,
        PLocalizer.Pants,
        PLocalizer.ClothingStrings.get(66),
        None],
    40020: [
        4,
        1,
        15,
        0,
        0,
        1000,
        PLocalizer.Pants,
        PLocalizer.ClothingStrings.get(67),
        None],
    40021: [
        4,
        0,
        12,
        0,
        0,
        1500,
        PLocalizer.Pants,
        PLocalizer.ClothingStrings.get(68),
        None],
    50001: [
        5,
        1,
        0,
        0,
        0,
        150,
        PLocalizer.Belt,
        PLocalizer.ClothingStrings.get(22),
        None],
    50002: [
        5,
        2,
        0,
        0,
        0,
        300,
        PLocalizer.Belt,
        PLocalizer.ClothingStrings.get(22),
        None],
    50003: [
        5,
        3,
        0,
        0,
        0,
        350,
        PLocalizer.Belt,
        PLocalizer.ClothingStrings.get(23),
        None],
    50004: [
        5,
        4,
        0,
        0,
        0,
        300,
        PLocalizer.Belt,
        PLocalizer.ClothingStrings.get(23),
        None],
    50005: [
        5,
        5,
        0,
        0,
        0,
        250,
        PLocalizer.Belt,
        PLocalizer.ClothingStrings.get(22),
        None],
    50006: [
        5,
        17,
        0,
        0,
        0,
        500,
        PLocalizer.Belt,
        PLocalizer.ClothingStrings.get(69),
        None],
    50007: [
        5,
        19,
        0,
        0,
        0,
        1000,
        PLocalizer.Belt,
        PLocalizer.ClothingStrings.get(70),
        None],
    50008: [
        5,
        18,
        0,
        0,
        0,
        1500,
        PLocalizer.Belt,
        PLocalizer.ClothingStrings.get(71),
        None],
    70001: [
        7,
        1,
        0,
        0,
        0,
        200,
        PLocalizer.Shoes,
        PLocalizer.ClothingStrings.get(24),
        None],
    70002: [
        7,
        1,
        1,
        0,
        0,
        200,
        PLocalizer.Shoes,
        PLocalizer.ClothingStrings.get(24),
        None],
    70003: [
        7,
        1,
        2,
        0,
        0,
        200,
        PLocalizer.Shoes,
        PLocalizer.ClothingStrings.get(24),
        None],
    70004: [
        7,
        1,
        3,
        0,
        0,
        200,
        PLocalizer.Shoes,
        PLocalizer.ClothingStrings.get(24),
        None],
    70005: [
        7,
        2,
        0,
        0,
        0,
        500,
        PLocalizer.Shoes,
        PLocalizer.ClothingStrings.get(24),
        None],
    70006: [
        7,
        2,
        1,
        0,
        0,
        200,
        PLocalizer.Shoes,
        PLocalizer.ClothingStrings.get(24),
        None],
    70007: [
        7,
        2,
        2,
        0,
        0,
        200,
        PLocalizer.Shoes,
        PLocalizer.ClothingStrings.get(24),
        None],
    70008: [
        7,
        2,
        3,
        0,
        0,
        200,
        PLocalizer.Shoes,
        PLocalizer.ClothingStrings.get(24),
        None],
    70009: [
        7,
        2,
        7,
        0,
        0,
        500,
        PLocalizer.Shoes,
        PLocalizer.ClothingStrings.get(72),
        None],
    70010: [
        7,
        1,
        9,
        0,
        0,
        1000,
        PLocalizer.Shoes,
        PLocalizer.ClothingStrings.get(73),
        None],
    70011: [
        7,
        1,
        8,
        0,
        0,
        1500,
        PLocalizer.Shoes,
        PLocalizer.ClothingStrings.get(74),
        None],
    80001: [
        0,
        1,
        0,
        0,
        0,
        300,
        PLocalizer.Hat,
        PLocalizer.ClothingStrings.get(25),
        None],
    80002: [
        0,
        3,
        0,
        0,
        0,
        200,
        PLocalizer.Hat,
        PLocalizer.ClothingStrings.get(25),
        None],
    80003: [
        0,
        5,
        0,
        0,
        0,
        150,
        PLocalizer.Hat,
        PLocalizer.ClothingStrings.get(2),
        None],
    80004: [
        0,
        6,
        0,
        0,
        0,
        100,
        PLocalizer.Hat,
        PLocalizer.ClothingStrings.get(3),
        None],
    80005: [
        0,
        5,
        2,
        0,
        0,
        0,
        PLocalizer.Hat,
        PLocalizer.ClothingStrings.get(4),
        PiratesGlobals.FREEHATWEEK],
    80006: [
        0,
        5,
        1,
        0,
        0,
        500,
        PLocalizer.Hat,
        PLocalizer.ClothingStrings.get(2),
        None],
    80007: [
        0,
        6,
        1,
        0,
        0,
        400,
        PLocalizer.Hat,
        PLocalizer.ClothingStrings.get(3),
        None],
    80008: [
        0,
        5,
        5,
        0,
        0,
        500,
        PLocalizer.Hat,
        PLocalizer.ClothingStrings.get(75),
        None],
    80009: [
        0,
        1,
        6,
        0,
        0,
        1000,
        PLocalizer.Hat,
        PLocalizer.ClothingStrings.get(76),
        None],
    80010: [
        0,
        1,
        5,
        0,
        0,
        1500,
        PLocalizer.Hat,
        PLocalizer.ClothingStrings.get(77),
        None],
    80011: [
        0,
        5,
        6,
        0,
        0,
        0,
        PLocalizer.Hat,
        PLocalizer.ClothingStrings.get(93),
        PiratesGlobals.FREEITEMTHANKSGIVING],
    90001: [
        1,
        0,
        1,
        0,
        0,
        300,
        PLocalizer.Shirt,
        PLocalizer.ClothingStrings.get(10),
        None],
    90002: [
        1,
        0,
        2,
        0,
        0,
        300,
        PLocalizer.Shirt,
        PLocalizer.ClothingStrings.get(10),
        None],
    90003: [
        1,
        0,
        3,
        0,
        0,
        300,
        PLocalizer.Shirt,
        PLocalizer.ClothingStrings.get(10),
        None],
    90004: [
        1,
        1,
        0,
        0,
        0,
        400,
        PLocalizer.Shirt,
        PLocalizer.ClothingStrings.get(26),
        None],
    90005: [
        1,
        1,
        1,
        0,
        0,
        200,
        PLocalizer.Shirt,
        PLocalizer.ClothingStrings.get(26),
        None],
    90006: [
        1,
        1,
        2,
        0,
        0,
        350,
        PLocalizer.Shirt,
        PLocalizer.ClothingStrings.get(26),
        None],
    90007: [
        1,
        1,
        3,
        0,
        0,
        350,
        PLocalizer.Shirt,
        PLocalizer.ClothingStrings.get(26),
        None],
    90008: [
        1,
        2,
        0,
        0,
        0,
        350,
        PLocalizer.Shirt,
        PLocalizer.ClothingStrings.get(10),
        None],
    90009: [
        1,
        2,
        1,
        0,
        0,
        400,
        PLocalizer.Shirt,
        PLocalizer.ClothingStrings.get(9),
        None],
    90010: [
        1,
        2,
        2,
        0,
        0,
        400,
        PLocalizer.Shirt,
        PLocalizer.ClothingStrings.get(9),
        None],
    90011: [
        1,
        2,
        3,
        0,
        0,
        400,
        PLocalizer.Shirt,
        PLocalizer.ClothingStrings.get(9),
        None],
    90012: [
        1,
        3,
        1,
        0,
        0,
        500,
        PLocalizer.Shirt,
        PLocalizer.ClothingStrings.get(27),
        None],
    90013: [
        1,
        3,
        2,
        0,
        0,
        400,
        PLocalizer.Shirt,
        PLocalizer.ClothingStrings.get(27),
        None],
    90014: [
        1,
        3,
        3,
        0,
        0,
        400,
        PLocalizer.Shirt,
        PLocalizer.ClothingStrings.get(27),
        None],
    90015: [
        1,
        4,
        0,
        0,
        0,
        450,
        PLocalizer.Shirt,
        PLocalizer.ClothingStrings.get(27),
        None],
    90016: [
        1,
        4,
        1,
        0,
        0,
        450,
        PLocalizer.Shirt,
        PLocalizer.ClothingStrings.get(27),
        None],
    90017: [
        1,
        4,
        2,
        0,
        0,
        500,
        PLocalizer.Shirt,
        PLocalizer.ClothingStrings.get(27),
        None],
    90018: [
        1,
        4,
        3,
        0,
        0,
        400,
        PLocalizer.Shirt,
        PLocalizer.ClothingStrings.get(27),
        None],
    90019: [
        1,
        5,
        0,
        0,
        0,
        750,
        PLocalizer.Shirt,
        PLocalizer.ClothingStrings.get(13),
        None],
    90020: [
        1,
        0,
        4,
        0,
        0,
        500,
        PLocalizer.Shirt,
        PLocalizer.ClothingStrings.get(9),
        None],
    90021: [
        1,
        0,
        5,
        0,
        0,
        500,
        PLocalizer.Shirt,
        PLocalizer.ClothingStrings.get(9),
        None],
    90022: [
        1,
        3,
        0,
        0,
        0,
        1000,
        PLocalizer.Shirt,
        PLocalizer.ClothingStrings.get(52),
        None],
    90023: [
        1,
        4,
        4,
        0,
        0,
        750,
        PLocalizer.Shirt,
        PLocalizer.ClothingStrings.get(13),
        None],
    90024: [
        1,
        4,
        5,
        0,
        0,
        750,
        PLocalizer.Shirt,
        PLocalizer.ClothingStrings.get(13),
        None],
    90025: [
        1,
        4,
        6,
        0,
        0,
        750,
        PLocalizer.Shirt,
        PLocalizer.ClothingStrings.get(13),
        None],
    90026: [
        1,
        5,
        1,
        0,
        0,
        750,
        PLocalizer.Shirt,
        PLocalizer.ClothingStrings.get(13),
        None],
    90027: [
        1,
        5,
        2,
        0,
        0,
        750,
        PLocalizer.Shirt,
        PLocalizer.ClothingStrings.get(13),
        None],
    90028: [
        1,
        5,
        3,
        0,
        0,
        750,
        PLocalizer.Shirt,
        PLocalizer.ClothingStrings.get(13),
        None],
    90029: [
        1,
        5,
        4,
        0,
        0,
        750,
        PLocalizer.Shirt,
        PLocalizer.ClothingStrings.get(13),
        None],
    90030: [
        1,
        5,
        5,
        0,
        0,
        750,
        PLocalizer.Shirt,
        PLocalizer.ClothingStrings.get(13),
        None],
    90031: [
        1,
        5,
        6,
        0,
        0,
        750,
        PLocalizer.Shirt,
        PLocalizer.ClothingStrings.get(13),
        None],
    90032: [
        1,
        0,
        0,
        0,
        0,
        300,
        PLocalizer.Shirt,
        PLocalizer.ClothingStrings.get(10),
        None],
    90033: [
        1,
        3,
        7,
        0,
        0,
        500,
        PLocalizer.Shirt,
        PLocalizer.ClothingStrings.get(78),
        None],
    90034: [
        1,
        3,
        8,
        0,
        0,
        1000,
        PLocalizer.Shirt,
        PLocalizer.ClothingStrings.get(79),
        None],
    90035: [
        1,
        3,
        9,
        0,
        0,
        1500,
        PLocalizer.Shirt,
        PLocalizer.ClothingStrings.get(80),
        None],
    100001: [
        2,
        1,
        0,
        0,
        0,
        200,
        PLocalizer.Vest,
        PLocalizer.ClothingStrings.get(16),
        None],
    100002: [
        2,
        1,
        1,
        0,
        0,
        200,
        PLocalizer.Vest,
        PLocalizer.ClothingStrings.get(16),
        None],
    100003: [
        2,
        1,
        2,
        0,
        0,
        200,
        PLocalizer.Vest,
        PLocalizer.ClothingStrings.get(16),
        None],
    100004: [
        2,
        1,
        3,
        0,
        0,
        200,
        PLocalizer.Vest,
        PLocalizer.ClothingStrings.get(16),
        None],
    100005: [
        2,
        2,
        0,
        0,
        0,
        250,
        PLocalizer.Vest,
        PLocalizer.ClothingStrings.get(28),
        None],
    100006: [
        2,
        2,
        1,
        0,
        0,
        250,
        PLocalizer.Vest,
        PLocalizer.ClothingStrings.get(28),
        None],
    100007: [
        2,
        2,
        2,
        0,
        0,
        250,
        PLocalizer.Vest,
        PLocalizer.ClothingStrings.get(28),
        None],
    100008: [
        2,
        2,
        3,
        0,
        0,
        300,
        PLocalizer.Vest,
        PLocalizer.ClothingStrings.get(28),
        None],
    100009: [
        2,
        3,
        0,
        0,
        0,
        400,
        PLocalizer.Vest,
        PLocalizer.ClothingStrings.get(29),
        None],
    100010: [
        2,
        3,
        1,
        0,
        0,
        400,
        PLocalizer.Vest,
        PLocalizer.ClothingStrings.get(29),
        None],
    100011: [
        2,
        3,
        2,
        0,
        0,
        400,
        PLocalizer.Vest,
        PLocalizer.ClothingStrings.get(29),
        None],
    100012: [
        2,
        4,
        0,
        0,
        0,
        500,
        PLocalizer.Vest,
        PLocalizer.ClothingStrings.get(29),
        None],
    100013: [
        2,
        4,
        1,
        0,
        0,
        400,
        PLocalizer.Vest,
        PLocalizer.ClothingStrings.get(29),
        None],
    100014: [
        2,
        4,
        2,
        0,
        0,
        400,
        PLocalizer.Vest,
        PLocalizer.ClothingStrings.get(29),
        None],
    100015: [
        2,
        1,
        4,
        0,
        0,
        750,
        PLocalizer.Vest,
        PLocalizer.ClothingStrings.get(53),
        None],
    100016: [
        2,
        1,
        5,
        0,
        0,
        750,
        PLocalizer.Vest,
        PLocalizer.ClothingStrings.get(53),
        None],
    100017: [
        2,
        1,
        6,
        0,
        0,
        750,
        PLocalizer.Vest,
        PLocalizer.ClothingStrings.get(53),
        None],
    100018: [
        2,
        1,
        7,
        0,
        0,
        1000,
        PLocalizer.Vest,
        PLocalizer.ClothingStrings.get(53),
        None],
    100019: [
        2,
        1,
        8,
        0,
        0,
        750,
        PLocalizer.Vest,
        PLocalizer.ClothingStrings.get(53),
        None],
    100020: [
        2,
        1,
        9,
        0,
        0,
        750,
        PLocalizer.Vest,
        PLocalizer.ClothingStrings.get(53),
        None],
    100021: [
        2,
        2,
        4,
        0,
        0,
        1000,
        PLocalizer.Vest,
        PLocalizer.ClothingStrings.get(54),
        None],
    100022: [
        2,
        2,
        5,
        0,
        0,
        1000,
        PLocalizer.Vest,
        PLocalizer.ClothingStrings.get(54),
        None],
    100023: [
        2,
        2,
        6,
        0,
        0,
        1000,
        PLocalizer.Vest,
        PLocalizer.ClothingStrings.get(54),
        None],
    100024: [
        2,
        2,
        7,
        0,
        0,
        1000,
        PLocalizer.Vest,
        PLocalizer.ClothingStrings.get(54),
        None],
    100025: [
        2,
        2,
        8,
        0,
        0,
        1000,
        PLocalizer.Vest,
        PLocalizer.ClothingStrings.get(54),
        None],
    100026: [
        2,
        2,
        9,
        0,
        0,
        1000,
        PLocalizer.Vest,
        PLocalizer.ClothingStrings.get(54),
        None],
    100027: [
        2,
        3,
        4,
        0,
        0,
        750,
        PLocalizer.Vest,
        PLocalizer.ClothingStrings.get(55),
        None],
    100028: [
        2,
        3,
        5,
        0,
        0,
        750,
        PLocalizer.Vest,
        PLocalizer.ClothingStrings.get(55),
        None],
    100029: [
        2,
        3,
        6,
        0,
        0,
        750,
        PLocalizer.Vest,
        PLocalizer.ClothingStrings.get(55),
        None],
    100030: [
        2,
        2,
        10,
        0,
        0,
        1000,
        PLocalizer.Vest,
        PLocalizer.ClothingStrings.get(81),
        None],
    100031: [
        2,
        1,
        10,
        0,
        0,
        1500,
        PLocalizer.Vest,
        PLocalizer.ClothingStrings.get(82),
        None],
    110001: [
        3,
        1,
        0,
        0,
        0,
        400,
        PLocalizer.Coat,
        PLocalizer.ClothingStrings.get(30),
        None],
    110002: [
        3,
        1,
        1,
        0,
        0,
        400,
        PLocalizer.Coat,
        PLocalizer.ClothingStrings.get(30),
        None],
    110003: [
        3,
        2,
        0,
        0,
        0,
        400,
        PLocalizer.Coat,
        PLocalizer.ClothingStrings.get(30),
        None],
    110004: [
        3,
        2,
        1,
        0,
        0,
        400,
        PLocalizer.Coat,
        PLocalizer.ClothingStrings.get(30),
        None],
    110005: [
        3,
        2,
        2,
        0,
        0,
        400,
        PLocalizer.Coat,
        PLocalizer.ClothingStrings.get(30),
        None],
    110006: [
        3,
        1,
        2,
        0,
        0,
        1500,
        PLocalizer.Coat,
        PLocalizer.ClothingStrings.get(48),
        None],
    110007: [
        3,
        1,
        3,
        0,
        0,
        1500,
        PLocalizer.Coat,
        PLocalizer.ClothingStrings.get(48),
        None],
    110008: [
        3,
        1,
        4,
        0,
        0,
        2000,
        PLocalizer.Coat,
        PLocalizer.ClothingStrings.get(48),
        None],
    110009: [
        3,
        2,
        3,
        0,
        0,
        750,
        PLocalizer.Coat,
        PLocalizer.ClothingStrings.get(48),
        None],
    110010: [
        3,
        2,
        4,
        0,
        0,
        1500,
        PLocalizer.Coat,
        PLocalizer.ClothingStrings.get(48),
        None],
    110011: [
        3,
        1,
        9,
        0,
        0,
        1500,
        PLocalizer.Coat,
        PLocalizer.ClothingStrings.get(83),
        None],
    130000: [
        4,
        0,
        0,
        0,
        0,
        200,
        PLocalizer.Pants,
        PLocalizer.ClothingStrings.get(20),
        None],
    130001: [
        4,
        0,
        1,
        0,
        0,
        200,
        PLocalizer.Pants,
        PLocalizer.ClothingStrings.get(20),
        None],
    130002: [
        4,
        0,
        2,
        0,
        0,
        200,
        PLocalizer.Pants,
        PLocalizer.ClothingStrings.get(20),
        None],
    130003: [
        4,
        0,
        3,
        0,
        0,
        200,
        PLocalizer.Pants,
        PLocalizer.ClothingStrings.get(20),
        None],
    130004: [
        4,
        0,
        4,
        0,
        0,
        200,
        PLocalizer.Pants,
        PLocalizer.ClothingStrings.get(20),
        None],
    130005: [
        4,
        0,
        5,
        0,
        0,
        300,
        PLocalizer.Pants,
        PLocalizer.ClothingStrings.get(21),
        None],
    130006: [
        4,
        1,
        0,
        0,
        0,
        300,
        PLocalizer.Pants,
        PLocalizer.ClothingStrings.get(31),
        None],
    130007: [
        4,
        1,
        1,
        0,
        0,
        300,
        PLocalizer.Pants,
        PLocalizer.ClothingStrings.get(31),
        None],
    130008: [
        4,
        1,
        2,
        0,
        0,
        300,
        PLocalizer.Pants,
        PLocalizer.ClothingStrings.get(31),
        None],
    130009: [
        4,
        1,
        3,
        0,
        0,
        300,
        PLocalizer.Pants,
        PLocalizer.ClothingStrings.get(31),
        None],
    130010: [
        4,
        1,
        4,
        0,
        0,
        300,
        PLocalizer.Pants,
        PLocalizer.ClothingStrings.get(31),
        None],
    130011: [
        4,
        2,
        0,
        0,
        0,
        400,
        PLocalizer.Pants,
        PLocalizer.ClothingStrings.get(32),
        None],
    130012: [
        4,
        2,
        1,
        0,
        0,
        400,
        PLocalizer.Pants,
        PLocalizer.ClothingStrings.get(32),
        None],
    130013: [
        4,
        2,
        2,
        0,
        0,
        400,
        PLocalizer.Pants,
        PLocalizer.ClothingStrings.get(32),
        None],
    130014: [
        4,
        2,
        3,
        0,
        0,
        400,
        PLocalizer.Pants,
        PLocalizer.ClothingStrings.get(32),
        None],
    130015: [
        4,
        2,
        4,
        0,
        0,
        400,
        PLocalizer.Pants,
        PLocalizer.ClothingStrings.get(32),
        None],
    130016: [
        4,
        2,
        5,
        0,
        0,
        400,
        PLocalizer.Pants,
        PLocalizer.ClothingStrings.get(32),
        None],
    130017: [
        4,
        2,
        6,
        0,
        0,
        400,
        PLocalizer.Pants,
        PLocalizer.ClothingStrings.get(32),
        None],
    130018: [
        4,
        0,
        6,
        0,
        0,
        750,
        PLocalizer.Pants,
        PLocalizer.ClothingStrings.get(51),
        None],
    130019: [
        4,
        0,
        7,
        0,
        0,
        750,
        PLocalizer.Pants,
        PLocalizer.ClothingStrings.get(51),
        None],
    130020: [
        4,
        0,
        8,
        0,
        0,
        750,
        PLocalizer.Pants,
        PLocalizer.ClothingStrings.get(51),
        None],
    130021: [
        4,
        0,
        9,
        0,
        0,
        750,
        PLocalizer.Pants,
        PLocalizer.ClothingStrings.get(51),
        None],
    130022: [
        4,
        0,
        10,
        0,
        0,
        750,
        PLocalizer.Pants,
        PLocalizer.ClothingStrings.get(51),
        None],
    130023: [
        4,
        0,
        11,
        0,
        0,
        750,
        PLocalizer.Pants,
        PLocalizer.ClothingStrings.get(51),
        None],
    130024: [
        4,
        0,
        12,
        0,
        0,
        750,
        PLocalizer.Pants,
        PLocalizer.ClothingStrings.get(51),
        None],
    130025: [
        4,
        0,
        13,
        0,
        0,
        500,
        PLocalizer.Pants,
        PLocalizer.ClothingStrings.get(84),
        None],
    130026: [
        4,
        0,
        15,
        0,
        0,
        1000,
        PLocalizer.Pants,
        PLocalizer.ClothingStrings.get(85),
        None],
    130027: [
        4,
        0,
        14,
        0,
        0,
        1500,
        PLocalizer.Pants,
        PLocalizer.ClothingStrings.get(86),
        None],
    140001: [
        5,
        1,
        0,
        0,
        0,
        200,
        PLocalizer.Belt,
        PLocalizer.ClothingStrings.get(22),
        None],
    140002: [
        5,
        2,
        0,
        0,
        0,
        250,
        PLocalizer.Belt,
        PLocalizer.ClothingStrings.get(33),
        None],
    140003: [
        5,
        3,
        0,
        0,
        0,
        200,
        PLocalizer.Belt,
        PLocalizer.ClothingStrings.get(22),
        None],
    140004: [
        5,
        4,
        0,
        0,
        0,
        200,
        PLocalizer.Belt,
        PLocalizer.ClothingStrings.get(22),
        None],
    140005: [
        5,
        5,
        0,
        0,
        0,
        350,
        PLocalizer.Belt,
        PLocalizer.ClothingStrings.get(23),
        None],
    140006: [
        5,
        6,
        0,
        0,
        0,
        350,
        PLocalizer.Belt,
        PLocalizer.ClothingStrings.get(23),
        None],
    140007: [
        5,
        7,
        0,
        0,
        0,
        350,
        PLocalizer.Belt,
        PLocalizer.ClothingStrings.get(23),
        None],
    140008: [
        5,
        8,
        0,
        0,
        0,
        350,
        PLocalizer.Belt,
        PLocalizer.ClothingStrings.get(23),
        None],
    140009: [
        5,
        9,
        0,
        0,
        0,
        250,
        PLocalizer.Belt,
        PLocalizer.ClothingStrings.get(23),
        None],
    140010: [
        5,
        10,
        0,
        0,
        0,
        300,
        PLocalizer.Belt,
        PLocalizer.ClothingStrings.get(23),
        None],
    140011: [
        5,
        15,
        0,
        0,
        0,
        500,
        PLocalizer.Belt,
        PLocalizer.ClothingStrings.get(87),
        None],
    140012: [
        5,
        17,
        0,
        0,
        0,
        1000,
        PLocalizer.Belt,
        PLocalizer.ClothingStrings.get(88),
        None],
    140013: [
        5,
        16,
        0,
        0,
        0,
        1500,
        PLocalizer.Belt,
        PLocalizer.ClothingStrings.get(89),
        None],
    160001: [
        7,
        1,
        0,
        0,
        0,
        200,
        PLocalizer.Shoes,
        PLocalizer.ClothingStrings.get(24),
        None],
    160002: [
        7,
        1,
        1,
        0,
        0,
        200,
        PLocalizer.Shoes,
        PLocalizer.ClothingStrings.get(24),
        None],
    160003: [
        7,
        1,
        2,
        0,
        0,
        200,
        PLocalizer.Shoes,
        PLocalizer.ClothingStrings.get(24),
        None],
    160004: [
        7,
        1,
        3,
        0,
        0,
        200,
        PLocalizer.Shoes,
        PLocalizer.ClothingStrings.get(24),
        None],
    160005: [
        7,
        2,
        0,
        0,
        0,
        300,
        PLocalizer.Shoes,
        PLocalizer.ClothingStrings.get(34),
        None],
    160006: [
        7,
        2,
        1,
        0,
        0,
        300,
        PLocalizer.Shoes,
        PLocalizer.ClothingStrings.get(34),
        None],
    160007: [
        7,
        2,
        2,
        0,
        0,
        300,
        PLocalizer.Shoes,
        PLocalizer.ClothingStrings.get(34),
        None],
    160008: [
        7,
        2,
        3,
        0,
        0,
        300,
        PLocalizer.Shoes,
        PLocalizer.ClothingStrings.get(34),
        None],
    160009: [
        7,
        3,
        0,
        0,
        0,
        400,
        PLocalizer.Shoes,
        PLocalizer.ClothingStrings.get(35),
        None],
    160010: [
        7,
        3,
        1,
        0,
        0,
        500,
        PLocalizer.Shoes,
        PLocalizer.ClothingStrings.get(35),
        None],
    160011: [
        7,
        3,
        2,
        0,
        0,
        400,
        PLocalizer.Shoes,
        PLocalizer.ClothingStrings.get(35),
        None],
    160012: [
        7,
        3,
        3,
        0,
        0,
        400,
        PLocalizer.Shoes,
        PLocalizer.ClothingStrings.get(35),
        None],
    160013: [
        7,
        3,
        4,
        0,
        0,
        400,
        PLocalizer.Shoes,
        PLocalizer.ClothingStrings.get(35),
        None],
    160014: [
        7,
        4,
        0,
        0,
        0,
        500,
        PLocalizer.Shoes,
        PLocalizer.ClothingStrings.get(36),
        None],
    160015: [
        7,
        4,
        1,
        0,
        0,
        500,
        PLocalizer.Shoes,
        PLocalizer.ClothingStrings.get(36),
        None],
    160016: [
        7,
        4,
        2,
        0,
        0,
        500,
        PLocalizer.Shoes,
        PLocalizer.ClothingStrings.get(36),
        None],
    160017: [
        7,
        4,
        3,
        0,
        0,
        500,
        PLocalizer.Shoes,
        PLocalizer.ClothingStrings.get(36),
        None],
    160018: [
        7,
        3,
        5,
        0,
        0,
        750,
        PLocalizer.Shoes,
        PLocalizer.ClothingStrings.get(56),
        None],
    160019: [
        7,
        3,
        6,
        0,
        0,
        750,
        PLocalizer.Shoes,
        PLocalizer.ClothingStrings.get(56),
        None],
    160020: [
        7,
        3,
        7,
        0,
        0,
        750,
        PLocalizer.Shoes,
        PLocalizer.ClothingStrings.get(56),
        None],
    160021: [
        7,
        3,
        8,
        0,
        0,
        750,
        PLocalizer.Shoes,
        PLocalizer.ClothingStrings.get(56),
        None],
    160022: [
        7,
        1,
        8,
        0,
        0,
        500,
        PLocalizer.Shoes,
        PLocalizer.ClothingStrings.get(90),
        None],
    160023: [
        7,
        4,
        7,
        0,
        0,
        1000,
        PLocalizer.Shoes,
        PLocalizer.ClothingStrings.get(91),
        None],
    160024: [
        7,
        1,
        9,
        0,
        0,
        1500,
        PLocalizer.Shoes,
        PLocalizer.ClothingStrings.get(92),
        None]}

def spitOutEconomy():
    itemsForSale = 0
    repeats = {}
    numRepeats = 0
    for shopId in [PiratesGlobals.PORT_ROYAL_DEFAULTS, PiratesGlobals.PORT_ROYAL_THRIFT, PiratesGlobals.TORTUGA_DEFAULTS, PiratesGlobals.CUBA_DEFAULTS, PiratesGlobals.DEL_FUEGO_DEFAULTS]:
        shop = stores.get(shopId)
        if shop:
            for itemId in list(shop.keys()):
                item = UNIQUE_ID.get(itemId)
                if item:
                    for color in shop.get(itemId):
                        type = item[0]
                        itemCost = item[5] * colorCostScaler.get(color)
                        typeString = item[6]
                        descString = item[7]
                        colorString = PLocalizer.TailorColorStrings.get(color)
                        if colorString:
                            if itemId in repeats:
                                previousColors = repeats.get(itemId)
                                if color in previousColors:
                                    numRepeats += 1
                                    continue
                                else:
                                    repeats[itemId].append(color)
                            else:
                                repeats[itemId] = [
                                    color]
                            if itemId in range(HAT_START_RANGE_MALE, HAT_START_RANGE_FEMALE - 1):
                                gender = 'Male'
                            else:
                                gender = 'Female'
                            print('Clothing Item UID %s\n - Type = %s(%s)\n - Long Desc = %s\n - Color = %s(%s)\n - Cost = %s gold\n - Gender = %s\n' % (itemId, typeString, type, descString, colorString, color, itemCost, gender))

                            itemsForSale += 1

    print('\n%s items for sale.' % itemsForSale)
    print('\n%s repeated items.' % numRepeats)

