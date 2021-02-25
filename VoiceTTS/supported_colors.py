# Color values can be found here: https://en.wikipedia.org/wiki/List_of_colors_(compact)

# RGB color values given in tuples are (R, G, B)

# tcs34725 color temperature equation y = 0.6091(x) + 986.41, where x = CCT value spoken to the voice agent
# and y = calculated sensor value to verify with (values around 5000 deg. K will be less than sensor reading).
# TCS34725 sesnor gain is set at 4.

# tcs_color_100 values are tcs.rgb_bytes values taken at 100% brightness and sensor gain set to 60.

# lux_coeff are (b0, b1, b2) where f(brightness) = b2*x^2 + b1*x + b0

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
    # {
    #     'name': 'almond',
    #     'google': {
    #         'is_rgb': True,
    #         'color_values': (239, 222, 205)
    #     },
    #     # 'alexa': {
    #     #     'is_rgb': True,
    #     #     'color_values': (0, 0, 0)
    #     # }
    # },
    {
        'name': 'antique white',      # Google uses cct for this color
        'google': {
            'is_rgb': False,
            'color_values': 5500
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
            'color_values': (0, 255, 255)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 255, 255)
        }
    },
    {
        'name': 'aquamarine',
        'google': {
            'is_rgb': True,
            'color_values': (127, 255, 212)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (127, 255, 212)
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
    # {
    #     'name': 'beige',              # Google uses cct for this color
    #     'google': {
    #         'is_rgb': False,
    #         'color_values': 5000
    #     },
    #     'alexa': {
    #         'is_rgb': True,
    #         'color_values': (245, 245, 220)
    #     }
    # },
    # {
    #     'name': 'bisque',             # Google uses cct for this color
    #     # 'google': {
    #     #     'is_rgb': False,
    #     #     'color_values': ''
    #     # },
    #     'alexa': {
    #         'is_rgb': True,
    #         'color_values': (255, 228, 196)
    #     }
    # },
    # {
    #     'name': 'black',
    #     'google': {
    #         'is_rgb': True,
    #         'color_values': (0, 0, 0)
    #     },
    #     'alexa': {
    #         'is_rgb': True,
    #         'color_values': (0, 0, 0)
    #     }
    # },
    {
        'name': 'blanched almond',    # Google uses cct for this color
        # 'google': {
        #     'is_rgb': False,
        #     'color_values': ''
        # },
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
    # {
    #     'name': 'burlywood',         # Google uses cct for this color
    #     'google': {
    #         'is_rgb': False,
    #         'color_values': ''
    #     },
    #     'alexa': {
    #         'is_rgb': False,
    #         'color_values': '',
    #         'tsl_brt_100': None
    #     }
    # },
    {
        'name': 'candlelight',       # Google uses cct for this color
        'google': {
            'is_rgb': False,
            'color_values': 2000
        },
        'alexa': {
            'is_rgb': False,
            'color_values': 2200
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
        'name': 'chartreuse',
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
        'name': 'cool',                # Google uses cct for this color
        # 'google': {
        #     'is_rgb': False,
        #     'color_values': ''
        # },
        'alexa': {
            'is_rgb': False,
            'color_values': 7000  # might be 6800
        }
    },
    {
        'name': 'cool white',                # Google uses cct for this color
        'google': {
            'is_rgb': False,
            'color_values': 4000
        },
        'alexa': {
            'is_rgb': False,
            'color_values': 7000
        }
    },
    {
        'name': 'coral',
        'google': {
            'is_rgb': True,
            'color_values': (255, 127, 80)  # need to recheck color_values
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (255, 127, 80)  # need to recheck color_values
        }
    },
    {
        'name': 'cornflower',
        'google': {
            'is_rgb': True,
            'color_values': (100, 149, 237)
        },
        # 'alexa': {
        #     'is_rgb': True,
        #     'color_values': (0, 0, 0)
        # }
    },
    {
        'name': 'cornflower blue',           # Need to test for Alexa
        'google': {
            'is_rgb': True,
            'color_values': (100, 149, 237)
        },
        # 'alexa': {
        #     'is_rgb': True,
        #     'color_values': (0, 0, 0)
        # }
    },
    # {
    #     'name': 'cornsilk',
    #     # 'google': {
    #     #     'is_rgb': False,
    #     #     'color_values': 6500
    #     # },
    #     'alexa': {
    #         'is_rgb': True,
    #         'color_values': (255, 248, 220)
    #     }
    # },
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
        # 'google': {
        #     'is_rgb': True,
        #     'color_values': (0, 0, 0)
        # },
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
        # 'google': {
        #     'is_rgb': True,
        #     'color_values': (0, 0, 0)
        # },
        'alexa': {
            'is_rgb': True,
            'color_values': (143, 188, 143)
        }
    },
    {
        'name': 'dark slate blue',
        # 'google': {
        #     'is_rgb': True,
        #     'color_values': (0, 0, 0)
        # },
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
        'name': 'daylight',                # Google uses cct for this color
        'google': {
            'is_rgb': False,
            'color_values': 5000
        },
        'alexa': {
            'is_rgb': False,
            'color_values': 5500
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
            'color_values': 6100
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (255, 250, 240)
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
    # {
    #     'name': 'gainsboro',         # Google uses cct for this color
    #     # 'google': {
    #     #     'is_rgb': True,
    #     #     'color_values': (220, 220, 220)
    #     # },
    #     'alexa': {
    #         'is_rgb': True,
    #         'color_values': (220, 220, 220)
    #     }
    # },
    # {
    #     'name': 'garnet',
    #     'google': {
    #         'is_rgb': True,
    #         'color_values': (0, 0, 0)
    #     },
    #     'alexa': {
    #         'is_rgb': True,
    #         'color_values': (0, 0, 0)
    #     }
    # },
    {
        'name': 'ghost white',       # Google uses cct for this color
        'google': {
            'is_rgb': False,
            'color_values': 7000
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
        'name': 'incandescent',                # Google uses cct for this color
        'google': {
            'is_rgb': False,
            'color_values': 2700
        },
        'alexa': {
            'is_rgb': False,
            'color_values': 2700,
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
            'color_values': 6100
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
        'alexa': {                          # These are custom values to match what Alexa chose for lavender
            'is_rgb': True,
            'color_values':(150, 127, 255)
        }
    },
    {
        'name': 'lavender blush',
        'google': {
            'is_rgb': True,
            'color_values': (255, 240, 245)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (255, 240, 245)
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
            'color_values': (191, 239, 255)
        }
    },
    {
        'name': 'light coral',          # The rgb values shown here come from "hey google turn the lights to the color light coral.'
        'google': {                     # Google results vary using 'light coral' and 'the color light coral'
            'is_rgb': True,
            'color_values': (240, 128, 128)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (240, 128, 128)
        }
    },
    {
        'name': 'light cyan',           # The rgb values shown here come from "hey google turn the lights to the color light cyan.'
        'google': {                     # Google results vary using 'light cyan' and 'the color light cyan'
            'is_rgb': True,
            'color_values': (224, 255, 255)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (224, 255, 255)
        }
    },
    {
        'name': 'light goldenrod',      # The rgb values shown here come from "hey google turn the lights to the color light goldenrod.'
        'google': {                     # Google results vary using 'light goldenrod' and 'the color light goldenrod'
            'is_rgb': True,
            'color_values': (255, 236, 139)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (250, 250, 210)
        }
    },
    {
        'name': 'light gray',           # The rgb values shown here come from "hey google turn the lights to the color light gray.'
        'google': {                     # Google results vary using 'light gray' and 'the color light gray'
            'is_rgb': True,
            'color_values': (211, 211, 211)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (211, 211, 211)
        }
    },
    {
        'name': 'light green',          # The rgb values shown here come from "hey google turn the lights to the color light green.'
        'google': {                     # Google results vary using 'light green' and 'the color light green'
            'is_rgb': True,
            'color_values': (144, 238, 144)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (144, 238, 144)
        }
    },
    {
        'name': 'light pink',           # The rgb values shown here come from "hey google turn the lights to the color light pink.'
        'google': {                     # Google results vary using 'light pink' and 'the color light pink'
            'is_rgb': True,
            'color_values': (255, 182, 193)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (255, 182, 193)
        }
    },
    {
        'name': 'light salmon',         # The rgb values shown here come from "hey google turn the lights to the color light salmon.'
        'google': {                     # Google results vary using 'light pink' and 'the color light salmon'
            'is_rgb': True,
            'color_values': (255, 160, 122)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (250, 160, 122)
        }
    },
    {
        'name': 'light sea green',      # The rgb values shown here come from "hey google turn the lights to the color light salmon.'
        'google': {                     # Google results vary using 'light sea green' and 'the color light sea green'
            'is_rgb': True,
            'color_values': (32, 178, 170)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (46, 196, 182)
        }
    },
    {
        'name': 'light sky blue',       # The rgb values shown here come from "hey google turn the lights to the color light sky blue.'
        'google': {                     # Google results vary using 'light sea sky blue' and 'the color light sea ky blue'
            'is_rgb': True,
            'color_values': (135, 206, 250)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (135, 206, 250)
        }
    },
    {
        'name': 'light slate gray',     # The rgb values shown here come from "hey google turn the lights to the color light slate gray.'
        'google': {                     # Google results vary using 'light sea green' and 'the color light slate gray'
            'is_rgb': True,
            'color_values': (119, 136, 153)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (119, 136, 153)
        }
    },
    {
        'name': 'light steel blue',     # The rgb values shown here come from "hey google turn the lights to the color light steel blue.'
        'google': {                     # Google results vary using 'light sea green' and 'the color light steel blue'
            'is_rgb': True,
            'color_values': (176, 196, 222)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (174, 194, 223)
        }
    },
    {
        'name': 'light turquoise',      # The rgb values shown here come from "hey google turn the lights to the color light turquoise.'
        'google': {                     # Google results vary using 'light turquoise' and 'the color light turquoise'
            'is_rgb': True,
            'color_values': (175, 228, 222)
        },
        # 'alexa': {
        #     'is_rgb': True,
        #     'color_values': (0, 0, 0)
        # }
    },
    {
        'name': 'light yellow',         # The rgb values shown here come from "hey google turn the lights to the color light yellow.'
        'google': {                     # Google results vary using 'light sea green' and 'the color light yellow'
            'is_rgb': True,
            'color_values': (255, 255, 224)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (255, 255, 224)  # -bVal could be 237
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
            'color_values': (166, 214, 40)
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
            'color_values': (50, 205, 50)
        }
    },
    {
        'name': 'linen',             # Google uses cct for this color
        'google': {
            'is_rgb': False,
            'color_values': 6100
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (250, 240, 230)
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
            'color_values': (255, 0, 255)
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
            'color_values': (178, 48, 96)
        }
    },
    {
        'name': 'medium aquamarine',
        'google': {
            'is_rgb': True,
            'color_values': (102, 221, 170)  # -gVal could be 205
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (97, 210, 180)
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
            'color_values': (0, 0, 205)
        }
    },
    {
        'name': 'medium orchid',
        # 'google': {
        #     'is_rgb': True,
        #     'color_values': (0, 0, 0)
        # },
        'alexa': {
            'is_rgb': True,
            'color_values': (186, 85, 211)
        }
    },
    {
        'name': 'medium purple',
        'google': {
            'is_rgb': True,
            'color_values': (147, 112, 219)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (147, 112, 219)
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
            'color_values': (60, 179, 113)
        }
    },
    {
        'name': 'medium slate blue',
        # 'google': {
        #     'is_rgb': True,
        #     'color_values': (0, 0, 0)
        # },
        'alexa': {
            'is_rgb': True,
            'color_values': (123, 104, 238)
        }
    },
    {
        'name': 'medium spring green',
        'google': {
            'is_rgb': True,
            'color_values': (0, 250, 154)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 250, 154)
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
            'color_values': (72, 209, 204)
        }
    },
    {
        'name': 'medium violet red',
        # 'google': {
        #     'is_rgb': True,
        #     'color_values': (0, 0, 0)
        # },
        'alexa': {
            'is_rgb': True,
            'color_values': (199, 21, 133)
        }
    },
    {
        'name': 'midnight blue',
        'google': {
            'is_rgb': True,
            'color_values': (25, 25, 112)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (25, 25, 112)
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
            'color_values': (245, 255, 250)
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
            'color_values': (255, 228, 225)
        }
    },
    # {
    #     'name': 'moccasin',
    #     # 'google': {
    #     #     'is_rgb': True,
    #     #     'color_values': (0, 0, 0)
    #     # },
    #     'alexa': {                   # Need to tell Alexa to set bulb 'to the color moccasin'
    #         'is_rgb': True,
    #         'color_values': (255, 228, 181)
    #     }
    # },
    {
        'name': 'navajo white',      # Google uses cct for this color
        'google': {
            'is_rgb': False,
            'color_values': 5000
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (255, 222, 173)
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
            'color_values': (0, 0, 128)
        }
    },
    # {
    #     'name': 'old lace',          # Google uses cct for this color
    #     # 'google': {
    #     #     'is_rgb': False,
    #     #     'color_values': 6100
    #     # },
    #     'alexa': {
    #         'is_rgb': True,
    #         'color_values': (253, 245, 230)
    #     }
    # },
    {
        'name': 'olive',
        'google': {
            'is_rgb': True,
            'color_values': (128, 128, 0)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (128, 128, 0)
        }
    },
    {
        'name': 'olive drab',
        'google': {                  # Need to tell Google, set the bulb 'to the color olive drab'
            'is_rgb': True,
            'color_values': (107, 142, 35)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (107, 142, 35)
        }
    },
    # {
    #     'name': 'olive green',
    #     'google': {
    #         'is_rgb': True,
    #         'color_values': (0, 0, 0)
    #     },
    #     'alexa': {
    #         'is_rgb': True,
    #         'color_values': (0, 0, 0)
    #     }
    # },
    {
        'name': 'orange',
        'google': {
            'is_rgb': True,
            'color_values': (255, 102, 0)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (255, 165, 0)
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
            'color_values': (255, 75, 0)
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
            'color_values': (218, 112, 214)
        }
    },
    {
        'name': 'pale goldenrod',
        # 'google': {
        #     'is_rgb': True,
        #     'color_values': (0, 0, 0)
        # },
        'alexa': {
            'is_rgb': True,
            'color_values': (238, 232, 170)
        }
    },
    {
        'name': 'pale green',
        # 'google': {
        #     'is_rgb': True,
        #     'color_values': (0, 0, 0)
        # },
        'alexa': {
            'is_rgb': True,
            'color_values': (152, 251, 152)
        }
    },
    {
        'name': 'pale turquoise',
        # 'google': {
        #     'is_rgb': True,
        #     'color_values': (0, 0, 0)
        # },
        'alexa': {
            'is_rgb': True,
            'color_values': (180, 255, 255)
        }
    },
    {
        'name': 'pale violet red',
        # 'google': {
        #     'is_rgb': True,
        #     'color_values': (0, 0, 0)
        # },
        'alexa': {
            'is_rgb': True,
            'color_values': (219, 112, 147)
        }
    },
    {
        'name': 'papaya whip',
        'google': {
            'is_rgb': True,
            'color_values': (255, 239, 213)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (255, 239, 213)
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
            'color_values': (255, 218, 185)
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
            'color_values': (205, 133, 63)
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
            'color_values': (250, 185, 204)  # (250, 185, 203)
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
            'color_values': (221, 160, 221)
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
            'color_values': (174, 224, 221)
        }
    },
    {
        'name': 'pumpkin',                    # Need to test for Alexa
        'google': {
            'is_rgb': True,
            'color_values': (255, 117, 24)
        },
        # 'alexa': {
        #     'is_rgb': True,
        #     'color_values': (0, 0, 0)
        # }
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
        'name': 'rebecca purple',
        # 'google': {
        #     'is_rgb': True,
        #     'color_values': (0, 0, 0)
        # },
        'alexa': {
            'is_rgb': True,
            'color_values': (102, 51, 153)
        }
    },
    {
        'name': 'red',
        'google': {
            'is_rgb': True,
            'color_values': (255, 0, 0)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (255, 0, 0)
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
            'color_values': (188, 143, 143)
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
            'color_values': (65, 105, 225)
        }
    },
    {
        'name': 'saddle brown',
        # 'google': {
        #     'is_rgb': True,
        #     'color_values': (0, 0, 0)
        # },
        'alexa': {
            'is_rgb': True,
            'color_values': (139, 69, 19)
        }
    },
    {
        'name': 'salmon',
        'google': {
            'is_rgb': True,
            'color_values': (250, 128, 114)
        },
        'alexa': {                            # Alexa uses the 'light salmon' rgb values for salmon
            'is_rgb': True,
            'color_values': (255, 160, 125)
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
            'color_values': (244, 164, 96)
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
            'color_values': (46, 139, 87)
        }
    },
    {
        'name': 'seashell',          # Google uses cct for this color
        'google': {
            'is_rgb': False,
            'color_values': 6100
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (255, 245, 238)
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
            'color_values': (160, 82, 45)
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
            'color_values': (192, 192, 192)
        }
    },
    # {
    #     'name': 'sky',
    #     'google': {
    #         'is_rgb': True,
    #         'color_values': (0, 0, 0)
    #     },
    #     'alexa': {
    #         'is_rgb': True,
    #         'color_values': (0, 0, 0)
    #     }
    # },
    {
        'name': 'sky blue',
        'google': {
            'is_rgb': True,
            'color_values': (135, 206, 235)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (135, 206, 235)
        }
    },
    # {
    #     'name': 'slate',
    #     'google': {
    #         'is_rgb': True,
    #         'color_values': (0, 0, 0)
    #     },
    #     'alexa': {
    #         'is_rgb': True,
    #         'color_values': (0, 0, 0)
    #     }
    # },
    {
        'name': 'slate blue',
        'google': {
            'is_rgb': True,
            'color_values': (106, 90, 205)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (106, 90, 205)
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
            'color_values': (112, 128, 144)
        }
    },
    {
        'name': 'smitten',
        'google': {
            'is_rgb': True,
            'color_values': (200, 65, 134)
        },
        # 'alexa': {
        #     'is_rgb': True,
        #     'color_values': (0, 0, 0)
        # }
    },
    {
        'name': 'snow',                # Google uses cct for this color
        'google': {
            'is_rgb': False,
            'color_values': 6500
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (255, 250, 250)
        }
    },
    {
        'name': 'soft white',                # Google uses cct for this color
        'google': {
            'is_rgb': False,
            'color_values': 3000
        },
        'alexa': {
            'is_rgb': False,
            'color_values': 2700
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
            'color_values': (0, 255, 127)
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
            'color_values': (70, 130, 180)
        }
    },
    # {
    #     'name': 'tan',
    #     # 'google': {
    #     #     'is_rgb': True,
    #     #     'color_values': (210, 180, 140)
    #     # },
    #     'alexa': {                           # Need to tell Alexa turn bulb 'to the color tan'
    #         'is_rgb': True,
    #         'color_values': (210, 180, 140)
    #     }
    # },
    {
        'name': 'teal',
        'google': {
            'is_rgb': True,
            'color_values': (0, 128, 128)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 128, 128)
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
            'color_values': (216, 191, 216)
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
            'color_values': (255, 99, 71)
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
            'color_values': (64, 224, 208)
        }
    },
    {
        'name': 'ultramarine',               # Need to test for Alexa
        'google': {
            'is_rgb': True,
            'color_values': (18, 10, 143)
        },
        # 'alexa': {
        #     'is_rgb': True,
        #     'color_values': (0, 0, 0)
        # }
    },
    {
        'name': 'vermillion',                # Need to test for Alexa
        'google': {
            'is_rgb': True,
            'color_values': (217, 56, 30)
        },
        # 'alexa': {
        #     'is_rgb': True,
        #     'color_values': (0, 0, 0)
        # }
    },
    {
        'name': 'violet',
        'google': {
            'is_rgb': True,
            'color_values': (127, 0, 255)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (238, 130, 238)
        }
    },
    {
        'name': 'warm',                # Google uses cct for this color
        # 'google': {
        #     'is_rgb': False,
        #     'color_values': ''
        # },
        'alexa': {
            'is_rgb': False,
            'color_values': 2200
        }
    },
    {
        'name': 'warm white',                # Google uses cct for this color
        'google': {
            'is_rgb': False,
            'color_values': 3000
        },
        'alexa': {
            'is_rgb': False,
            'color_values': 2200
        }
    },
    {
        'name': 'web gray',
        # 'google': {
        #     'is_rgb': True,
        #     'color_values': (0, 0, 0)
        # },
        'alexa': {
            'is_rgb': True,
            'color_values': (128, 128, 128)
        }
    },
    {
        'name': 'web green',
        # 'google': {
        #     'is_rgb': True,
        #     'color_values': (0, 0, 0)
        # },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 128, 0)
        }
    },
    {
        'name': 'web maroon',
        'google': {
            'is_rgb': True,
            'color_values': (128, 0, 0)
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (178, 48, 96)
        }
    },
    {
        'name': 'web purple',
        # 'google': {
        #     'is_rgb': True,
        #     'color_values': (128, 0, 128)
        # },
        'alexa': {
            'is_rgb': True,
            'color_values': (128, 0, 128)
        }
    },
    # {
    #     'name': 'wheat',
    #     'google': {
    #         'is_rgb': True,
    #         'color_values': (245, 222, 179)
    #     },
    #     'alexa': {
    #         'is_rgb': True,
    #         'color_values': (245, 222, 179)
    #     }
    # },
    {
        'name': 'white',                   # Google uses cct for this color
        'google': {
            'is_rgb': False,
            'color_values': 5000
        },
        'alexa': {
            'is_rgb': False,
            'color_values': 4000
        }
    },
    {
        'name': 'white smoke',             # Google uses cct for this color
        'google': {
            'is_rgb': False,
            'color_values': 7000
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (245, 245, 245)
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
            'color_values': (255, 255, 0)
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
            'color_values': (154, 205, 50)
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
            if not color.get(voice_agent).get('is_rgb'):
                color_list.append(color)
                print(color['name'], color[voice_agent]['color_values'])

    # for color in supported_colors_list:
    #     if color.get(voice_agent):
    #         if color.get(voice_agent).get('color_values'):
    #             print(color['name'], color[voice_agent]['color_values'])
        # print(color['name'], color[voice_agent]['color_values'])

    print('color_list length: ', len(color_list))

else:
    print('Successfully imported supported colors.py')
