# Color values can be found here: https://en.wikipedia.org/wiki/List_of_colors_(compact)

supported_colors_list = [
    {
        'name': 'alice blue',
        'google': {
            'is_rgb': True,
            'color_values': (240, 248, 255)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (240, 248, 255)
        }
    },
    {
#         'name': 'almond',             # Google uses color_values for this color
#         'google': {
#             'is_rgb': True,
#             'color_values': (0, 0, 0)
#         },
#         'alexa': {
#             'is_rgb': True,
#             'color_values': (0, 0, 0)
#         }
    },
    {
        'name': 'antique white',      # Google uses color_values for this color
        'google': {
            'is_rgb': False,
            'color_values': ''
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (250, 235, 215)
        }
    },
    {
        'name': 'aqua',
        'google': {
            'is_rgb': True,
            'color_values': (0, 255, 255),
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 255, 255),
        }
    },
    {
        'name': 'aquamarine',
        'google': {
            'is_rgb': True,
            'color_values': (127, 255, 212),
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (127, 255, 212),
        }
    },
    {
        'name': 'azure',
        'google': {
            'is_rgb': True,
            'color_values': (0, 127, 255)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (240, 255, 255)
        }
    },
    {
        'name': 'beige',              # Google uses color_values for this color
        'google': {
            'is_rgb': False,
            'color_values': ''
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (245, 245, 220)
        }
    },
    {
        'name': 'bisque',             # Google uses color_values for this color
        'google': {
            'is_rgb': False,
            'color_values': ''
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (255, 228, 196)
        }
    },
    {
        'name': 'black',
        'google': {
            'is_rgb': True,
            'color_values': (0, 0, 0)
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
            'color_values': (255, 235, 205)
        }
    },
    {
        'name': 'blue',
        'google': {
            'is_rgb': True,
            'color_values': (0, 0, 255)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 0, 255)
        }
    },
    {
        'name': 'blue violet',
        'google': {
            'is_rgb': True,
            'color_values': (138, 43, 226)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (138, 43, 226)
        }
    },
    {
        'name': 'brown',
        'google': {
            'is_rgb': True,
            'color_values': (150, 75, 0)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (165, 42, 42)
        }
    },
#     {
#         'name': 'burlywood',         # Google uses cct for this color
#         'color_values': '',
#         'is_rgb': False,
#         'va_support': ['Alexa']
#     },
    {
        'name': 'candlelight',    # Google uses cct for this color
        'google': {
            'is_rgb': False,
            'color_values': '2000'
        },
        'alexa': {
            'is_rgb': False,
            'color_values': '2200'
        }
    },
    {
        'name': 'cadet blue',
        'google': {
            'is_rgb': True,
            'color_values': (95, 158, 160)
        },
        'alexa': {                           # Need to tell Alexa to set a Full Color bulb 'to the color cadet blue'
            'is_rgb': True,
            'color_values': (95, 158, 160)
        }
    },
    {
        'name': 'charteuse',
        'google': {
            'is_rgb': True,
            'color_values': (223, 255, 0)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (127, 255, 0)
        }
    },
    {
        'name': 'chocolate',
        'google': {
            'is_rgb': True,
            'color_values': (123, 63, 0)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (210, 105, 30)
        }
    },
    {
        'name': 'coral',
        'google': {
            'is_rgb': True,
            'color_values': (255, 127, 80)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (255, 127, 80)
        }
    },
    {
        'name': 'cornflower',
        'google': {
            'is_rgb': True,
            'color_values': (100, 149, 237)
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
            'color_values': (100, 149, 237)
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
            'color_values': '6500'
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (255, 248, 220)
        }
    },
    {
        'name': 'crimson',
        'google': {
            'is_rgb': True,
            'color_values': (220, 20, 60)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (220, 20, 60)
        }
    },
    {
        'name': 'cyan',
        'google': {
            'is_rgb': True,
            'color_values': (0, 255, 255)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 255, 255)
        }
    },
    {
        'name': 'dark blue',
        'google': {
            'is_rgb': True,
            'color_values': (0, 0, 139)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 0, 139)
        }
    },
    {
        'name': 'dark cyan',
        'google': {
            'is_rgb': True,
            'color_values': (0, 139, 139)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 139, 139)
        }
    },
    {
        'name': 'dark goldenrod',
        'google': {
            'is_rgb': True,
            'color_values': (184, 134, 11)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (184, 134, 11)
        }
    },
    {
        'name': 'dark gray',
        'google': {
            'is_rgb': True,
            'color_values': (169, 169, 169)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (169, 169, 169)
        }
    },
    {
        'name': 'dark green',
        'google': {
            'is_rgb': True,
            'color_values': (1, 50, 32)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 100, 0)
        }
    },
    {
        'name': 'dark khaki',
        'google': {
            'is_rgb': True,
            'color_values': (189, 183, 107)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (189, 183, 107)
        }
    },
    {
        'name': 'dark magenta',
        'google': {
            'is_rgb': True,
            'color_values': (139, 0, 139)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (139, 0, 139)
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
            'color_values': (86, 103, 51)
        }
    },
    {
        'name': 'dark orange',
        'google': {
            'is_rgb': True,
            'color_values': (255, 140, 0)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (255, 140, 0)
        }
    },
    {
        'name': 'dark orchid',
        'google': {
            'is_rgb': True,
            'color_values': (153, 50, 204)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (153, 50, 204)
        }
    },
    {
        'name': 'dark red',
        'google': {
            'is_rgb': True,
            'color_values': (139, 0, 0)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (139, 0, 0)
        }
    },
    {
        'name': 'dark salmon',
        'google': {
            'is_rgb': True,
            'color_values': (233, 150, 122)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (233, 150, 122)
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
            'color_values': (143, 188, 143)
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
            'color_values': (72, 61, 139)
        }
    },
    {
        'name': 'dark slate gray',
        'google': {
            'is_rgb': True,
            'color_values': (47, 79, 79)
        },
        'alexa': {                            # Need to tell Alexa to set a Full Color bulb 'to the color dark slate gray'
            'is_rgb': True,
            'color_values': (47, 79, 79)
        }
    },
    {
        'name': 'dark turquoise',
        'google': {
            'is_rgb': True,
            'color_values': (0, 206, 209)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 210, 210)
        }
    },
    {
        'name': 'dark violet',
        'google': {
            'is_rgb': True,
            'color_values': (148, 0, 211)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (148, 0, 211)
        }
    },
    {
        'name': 'deep pink',
        'google': {
            'is_rgb': True,
            'color_values': (255, 20, 147)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (255, 20, 147)
        }
    },
    {
        'name': 'deep sky blue',
        'google': {
            'is_rgb': True,
            'color_values': (0, 191, 255)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 191, 255)
        }
    },
    {
        'name': 'dim gray',
        'google': {
            'is_rgb': True,
            'color_values': (105, 105, 105)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (105, 105, 105)
        }
    },
    {
        'name': 'dodger blue',
        'google': {
            'is_rgb': True,
            'color_values': (30, 144, 255)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (30, 144, 255)
        }
    },
    {
        'name': 'firebrick',
        'google': {
            'is_rgb': True,
            'color_values': (178, 34, 34)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (178, 34, 34)
        }
    },
    {
        'name': 'floral white',      # Google uses cct for this color
        'google': {
            'is_rgb': False,
            'color_values': ''
        },
        'alexa': {
            'is_rgb': True,
            'color_values': 'color_values': (255, 250, 240)
        }
    },
    {
        'name': 'forest green',
        'google': {
            'is_rgb': True,
            'color_values': (34, 139, 34)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (34, 139, 34)
        }
    },
    {
        'name': 'fuchsia',
        'google': {
            'is_rgb': True,
            'color_values': (193, 84, 193)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (255, 0, 255)
        }
    },
    {
        'name': 'gainsboro',         # Google uses cct for this color
        'google': {
            'is_rgb': False,
            'color_values': ''
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (220, 0, 220)
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
            'color_values': ''
        },
        'alexa': {                   # Need to tell Alexa to set a Full Color bulb 'to the color dark slate gray'
            'is_rgb': True,
            'color_values': (248, 248, 255)
        }
    },
    {
        'name': 'gold',
        'google': {
            'is_rgb': True,
            'color_values': (165, 124, 0)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (255, 215, 0)
        }
    },
    {
        'name': 'goldenrod',
        'google': {
            'is_rgb': True,
            'color_values': (218, 165, 32)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (218, 165, 32)
        }
    },
    {
        'name': 'gray',
        'google': {
            'is_rgb': True,
            'color_values': (128, 128, 128)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (128, 128, 128)
        }
    },
    {
        'name': 'green',
        'google': {
            'is_rgb': True,
            'color_values': (0, 255, 0)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 255, 0)
        }
    },
    {
        'name': 'green yellow',
        'google': {
            'is_rgb': True,
            'color_values': (173, 255, 47)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (173, 255, 47)
        }
    },
    {
        'name': 'honeydew',
        'google': {
            'is_rgb': True,
            'color_values': (240, 255, 240)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (240, 255, 240)
        }
    },
    {
        'name': 'hot pink',
        'google': {
            'is_rgb': True,
            'color_values': (255, 105, 180)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (255, 105, 180)
        }
    },
    {
        'name': 'indian red',
        'google': {
            'is_rgb': True,
            'color_values': (205, 92, 92)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (200, 100, 100)
        }
    },
    {
        'name': 'indigo',
        'google': {
            'is_rgb': True,
            'color_values': (75, 0, 130)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (75, 0, 130)
        }
    },
    {
        'name': 'ivory',               # Google uses cct for this color
        'google': {
            'is_rgb': False,
            'color_values': ''
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (255, 255, 240)
        }
    },
    {
        'name': 'khaki',
        'google': {
            'is_rgb': True,
            'color_values': (195, 176, 145)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (240, 230, 140)
        }
    },
    {
        'name': 'lavender',
        'google': {
            'is_rgb': True,
            'color_values': (181, 126, 220)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 0, 0)
        }
    },
    {
        'name': 'lavender blush',
        'google': {
            'is_rgb': True,
            'color_values': (255, 240, 245)
        },
        'alexa': {                               # These are custom values to match what Alexa chose for lavender
            'is_rgb': True,
            'color_values': (150, 127, 255)
        }
    },
    {
        'name': 'lawn green',
        'google': {
            'is_rgb': True,
            'color_values': (124, 252, 0)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (124, 252, 0)
        }
    },
    {
        'name': 'lemon chiffon',
        'google': {
            'is_rgb': True,
            'color_values': (255, 250, 205)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (255, 250, 205)
        }
    },
    {
        'name': 'light blue',
        'google': {
            'is_rgb': True,
            'color_values': (173, 216, 230)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 0, 0)
        }
    },
    {
        'name': 'ligth coral',          # The is_rgb values shown here come from "hey google turn the lights to the color light coral.'
        'google': {                     # Google results vary using 'light coral' and 'the color light coral'
            'is_rgb': True,
            'color_values': (240, 128, 128)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 0, 0)
        }
    },
    {
        'name': 'light cyan',           # The is_rgb values shown here come from "hey google turn the lights to the color light cyan.'
        'google': {                     # Google results vary using 'light cyan' and 'the color light cyan'
            'is_rgb': True,
            'color_values': (224, 255, 255)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 0, 0)
        }
    },
    {
        'name': 'light goldenrod',      # The is_rgb values shown here come from "hey google turn the lights to the color light goldenrod.'
        'google': {                     # Google results vary using 'light goldenrod' and 'the color light goldenrod'
            'is_rgb': True,
            'color_values': (255, 236, 139)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 0, 0)
        }
    },
    {
        'name': 'light gray',           # The is_rgb values shown here come from "hey google turn the lights to the color light gray.'
        'google': {                     # Google results vary using 'light gray' and 'the color light gray'
            'is_rgb': True,
            'color_values': (211, 211, 211)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 0, 0)
        }
    },
    {
        'name': 'light green',          # The is_rgb values shown here come from "hey google turn the lights to the color light green.'
        'google': {                     # Google results vary using 'light green' and 'the color light green'
            'is_rgb': True,
            'color_values': (144, 238, 144)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 0, 0)
        }
    },
    {
        'name': 'light pink',           # The is_rgb values shown here come from "hey google turn the lights to the color light pink.'
        'google': {                     # Google results vary using 'light pink' and 'the color light pink'
            'is_rgb': True,
            'color_values': (255, 182, 193)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 0, 0)
        }
    },
    {
        'name': 'light salmon',         # The is_rgb values shown here come from "hey google turn the lights to the color light salmon.'
        'google': {                     # Google results vary using 'light pink' and 'the color light salmon'
            'is_rgb': True,
            'color_values': (255, 160, 122)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 0, 0)
        }
    },
    {
        'name': 'light sea green',      # The is_rgb values shown here come from "hey google turn the lights to the color light salmon.'
        'google': {                     # Google results vary using 'light sea green' and 'the color light sea green'
            'is_rgb': True,
            'color_values': (32, 178, 170)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 0, 0)
        }
    },
    {
        'name': 'light sky blue',       # The is_rgb values shown here come from "hey google turn the lights to the color light sky blue.'
        'google': {                     # Google results vary using 'light sea sky blue' and 'the color light sea ky blue'
            'is_rgb': True,
            'color_values': (135, 206, 250)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 0, 0)
        }
    },
    {
        'name': 'light slate gray',     # The is_rgb values shown here come from "hey google turn the lights to the color light slate gray.'
        'google': {                     # Google results vary using 'light sea green' and 'the color light slate gray'
            'is_rgb': True,
            'color_values': (119, 136, 153)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 0, 0)
        }
    },
    {
        'name': 'light steel blue',     # The is_rgb values shown here come from "hey google turn the lights to the color light steel blue.'
        'google': {                     # Google results vary using 'light sea green' and 'the color light steel blue'
            'is_rgb': True,
            'color_values': (176, 196, 222)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 0, 0)
        }
    },
    {
        'name': 'light turquoise',      # The is_rgb values shown here come from "hey google turn the lights to the color light turquoise.'
        'google': {                     # Google results vary using 'light turquoise' and 'the color light turquoise'
            'is_rgb': True,
            'color_values': (175, 228, 222)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 0, 0)
        }
    },
    {
        'name': 'light yellow',         # The is_rgb values shown here come from "hey google turn the lights to the color light yellow.'
        'google': {                     # Google results vary using 'light sea green' and 'the color light yellow'
            'is_rgb': True,
            'color_values': (255, 255, 224)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 0, 0)
        }
    },
    {
        'name': 'lime',
        'google': {
            'is_rgb': True,
            'color_values': (191, 255, 0)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 0, 0)
        }
    },
    {
        'name': 'lime green',
        'google': {
            'is_rgb': True,
            'color_values': (50, 205, 50)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 0, 0)
        }
    },
    {
        'name': 'linen',             # Google uses cct for this color
        'google': {
            'is_rgb': False,
            'color_values': ''
        },
        'alexa': {
            'is_rgb': False,
            'color_values': ''
        }
    },
    {
        'name': 'magenta',
        'google': {
            'is_rgb': True,
            'color_values': (255, 0, 255)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 0, 0)
        }
    },
    {
        'name': 'maroon',
        'google': {
            'is_rgb': True,
            'color_values': (128, 0, 0)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 0, 0)
        }
    },
    {
        'name': 'medium aquamarine',
        'google': {
            'is_rgb': True,
            'color_values': (102, 221, 170)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 0, 0)
        }
    },
    {
        'name': 'medium blue',
        'google': {
            'is_rgb': True,
            'color_values': (0, 0, 205)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 0, 0)
        }
    },
#     {
#         'name': 'medium orchid',
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
        'name': 'medium purple',
        'google': {
            'is_rgb': True,
            'color_values': (147, 112, 219)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 0, 0)
        }
    },
    {
        'name': 'medium sea green',
        'google': {
            'is_rgb': True,
            'color_values': (60, 179, 113)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 0, 0)
        }
    },
#     {
#         'name': 'medium slate blue',
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
        'name': 'medium spring green',
        'google': {
            'is_rgb': True,
            'color_values': (0, 250, 154)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 0, 0)
        }
    },
    {
        'name': 'medium turquoise',
        'google': {
            'is_rgb': True,
            'color_values': (72, 209, 204)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 0, 0)
        }
    },
#     {
#         'name': 'medium violet red',
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
        'name': 'midnight blue',
        'google': {
            'is_rgb': True,
            'color_values': (25, 25, 112)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 0, 0)
        }
    },
    {
        'name': 'mint cream',
        'google': {
            'is_rgb': True,
            'color_values': (245, 255, 250)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 0, 0)
        }
    },
    {
        'name': 'misty rose',
        'google': {
            'is_rgb': True,
            'color_values': (255, 228, 225)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 0, 0)
        }
    },
#     {
#         'name': 'moccasin',
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
        'name': 'navajo white',      # Google uses cct for this color
        'google': {
            'is_rgb': False,
            'color_values': ''
        },
        'alexa': {
            'is_rgb': False,
            'color_values': ''
        }
    },
    {
        'name': 'navy blue',
        'google': {
            'is_rgb': True,
            'color_values': (0, 0, 128)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 0, 0)
        }
    },
    {
        'name': 'old lace',          # Google uses cct for this color
        'google': {
            'is_rgb': False,
            'color_values': ''
        },
        'alexa': {
            'is_rgb': False,
            'color_values': ''
        }
    },
    {
        'name': 'olive',
        'google': {
            'is_rgb': True,
            'color_values': (128, 128, 0)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 0, 0)
        }
    },
#     {
#         'name': 'olive drab',
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
        'name': 'olive green',
        'google': {
            'is_rgb': True,
            'color_values': (107, 142, 35)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 0, 0)
        }
    },
    {
        'name': 'orange',
        'google': {
            'is_rgb': True,
            'color_values': (255, 102, 0)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 0, 0)
        }
    },
    {
        'name': 'orange red',
        'google': {
            'is_rgb': True,
            'color_values': (255, 75, 0)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 0, 0)
        }
    },
    {
        'name': 'orchid',
        'google': {
            'is_rgb': True,
            'color_values': (218, 112, 214)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 0, 0)
        }
    },
#     {
#         'name': 'pale goldenrod',
#         'google': {
#             'is_rgb': True,
#             'color_values': (0, 0, 0)
#         },
#         'alexa': {
#             'is_rgb': True,
#             'color_values': (0, 0, 0)
#         }
#     },
#     {
#         'name': 'pale green',
#         'google': {
#             'is_rgb': True,
#             'color_values': (0, 0, 0)
#         },
#         'alexa': {
#             'is_rgb': True,
#             'color_values': (0, 0, 0)
#         }
#     },
#     {
#         'name': 'pale turquoise',
#         'google': {
#             'is_rgb': True,
#             'color_values': (0, 0, 0)
#         },
#         'alexa': {
#             'is_rgb': True,
#             'color_values': (0, 0, 0)
#         }
#     },
#     {
#         'name': 'pale violet red',
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
        'name': 'papaya whip',
        'google': {
            'is_rgb': True,
            'color_values': (255, 239, 213)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 0, 0)
        }
    },
    {
        'name': 'peach puff',
        'google': {
            'is_rgb': True,
            'color_values': (255, 218, 185)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 0, 0)
        }
    },
    {
        'name': 'peru',
        'google': {
            'is_rgb': True,
            'color_values': (205, 133, 63)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 0, 0)
        }
    },
    {
        'name': 'pink',
        'google': {
            'is_rgb': True,
            'color_values': (255, 192, 203)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 0, 0)
        }
    },
    {
        'name': 'plum',
        'google': {
            'is_rgb': True,
            'color_values': (142, 69, 133)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 0, 0)
        }
    },
    {
        'name': 'powder blue',
        'google': {
            'is_rgb': True,
            'color_values': (176, 224, 230)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 0, 0)
        }
    },
    {
        'name': 'purple',
        'google': {
            'is_rgb': True,
            'color_values': (128, 0, 128)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (160, 32, 240)
        }
    },
    {
        'name': 'pumpkin',                    # Need to test for Alexa
        'google': {
            'is_rgb': True,
            'color_values': (255, 117, 24)
        },
#         'alexa': {
#             'is_rgb': True,
#             'color_values': (0, 0, 0)
#         }
    },
#     {
#         'name': 'rebecca purple',
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
        'name': 'red',
        'google': {
            'is_rgb': True,
            'color_values': (255, 0, 0)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 0, 0)
        }
    },
    {
        'name': 'rosy brown',
        'google': {
            'is_rgb': True,
            'color_values': (188, 143, 143)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 0, 0)
        }
    },
    {
        'name': 'royal blue',
        'google': {
            'is_rgb': True,
            'color_values': (0, 5, 102)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 0, 0)
        }
    },
#     {
#         'name': 'saddle brown',
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
        'name': 'salmon',
        'google': {
            'is_rgb': True,
            'color_values': (250, 128, 114)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 0, 0)
        }
    },
    {
        'name': 'sandy brown',
        'google': {
            'is_rgb': True,
            'color_values': (244, 164, 96)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 0, 0)
        }
    },
    {
        'name': 'sea green',
        'google': {
            'is_rgb': True,
            'color_values': (46, 139, 87)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 0, 0)
        }
    },
    {
        'name': 'seashell',          # Google uses cct for this color
        'google': {
            'is_rgb': False,
            'color_values': ''
        },
        'alexa': {
            'is_rgb': False,
            'color_values': ''
        }
    },
    {
        'name': 'sienna',
        'google': {
            'is_rgb': True,
            'color_values': (136, 45, 23)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 0, 0)
        }
    },
    {
        'name': 'silver',
        'google': {
            'is_rgb': True,
            'color_values': (192, 192, 192)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 0, 0)
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
            'color_values': (135, 206, 235)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 0, 0)
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
            'color_values': (106, 90, 205)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 0, 0)
        }
    },
    {
        'name': 'slate gray',
        'google': {
            'is_rgb': True,
            'color_values': (112, 128, 144)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 0, 0)
        }
    },
    {
        'name': 'smitten',
        'google': {
            'is_rgb': True,
            'color_values': (200, 65, 134)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 0, 0)
        }
    },
    {
        'name': 'snow',                # Google uses cct for this color
        'google': {
            'is_rgb': False,
            'color_values': ''
        },
        'alexa': {
            'is_rgb': False,
            'color_values': ''
        }
    },
    {
        'name': 'spring green',
        'google': {
            'is_rgb': True,
            'color_values': (0, 255, 127)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 0, 0)
        }
    },
    {
        'name': 'steel blue',
        'google': {
            'is_rgb': True,
            'color_values': (70, 130, 180)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 0, 0)
        }
    },
    {
        'name': 'tan',
        'google': {
            'is_rgb': True,
            'color_values': (210, 180, 140)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 0, 0)
        }
    },
    {
        'name': 'teal',
        'google': {
            'is_rgb': True,
            'color_values': (0, 128, 128)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 0, 0)
        }
    },
    {
        'name': 'thistle',
        'google': {
            'is_rgb': True,
            'color_values': (216, 191, 216)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 0, 0)
        }
    },
    {
        'name': 'tomato',
        'google': {
            'is_rgb': True,
            'color_values': (255, 99, 71)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 0, 0)
        }
    },
    {
        'name': 'turquoise',
        'google': {
            'is_rgb': True,
            'color_values': (64, 224, 208)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 0, 0)
        }
    },
    {
        'name': 'ultramarine',               # Need to test for Alexa
        'google': {
            'is_rgb': True,
            'color_values': (18, 10, 143)
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
            'color_values': (217, 56, 30)
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
            'color_values': (127, 0, 255)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 0, 0)
        }
    },
#     {
#         'name': 'web gray',
#         'google': {
#             'is_rgb': True,
#             'color_values': (0, 0, 0)
#         },
#         'alexa': {
#             'is_rgb': True,
#             'color_values': (0, 0, 0)
#         }
#     },
#     {
#         'name': 'web green',
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
        'name': 'web maroon',
#         'google': {
#             'is_rgb': True,
#             'color_values': (128, 0, 0)
#         },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 0, 0)
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
            'color_values': (0, 0, 0)
        }
    },
    {
        'name': 'wheat',
        'google': {
            'is_rgb': True,
            'color_values': (245, 222, 179)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 0, 0)
        }
    },
    {
        'name': 'white',                   # Google uses cct for this color
        'google': {
            'is_rgb': False,
            'color_values': ''
        },
        'alexa': {
            'is_rgb': False,
            'color_values': ''
        }
    },
    {
        'name': 'white smoke',             # Google uses cct for this color
        'google': {
            'is_rgb': False,
            'color_values': ''
        },
        'alexa': {
            'is_rgb': False,
            'color_values': ''
        }
    },
    {
        'name': 'yellow',
        'google': {
            'is_rgb': True,
            'color_values': (255, 255, 0)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 0, 0)
        }
    },
    {
        'name': 'yellow green',
        'google': {
            'is_rgb': True,
            'color_values': (154, 205, 50)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 0, 0)
        }
    }
]

# for color in supported_colors_list:
#     try:
#         if not color['alexa']['is_rgb']:
#             print(color['name'])
#     except Exception as ex:
#         pass
