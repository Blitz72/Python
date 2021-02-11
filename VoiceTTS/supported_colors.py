# Color values can be found here: https://en.wikipedia.org/wiki/List_of_colors_(compact)

# RGB color values given in tuples are (R, G, B)

supported_colors_list = [
    {
        'name': 'alice blue',
        'google': {
            'is_rgb': True,
            'color_values': (240, 248, 255),
            'tcs_value': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (240, 248, 255),
            'tcs_value': None
        }
    },
#     {
#         'name': 'almond',
#         'google': {
#             'is_rgb': True,
#             'color_values': (239, 222, 205)
#         }
# #         'alexa': {
# #             'is_rgb': True,
# #             'color_values': (0, 0, 0)
# #         }
#     },
    {
        'name': 'antique white',      # Google uses cct for this color
        'google': {
            'is_rgb': False,
            'color_values': 5500,
            'tcs_value': 4380
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (250, 235, 215),
            'tcs_value': None
        }
    },
    {
        'name': 'aqua',
        'google': {
            'is_rgb': True,
            'color_values': (0, 255, 255),
            'tcs_value': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 255, 255),
            'tcs_value': None
        }
    },
    {
        'name': 'aquamarine',
        'google': {
            'is_rgb': True,
            'color_values': (127, 255, 212),
            'tcs_value': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (127, 255, 212),
            'tcs_value': None
        }
    },
    {
        'name': 'azure',
        'google': {
            'is_rgb': True,
            'color_values': (0, 127, 255),
            'tcs_value': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (240, 255, 255),
            'tcs_value': None
        }
    },
    {
        'name': 'beige',              # Google uses cct for this color
        'google': {
            'is_rgb': False,
            'color_values': 5000,
            'tcs_value': 4150
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (245, 245, 220),
            'tcs_value': None
        }
    },
    {
        'name': 'bisque',             # Google uses cct for this color
        # 'google': {
        #     'is_rgb': False,
        #     'color_values': ''
        # },
        'alexa': {
            'is_rgb': True,
            'color_values': (255, 228, 196),
            'tcs_value': None
        }
    },
    {
        'name': 'black',
        'google': {
            'is_rgb': True,
            'color_values': (0, 0, 0),
            'tcs_value': None
        },
#         'alexa': {
#             'is_rgb': True,
#             'color_values': (0, 0, 0)
#         }
    },
    {
        'name': 'blanched almond',    # Google uses cct for this color
#         'google': {
#             'is_rgb': False,
#             'color_values': ''
#         },
        'alexa': {
            'is_rgb': True,
            'color_values': (255, 235, 205),
            'tcs_value': None
        }
    },
    {
        'name': 'blue',
        'google': {
            'is_rgb': True,
            'color_values': (0, 0, 255),
            'tcs_value': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 0, 255),
            'tcs_value': None
        }
    },
    {
        'name': 'blue violet',
        'google': {
            'is_rgb': True,
            'color_values': (138, 43, 226),
            'tcs_value': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (138, 43, 226),
            'tcs_value': None
        }
    },
    {
        'name': 'brown',
        'google': {
            'is_rgb': True,
            'color_values': (150, 75, 0),
            'tcs_value': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (165, 42, 42),
            'tcs_value': None
        }
    },
#     {
#         'name': 'burlywood',         # Google uses cct for this color
#         'google': {
#             'is_rgb': False,
#             'color_values': ''
#         },
#         'alexa': {
#             'is_rgb': False,
#             'color_values': ''
#         }
#     },
    {
        'name': 'candlelight',       # Google uses cct for this color
        'google': {
            'is_rgb': False,
            'color_values': 2000,
            'tcs_value': 2200
        },
        'alexa': {
            'is_rgb': False,
            'color_values': 2200,
            'tcs_value': 3340
        }
    },
    {
        'name': 'cadet blue',
        'google': {
            'is_rgb': True,
            'color_values': (95, 158, 160),
            'tcs_value': None
        },
        'alexa': {                           # Need to tell Alexa to set a Full Color bulb 'to the color cadet blue'
            'is_rgb': True,
            'color_values': (95, 158, 160),
            'tcs_value': None
        }
    },
    {
        'name': 'chartreuse',
        'google': {
            'is_rgb': True,
            'color_values': (223, 255, 0),
            'tcs_value': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (127, 255, 0),
            'tcs_value': None
        }
    },
    {
        'name': 'chocolate',
        'google': {
            'is_rgb': True,
            'color_values': (123, 63, 0),
            'tcs_value': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (210, 105, 30),
            'tcs_value': None
        }
    },
    {
        'name': 'cool',                # Google uses cct for this color
#         'google': {
#             'is_rgb': False,
#             'color_values': ''
#         },
        'alexa': {
            'is_rgb': False,
            'color_values': 7000,
            'tcs_value': 5340
        }
    },
    {
        'name': 'cool white',                # Google uses cct for this color
        'google': {
            'is_rgb': False,
            'color_values': 4000,
            'tcs_value': 3350
        },
        'alexa': {
            'is_rgb': False,
            'color_values': 7000,
            'tcs_value': 5340
        }
    },
    {
        'name': 'coral',
        'google': {
            'is_rgb': True,
            'color_values': (255, 127, 80),
            'tcs_value': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (255, 127, 80),
            'tcs_value': None
        }
    },
    {
        'name': 'cornflower',
        'google': {
            'is_rgb': True,
            'color_values': (100, 149, 237),
            'tcs_value': None
        },
#         'alexa': {
#             'is_rgb': True,
#             'color_values': (0, 0, 0)
#         }
    },
    {
        'name': 'cornflower blue',           # Need to test for Alexa
        'google': {
            'is_rgb': True,
            'color_values': (100, 149, 237),
            'tcs_value': None
        },
#         'alexa': {
#             'is_rgb': True,
#             'color_values': (0, 0, 0)
#         }
    },
    {
        'name': 'cornsilk',
        'google': {
            'is_rgb': False,
            'color_values': 6500,
            'tcs_value': 4850
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (255, 248, 220),
            'tcs_value': None
        }
    },
    {
        'name': 'crimson',
        'google': {
            'is_rgb': True,
            'color_values': (220, 20, 60),
            'tcs_value': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (220, 20, 60),
            'tcs_value': None
        }
    },
    {
        'name': 'cyan',
        'google': {
            'is_rgb': True,
            'color_values': (0, 255, 255),
            'tcs_value': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 255, 255),
            'tcs_value': None
        }
    },
    {
        'name': 'dark blue',
        'google': {
            'is_rgb': True,
            'color_values': (0, 0, 139),
            'tcs_value': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 0, 139),
            'tcs_value': None
        }
    },
    {
        'name': 'dark cyan',
        'google': {
            'is_rgb': True,
            'color_values': (0, 139, 139),
            'tcs_value': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 139, 139),
            'tcs_value': None
        }
    },
    {
        'name': 'dark goldenrod',
        'google': {
            'is_rgb': True,
            'color_values': (184, 134, 11),
            'tcs_value': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (184, 134, 11),
            'tcs_value': None
        }
    },
    {
        'name': 'dark gray',
        'google': {
            'is_rgb': True,
            'color_values': (169, 169, 169),
            'tcs_value': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (169, 169, 169),
            'tcs_value': None
        }
    },
    {
        'name': 'dark green',
        'google': {
            'is_rgb': True,
            'color_values': (1, 50, 32),
            'tcs_value': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 100, 0),
            'tcs_value': None
        }
    },
    {
        'name': 'dark khaki',
        'google': {
            'is_rgb': True,
            'color_values': (189, 183, 107),
            'tcs_value': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (189, 183, 107),
            'tcs_value': None
        }
    },
    {
        'name': 'dark magenta',
        'google': {
            'is_rgb': True,
            'color_values': (139, 0, 139),
            'tcs_value': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (139, 0, 139),
            'tcs_value': None
        }
    },
    {
        'name': 'dark olive green',
#         'google': {
#             'is_rgb': True,
#             'color_values': (0, 0, 0)
#         },
        'alexa': {
            'is_rgb': True,
            'color_values': (86, 103, 51),
            'tcs_value': None
        }
    },
    {
        'name': 'dark orange',
        'google': {
            'is_rgb': True,
            'color_values': (255, 140, 0),
            'tcs_value': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (255, 140, 0),
            'tcs_value': None
        }
    },
    {
        'name': 'dark orchid',
        'google': {
            'is_rgb': True,
            'color_values': (153, 50, 204),
            'tcs_value': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (153, 50, 204),
            'tcs_value': None
        }
    },
    {
        'name': 'dark red',
        'google': {
            'is_rgb': True,
            'color_values': (139, 0, 0),
            'tcs_value': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (139, 0, 0),
            'tcs_value': None
        }
    },
    {
        'name': 'dark salmon',
        'google': {
            'is_rgb': True,
            'color_values': (233, 150, 122),
            'tcs_value': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (233, 150, 122),
            'tcs_value': None
        }
    },
    {
        'name': 'dark sea green',
#         'google': {
#             'is_rgb': True,
#             'color_values': (0, 0, 0)
#         },
        'alexa': {
            'is_rgb': True,
            'color_values': (143, 188, 143),
            'tcs_value': None
        }
    },
    {
        'name': 'dark slate blue',
#         'google': {
#             'is_rgb': True,
#             'color_values': (0, 0, 0)
#         },
        'alexa': {
            'is_rgb': True,
            'color_values': (72, 61, 139),
            'tcs_value': None
        }
    },
    {
        'name': 'dark slate gray',
        'google': {
            'is_rgb': True,
            'color_values': (47, 79, 79),
            'tcs_value': None
        },
        'alexa': {                            # Need to tell Alexa to set a Full Color bulb 'to the color dark slate gray'
            'is_rgb': True,
            'color_values': (47, 79, 79),
            'tcs_value': None
        }
    },
    {
        'name': 'dark turquoise',
        'google': {
            'is_rgb': True,
            'color_values': (0, 206, 209),
            'tcs_value': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 210, 210),
            'tcs_value': None
        }
    },
    {
        'name': 'dark violet',
        'google': {
            'is_rgb': True,
            'color_values': (148, 0, 211),
            'tcs_value': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (148, 0, 211),
            'tcs_value': None
        }
    },
    {
        'name': 'daylight',                # Google uses cct for this color
        'google': {
            'is_rgb': False,
            'color_values': 5000,
            'tcs_value': 4150
        },
        'alexa': {
            'is_rgb': False,
            'color_values': 5500,
            'tcs_value': 4360
        }
    },
    {
        'name': 'deep pink',
        'google': {
            'is_rgb': True,
            'color_values': (255, 20, 147),
            'tcs_value': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (255, 20, 147),
            'tcs_value': None
        }
    },
    {
        'name': 'deep sky blue',
        'google': {
            'is_rgb': True,
            'color_values': (0, 191, 255),
            'tcs_value': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 191, 255),
            'tcs_value': None
        }
    },
    {
        'name': 'dim gray',
        'google': {
            'is_rgb': True,
            'color_values': (105, 105, 105),
            'tcs_value': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (105, 105, 105),
            'tcs_value': None
        }
    },
    {
        'name': 'dodger blue',
        'google': {
            'is_rgb': True,
            'color_values': (30, 144, 255),
            'tcs_value': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (30, 144, 255),
            'tcs_value': None
        }
    },
    {
        'name': 'firebrick',
        'google': {
            'is_rgb': True,
            'color_values': (178, 34, 34),
            'tcs_value': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (178, 34, 34),
            'tcs_value': None
        }
    },
    {
        'name': 'floral white',      # Google uses cct for this color
        'google': {
            'is_rgb': False,
            'color_values': 6100,
            'tcs_value': 4640
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (255, 250, 240),
            'tcs_value': None
        }
    },
    {
        'name': 'forest green',
        'google': {
            'is_rgb': True,
            'color_values': (34, 139, 34),
            'tcs_value': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (34, 139, 34),
            'tcs_value': None
        }
    },
    {
        'name': 'fuchsia',
        'google': {
            'is_rgb': True,
            'color_values': (193, 84, 193),
            'tcs_value': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (255, 0, 255),
            'tcs_value': None
        }
    },
    {
        'name': 'gainsboro',         # Google uses cct for this color
        'google': {
            'is_rgb': True,
            'color_values': (220, 220, 220),
            'tcs_value': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (220, 220, 220),
            'tcs_value': None
        }
    },
#     {
#         'name': 'garnet',
# #         'google': {
# #             'is_rgb': True,
# #             'color_values': (0, 0, 0)
# #         },
#         'alexa': {
#             'is_rgb': True,
#             'color_values': (0, 0, 0)
#         }
#     },
    {
        'name': 'ghost white',       # Google uses cct for this color
        'google': {
            'is_rgb': False,
            'color_values': 7000,
            'tcs_value': 5335
        },
        'alexa': {                   # Need to tell Alexa to set a Full Color bulb 'to the color dark slate gray'
            'is_rgb': True,
            'color_values': (248, 248, 255),
            'tcs_value': None
        }
    },
    {
        'name': 'gold',
        'google': {
            'is_rgb': True,
            'color_values': (165, 124, 0),
            'tcs_value': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (255, 215, 0),
            'tcs_value': None
        }
    },
    {
        'name': 'goldenrod',
        'google': {
            'is_rgb': True,
            'color_values': (218, 165, 32),
            'tcs_value': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (218, 165, 32),
            'tcs_value': None
        }
    },
    {
        'name': 'gray',
        'google': {
            'is_rgb': True,
            'color_values': (128, 128, 128),
            'tcs_value': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (128, 128, 128),
            'tcs_value': None
        }
    },
    {
        'name': 'green',
        'google': {
            'is_rgb': True,
            'color_values': (0, 255, 0),
            'tcs_value': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 255, 0),
            'tcs_value': None
        }
    },
    {
        'name': 'green yellow',
        'google': {
            'is_rgb': True,
            'color_values': (173, 255, 47),
            'tcs_value': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (173, 255, 47),
            'tcs_value': None
        }
    },
    {
        'name': 'honeydew',
        'google': {
            'is_rgb': True,
            'color_values': (240, 255, 240),
            'tcs_value': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (240, 255, 240),
            'tcs_value': None
        }
    },
    {
        'name': 'hot pink',
        'google': {
            'is_rgb': True,
            'color_values': (255, 105, 180),
            'tcs_value': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (255, 105, 180),
            'tcs_value': None
        }
    },
    {
        'name': 'incandescent',                # Google uses cct for this color
        'google': {
            'is_rgb': False,
            'color_values': 2700,
            'tcs_value': 2630
        },
        'alexa': {
            'is_rgb': False,
            'color_values': 2700,
            'tcs_value': 2630
        }
    },
    {
        'name': 'indian red',
        'google': {
            'is_rgb': True,
            'color_values': (205, 92, 92),
            'tcs_value': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (200, 100, 100),
            'tcs_value': None
        }
    },
    {
        'name': 'indigo',
        'google': {
            'is_rgb': True,
            'color_values': (75, 0, 130),
            'tcs_value': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (75, 0, 130),
            'tcs_value': None
        }
    },
    {
        'name': 'ivory',               # Google uses cct for this color
        'google': {
            'is_rgb': False,
            'color_values': 6100,
            'tcs_value': 4640
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (255, 255, 240),
            'tcs_value': None
        }
    },
    {
        'name': 'khaki',
        'google': {
            'is_rgb': True,
            'color_values': (195, 176, 145),
            'tcs_value': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (240, 230, 140),
            'tcs_value': None
        }
    },
    {
        'name': 'lavender',
        'google': {
            'is_rgb': True,
            'color_values': (181, 126, 220),
            'tcs_value': None
        },
        'alexa': {                          # These are custom values to match what Alexa chose for lavender
            'is_rgb': True,
            'color_values':(150, 127, 255),
            'tcs_value': None
        }
    },
    {
        'name': 'lavender blush',
        'google': {
            'is_rgb': True,
            'color_values': (255, 240, 245),
            'tcs_value': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (255, 240, 245),
            'tcs_value': None
        }
    },
    {
        'name': 'lawn green',
        'google': {
            'is_rgb': True,
            'color_values': (124, 252, 0),
            'tcs_value': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (124, 252, 0),
            'tcs_value': None
        }
    },
    {
        'name': 'lemon chiffon',
        'google': {
            'is_rgb': True,
            'color_values': (255, 250, 205),
            'tcs_value': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (255, 250, 205),
            'tcs_value': None
        }
    },
    {
        'name': 'light blue',
        'google': {
            'is_rgb': True,
            'color_values': (173, 216, 230),
            'tcs_value': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (191, 239, 255),
            'tcs_value': None
        }
    },
    {
        'name': 'light coral',          # The rgb values shown here come from "hey google turn the lights to the color light coral.'
        'google': {                     # Google results vary using 'light coral' and 'the color light coral'
            'is_rgb': True,
            'color_values': (240, 128, 128),
            'tcs_value': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (240, 128, 128),
            'tcs_value': None
        }
    },
    {
        'name': 'light cyan',           # The rgb values shown here come from "hey google turn the lights to the color light cyan.'
        'google': {                     # Google results vary using 'light cyan' and 'the color light cyan'
            'is_rgb': True,
            'color_values': (224, 255, 255),
            'tcs_value': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (224, 255, 255),
            'tcs_value': None
        }
    },
    {
        'name': 'light goldenrod',      # The rgb values shown here come from "hey google turn the lights to the color light goldenrod.'
        'google': {                     # Google results vary using 'light goldenrod' and 'the color light goldenrod'
            'is_rgb': True,
            'color_values': (255, 236, 139),
            'tcs_value': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (250, 250, 210),
            'tcs_value': None
        }
    },
    {
        'name': 'light gray',           # The rgb values shown here come from "hey google turn the lights to the color light gray.'
        'google': {                     # Google results vary using 'light gray' and 'the color light gray'
            'is_rgb': True,
            'color_values': (211, 211, 211),
            'tcs_value': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (211, 211, 211),
            'tcs_value': None
        }
    },
    {
        'name': 'light green',          # The rgb values shown here come from "hey google turn the lights to the color light green.'
        'google': {                     # Google results vary using 'light green' and 'the color light green'
            'is_rgb': True,
            'color_values': (144, 238, 144),
            'tcs_value': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (144, 238, 144),
            'tcs_value': None
        }
    },
    {
        'name': 'light pink',           # The rgb values shown here come from "hey google turn the lights to the color light pink.'
        'google': {                     # Google results vary using 'light pink' and 'the color light pink'
            'is_rgb': True,
            'color_values': (255, 182, 193),
            'tcs_value': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (255, 182, 193),
            'tcs_value': None
        }
    },
    {
        'name': 'light salmon',         # The rgb values shown here come from "hey google turn the lights to the color light salmon.'
        'google': {                     # Google results vary using 'light pink' and 'the color light salmon'
            'is_rgb': True,
            'color_values': (255, 160, 122),
            'tcs_value': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (250, 160, 122),
            'tcs_value': None
        }
    },
    {
        'name': 'light sea green',      # The rgb values shown here come from "hey google turn the lights to the color light salmon.'
        'google': {                     # Google results vary using 'light sea green' and 'the color light sea green'
            'is_rgb': True,
            'color_values': (32, 178, 170),
            'tcs_value': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (46, 196, 182),
            'tcs_value': None
        }
    },
    {
        'name': 'light sky blue',       # The rgb values shown here come from "hey google turn the lights to the color light sky blue.'
        'google': {                     # Google results vary using 'light sea sky blue' and 'the color light sea ky blue'
            'is_rgb': True,
            'color_values': (135, 206, 250),
            'tcs_value': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (135, 206, 250),
            'tcs_value': None
        }
    },
    {
        'name': 'light slate gray',     # The rgb values shown here come from "hey google turn the lights to the color light slate gray.'
        'google': {                     # Google results vary using 'light sea green' and 'the color light slate gray'
            'is_rgb': True,
            'color_values': (119, 136, 153),
            'tcs_value': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (119, 136, 153),
            'tcs_value': None
        }
    },
    {
        'name': 'light steel blue',     # The rgb values shown here come from "hey google turn the lights to the color light steel blue.'
        'google': {                     # Google results vary using 'light sea green' and 'the color light steel blue'
            'is_rgb': True,
            'color_values': (176, 196, 222),
            'tcs_value': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (174, 194, 223),
            'tcs_value': None
        }
    },
    {
        'name': 'light turquoise',      # The rgb values shown here come from "hey google turn the lights to the color light turquoise.'
        'google': {                     # Google results vary using 'light turquoise' and 'the color light turquoise'
            'is_rgb': True,
            'color_values': (175, 228, 222),
            'tcs_value': None
        },
#         'alexa': {
#             'is_rgb': True,
#             'color_values': (0, 0, 0)
#         }
    },
    {
        'name': 'light yellow',         # The rgb values shown here come from "hey google turn the lights to the color light yellow.'
        'google': {                     # Google results vary using 'light sea green' and 'the color light yellow'
            'is_rgb': True,
            'color_values': (255, 255, 224),
            'tcs_value': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (255, 255, 224),  # -bVal could be 237
            'tcs_value': None
        }
    },
    {
        'name': 'lime',
        'google': {
            'is_rgb': True,
            'color_values': (191, 255, 0),
            'tcs_value': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (166, 214, 40),
            'tcs_value': None
        }
    },
    {
        'name': 'lime green',
        'google': {
            'is_rgb': True,
            'color_values': (50, 205, 50),
            'tcs_value': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (50, 205, 50),
            'tcs_value': None
        }
    },
    {
        'name': 'linen',             # Google uses cct for this color
        'google': {
            'is_rgb': False,
            'color_values': 6100,
            'tcs_value': 4640
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (250, 240, 230),
            'tcs_value': None
        }
    },
    {
        'name': 'magenta',
        'google': {
            'is_rgb': True,
            'color_values': (255, 0, 255),
            'tcs_value': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (255, 0, 255),
            'tcs_value': None
        }
    },
    {
        'name': 'maroon',
        'google': {
            'is_rgb': True,
            'color_values': (128, 0, 0),
            'tcs_value': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (178, 48, 96),
            'tcs_value': None
        }
    },
    {
        'name': 'medium aquamarine',
        'google': {
            'is_rgb': True,
            'color_values': (102, 221, 170),  # -gVal could be 205
            'tcs_value': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (97, 210, 180),
            'tcs_value': None
        }
    },
    {
        'name': 'medium blue',
        'google': {
            'is_rgb': True,
            'color_values': (0, 0, 205),
            'tcs_value': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 0, 205),
            'tcs_value': None
        }
    },
    {
        'name': 'medium orchid',
#         'google': {
#             'is_rgb': True,
#             'color_values': (0, 0, 0)
#         },
        'alexa': {
            'is_rgb': True,
            'color_values': (186, 85, 211),
            'tcs_value': None
        }
    },
    {
        'name': 'medium purple',
        'google': {
            'is_rgb': True,
            'color_values': (147, 112, 219),
            'tcs_value': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (147, 112, 219),
            'tcs_value': None
        }
    },
    {
        'name': 'medium sea green',
        'google': {
            'is_rgb': True,
            'color_values': (60, 179, 113),
            'tcs_value': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (60, 179, 113),
            'tcs_value': None
        }
    },
    {
        'name': 'medium slate blue',
#         'google': {
#             'is_rgb': True,
#             'color_values': (0, 0, 0)
#         },
        'alexa': {
            'is_rgb': True,
            'color_values': (123, 104, 238),
            'tcs_value': None
        }
    },
    {
        'name': 'medium spring green',
        'google': {
            'is_rgb': True,
            'color_values': (0, 250, 154),
            'tcs_value': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 250, 154),
            'tcs_value': None
        }
    },
    {
        'name': 'medium turquoise',
        'google': {
            'is_rgb': True,
            'color_values': (72, 209, 204),
            'tcs_value': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (72, 209, 204),
            'tcs_value': None
        }
    },
    {
        'name': 'medium violet red',
#         'google': {
#             'is_rgb': True,
#             'color_values': (0, 0, 0)
#         },
        'alexa': {
            'is_rgb': True,
            'color_values': (199, 21, 133),
            'tcs_value': None
        }
    },
    {
        'name': 'midnight blue',
        'google': {
            'is_rgb': True,
            'color_values': (25, 25, 112),
            'tcs_value': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (25, 25, 112),
            'tcs_value': None
        }
    },
    {
        'name': 'mint cream',
        'google': {
            'is_rgb': True,
            'color_values': (245, 255, 250),
            'tcs_value': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (245, 255, 250),
            'tcs_value': None
        }
    },
    {
        'name': 'misty rose',
        'google': {
            'is_rgb': True,
            'color_values': (255, 228, 225),
            'tcs_value': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (255, 228, 225),
            'tcs_value': None
        }
    },
    {
        'name': 'moccasin',
#         'google': {
#             'is_rgb': True,
#             'color_values': (0, 0, 0)
#         },
        'alexa': {                   # Need to tell Alexa to set bulb 'to the color moccasin'
            'is_rgb': True,
            'color_values': (255, 228, 181),
            'tcs_value': None
        }
    },
    {
        'name': 'navajo white',      # Google uses cct for this color
        'google': {
            'is_rgb': False,
            'color_values': 5000,
            'tcs_value': 4150
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (255, 222, 173),
            'tcs_value': None
        }
    },
    {
        'name': 'navy blue',
        'google': {
            'is_rgb': True,
            'color_values': (0, 0, 128),
            'tcs_value': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 0, 128),
            'tcs_value': None
        }
    },
    {
        'name': 'old lace',          # Google uses cct for this color
        'google': {
            'is_rgb': False,
            'color_values': 6100,
            'tcs_value': 4640
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (253, 245, 230),
            'tcs_value': None
        }
    },
    {
        'name': 'olive',
        'google': {
            'is_rgb': True,
            'color_values': (128, 128, 0),
            'tcs_value': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (128, 128, 0),
            'tcs_value': None
        }
    },
    {
        'name': 'olive drab',
        'google': {                  # Need to tell Google, set the bulb 'to the color olive drab'
            'is_rgb': True,
            'color_values': (107, 142, 35),
            'tcs_value': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (107, 142, 35),
            'tcs_value': None
        }
    },
#     {
#         'name': 'olive green',
#         'google': {
#             'is_rgb': True,
#             'color_values': (0, 0, 0)
#         },
#         'alexa': {
#             'is_rgb': True,
#             'color_values': (0, 0, 0)
#         }
#     },
    {
        'name': 'orange',
        'google': {
            'is_rgb': True,
            'color_values': (255, 102, 0),
            'tcs_value': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (255, 165, 0),
            'tcs_value': None
        }
    },
    {
        'name': 'orange red',
        'google': {
            'is_rgb': True,
            'color_values': (255, 75, 0),
            'tcs_value': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (255, 75, 0),
            'tcs_value': None
        }
    },
    {
        'name': 'orchid',
        'google': {
            'is_rgb': True,
            'color_values': (218, 112, 214),
            'tcs_value': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (218, 112, 214),
            'tcs_value': None
        }
    },
    {
        'name': 'pale goldenrod',
#         'google': {
#             'is_rgb': True,
#             'color_values': (0, 0, 0)
#         },
        'alexa': {
            'is_rgb': True,
            'color_values': (238, 232, 170),
            'tcs_value': None
        }
    },
    {
        'name': 'pale green',
#         'google': {
#             'is_rgb': True,
#             'color_values': (0, 0, 0)
#         },
        'alexa': {
            'is_rgb': True,
            'color_values': (152, 251, 152),
            'tcs_value': None
        }
    },
    {
        'name': 'pale turquoise',
#         'google': {
#             'is_rgb': True,
#             'color_values': (0, 0, 0)
#         },
        'alexa': {
            'is_rgb': True,
            'color_values': (180, 255, 255),
            'tcs_value': None
        }
    },
    {
        'name': 'pale violet red',
#         'google': {
#             'is_rgb': True,
#             'color_values': (0, 0, 0)
#         },
        'alexa': {
            'is_rgb': True,
            'color_values': (219, 112, 147),
            'tcs_value': None
        }
    },
    {
        'name': 'papaya whip',
        'google': {
            'is_rgb': True,
            'color_values': (255, 239, 213),
            'tcs_value': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (255, 239, 213),
            'tcs_value': None
        }
    },
    {
        'name': 'peach puff',
        'google': {
            'is_rgb': True,
            'color_values': (255, 218, 185),
            'tcs_value': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (255, 218, 185),
            'tcs_value': None
        }
    },
    {
        'name': 'peru',
        'google': {
            'is_rgb': True,
            'color_values': (205, 133, 63),
            'tcs_value': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (205, 133, 63),
            'tcs_value': None
        }
    },
    {
        'name': 'pink',
        'google': {
            'is_rgb': True,
            'color_values': (255, 192, 203),
            'tcs_value': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (250, 185, 204),  # (250, 185, 203)
            'tcs_value': None
        }
    },
    {
        'name': 'plum',
        'google': {
            'is_rgb': True,
            'color_values': (142, 69, 133),
            'tcs_value': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (221, 160, 221),
            'tcs_value': None
        }
    },
    {
        'name': 'powder blue',
        'google': {
            'is_rgb': True,
            'color_values': (176, 224, 230),
            'tcs_value': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (174, 224, 221),
            'tcs_value': None
        }
    },
    {
        'name': 'pumpkin',                    # Need to test for Alexa
        'google': {
            'is_rgb': True,
            'color_values': (255, 117, 24),
            'tcs_value': None
        },
#         'alexa': {
#             'is_rgb': True,
#             'color_values': (0, 0, 0)
#         }
    },
    {
        'name': 'purple',
        'google': {
            'is_rgb': True,
            'color_values': (128, 0, 128),
            'tcs_value': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (160, 32, 240),
            'tcs_value': None
        }
    },
    {
        'name': 'rebecca purple',
#         'google': {
#             'is_rgb': True,
#             'color_values': (0, 0, 0)
#         },
        'alexa': {
            'is_rgb': True,
            'color_values': (102, 51, 153),
            'tcs_value': None
        }
    },
    {
        'name': 'red',
        'google': {
            'is_rgb': True,
            'color_values': (255, 0, 0),
            'tcs_value': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (255, 0, 0),
            'tcs_value': None
        }
    },
    {
        'name': 'rosy brown',
        'google': {
            'is_rgb': True,
            'color_values': (188, 143, 143),
            'tcs_value': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (188, 143, 143),
            'tcs_value': None
        }
    },
    {
        'name': 'royal blue',
        'google': {
            'is_rgb': True,
            'color_values': (0, 5, 102),
            'tcs_value': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (65, 105, 225),
            'tcs_value': None
        }
    },
    {
        'name': 'saddle brown',
#         'google': {
#             'is_rgb': True,
#             'color_values': (0, 0, 0)
#         },
        'alexa': {
            'is_rgb': True,
            'color_values': (139, 69, 19),
            'tcs_value': None
        }
    },
    {
        'name': 'salmon',
        'google': {
            'is_rgb': True,
            'color_values': (250, 128, 114),
            'tcs_value': None
        },
        'alexa': {                            # Alexa uses the 'light salmon' rgb values for salmon
            'is_rgb': True,
            'color_values': (255, 160, 125),
            'tcs_value': None
        }
    },
    {
        'name': 'sandy brown',
        'google': {
            'is_rgb': True,
            'color_values': (244, 164, 96),
            'tcs_value': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (244, 164, 96),
            'tcs_value': None
        }
    },
    {
        'name': 'sea green',
        'google': {
            'is_rgb': True,
            'color_values': (46, 139, 87),
            'tcs_value': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (46, 139, 87),
            'tcs_value': None
        }
    },
    {
        'name': 'seashell',          # Google uses cct for this color
        'google': {
            'is_rgb': False,
            'color_values': 6100,
            'tcs_value': 4640
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (255, 245, 238),
            'tcs_value': None
        }
    },
    {
        'name': 'sienna',
        'google': {
            'is_rgb': True,
            'color_values': (136, 45, 23),
            'tcs_value': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (160, 82, 45),
            'tcs_value': None
        }
    },
    {
        'name': 'silver',
        'google': {
            'is_rgb': True,
            'color_values': (192, 192, 192),
            'tcs_value': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (192, 192, 192),
            'tcs_value': None
        }
    },
#     {
#         'name': 'sky',
#         'google': {
#             'is_rgb': True,
#             'color_values': (0, 0, 0)
#         },
#         'alexa': {
#             'is_rgb': True,
#             'color_values': (0, 0, 0)
#         }
#     },
    {
        'name': 'sky blue',
        'google': {
            'is_rgb': True,
            'color_values': (135, 206, 235),
            'tcs_value': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (135, 206, 235),
            'tcs_value': None
        }
    },
#     {
#         'name': 'slate',
#         'google': {
#             'is_rgb': True,
#             'color_values': (0, 0, 0)
#         },
#         'alexa': {
#             'is_rgb': True,
#             'color_values': (0, 0, 0)
#         }
#     },
    {
        'name': 'slate blue',
        'google': {
            'is_rgb': True,
            'color_values': (106, 90, 205),
            'tcs_value': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (106, 90, 205),
            'tcs_value': None
        }
    },
    {
        'name': 'slate gray',
        'google': {
            'is_rgb': True,
            'color_values': (112, 128, 144),
            'tcs_value': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (112, 128, 144),
            'tcs_value': None
        }
    },
    {
        'name': 'smitten',
        'google': {
            'is_rgb': True,
            'color_values': (200, 65, 134),
            'tcs_value': None
        },
#         'alexa': {
#             'is_rgb': True,
#             'color_values': (0, 0, 0)
#         }
    },
    {
        'name': 'snow',                # Google uses cct for this color
        'google': {
            'is_rgb': False,
            'color_values': 6500,
            'tcs_value': 4850
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (255, 250, 250),
            'tcs_value': None
        }
    },
    {
        'name': 'soft white',                # Google uses cct for this color
        'google': {
            'is_rgb': False,
            'color_values': 3000,
            'tcs_value': 2830
        },
        'alexa': {
            'is_rgb': False,
            'color_values': 2700,
            'tcs_value': 2630
        }
    },
    {
        'name': 'spring green',
        'google': {
            'is_rgb': True,
            'color_values': (0, 255, 127),
            'tcs_value': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 255, 127),
            'tcs_value': None
        }
    },
    {
        'name': 'steel blue',
        'google': {
            'is_rgb': True,
            'color_values': (70, 130, 180),
            'tcs_value': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (70, 130, 180),
            'tcs_value': None
        }
    },
    {
        'name': 'tan',
        'google': {
            'is_rgb': True,
            'color_values': (210, 180, 140),
            'tcs_value': None
        },
        'alexa': {                           # Need to tell Alexa turn bulb 'to the color tan'
            'is_rgb': True,
            'color_values': (210, 180, 140),
            'tcs_value': None
        }
    },
    {
        'name': 'teal',
        'google': {
            'is_rgb': True,
            'color_values': (0, 128, 128),
            'tcs_value': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 128, 128),
            'tcs_value': None
        }
    },
    {
        'name': 'thistle',
        'google': {
            'is_rgb': True,
            'color_values': (216, 191, 216),
            'tcs_value': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (216, 191, 216),
            'tcs_value': None
        }
    },
    {
        'name': 'tomato',
        'google': {
            'is_rgb': True,
            'color_values': (255, 99, 71),
            'tcs_value': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (255, 99, 71),
            'tcs_value': None
        }
    },
    {
        'name': 'turquoise',
        'google': {
            'is_rgb': True,
            'color_values': (64, 224, 208),
            'tcs_value': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (64, 224, 208),
            'tcs_value': None
        }
    },
    {
        'name': 'ultramarine',               # Need to test for Alexa
        'google': {
            'is_rgb': True,
            'color_values': (18, 10, 143),
            'tcs_value': None
        },
#         'alexa': {
#             'is_rgb': True,
#             'color_values': (0, 0, 0)
#         }
    },
    {
        'name': 'vermillion',                # Need to test for Alexa
        'google': {
            'is_rgb': True,
            'color_values': (217, 56, 30),
            'tcs_value': None
        },
#         'alexa': {
#             'is_rgb': True,
#             'color_values': (0, 0, 0)
#         }
    },
    {
        'name': 'violet',
        'google': {
            'is_rgb': True,
            'color_values': (127, 0, 255),
            'tcs_value': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (238, 130, 238),
            'tcs_value': None
        }
    },
    {
        'name': 'warm',                # Google uses cct for this color
#         'google': {
#             'is_rgb': False,
#             'color_values': ''
#         },
        'alexa': {
            'is_rgb': False,
            'color_values': 2200,
            'tcs_value': 2320
        }
    },
    {
        'name': 'warm white',                # Google uses cct for this color
        'google': {
            'is_rgb': False,
            'color_values': 3000,
            'tcs_value': 2830
        },
        'alexa': {
            'is_rgb': False,
            'color_values': 2200,
            'tcs_value': 2320
        }
    },
    {
        'name': 'web gray',
#         'google': {
#             'is_rgb': True,
#             'color_values': (0, 0, 0)
#         },
        'alexa': {
            'is_rgb': True,
            'color_values': (128, 128, 128),
            'tcs_value': None
        }
    },
    {
        'name': 'web green',
#         'google': {
#             'is_rgb': True,
#             'color_values': (0, 0, 0)
#         },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 128, 0),
            'tcs_value': None
        }
    },
    {
        'name': 'web maroon',
#         'google': {
#             'is_rgb': True,
#             'color_values': (128, 0, 0)
#         },
        'alexa': {
            'is_rgb': True,
            'color_values': (178, 48, 96),
            'tcs_value': None
        }
    },
    {
        'name': 'web purple',
#         'google': {
#             'is_rgb': True,
#             'color_values': (128, 0, 128)
#         },
        'alexa': {
            'is_rgb': True,
            'color_values': (128, 0, 128),
            'tcs_value': None
        }
    },
    {
        'name': 'wheat',
        'google': {
            'is_rgb': True,
            'color_values': (245, 222, 179),
            'tcs_value': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (245, 222, 179),
            'tcs_value': None
        }
    },
    {
        'name': 'white',                   # Google uses cct for this color
        'google': {
            'is_rgb': False,
            'color_values': 5000,
            'tcs_value': 4150
        },
        'alexa': {
            'is_rgb': False,
            'color_values': 4000,
            'tcs_value': 3350
        }
    },
    {
        'name': 'white smoke',             # Google uses cct for this color
        'google': {
            'is_rgb': False,
            'color_values': 7000,
            'tcs_value': 5335
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (245, 245, 245),
            'tcs_value': None
        }
    },
    {
        'name': 'yellow',
        'google': {
            'is_rgb': True,
            'color_values': (255, 255, 0),
            'tcs_value': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (255, 255, 0),
            'tcs_value': None
        }
    },
    {
        'name': 'yellow green',
        'google': {
            'is_rgb': True,
            'color_values': (154, 205, 50),
            'tcs_value': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (154, 205, 50),
            'tcs_value': None
        }
    }
]


if __name__ == '__main__':
#     for color in supported_colors_list:
#         try:
#             if not color['alexa']['is_rgb']:
#                 print(color['name'])
#         except Exception as ex:
#             pass

    voice_agent = 'google'
    color_list = []
    for color in supported_colors_list:
        if color.get(voice_agent):
            if color.get(voice_agent).get('is_rgb'):
                color_list.append(color)

    for color in color_list:
        print(color['name'], color[voice_agent]['tcs_value'])

    print('color_list length: ', len(color_list))

else:
    print('Successfully imported supported colors.py')


