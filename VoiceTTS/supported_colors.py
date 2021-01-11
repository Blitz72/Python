# Color values can be found here: https://en.wikipedia.org/wiki/List_of_colors_(compact)

supported_colors_list = [
    {
        'name': 'alice blue',
        'color_values': (240, 248, 255),
        'is_rgb': True,
        'va_support': ['Google', 'Alexa']
    },
    {
        'name': 'almond',             # Google uses color_values for this color
        'color_values': '',
        'is_rgb': False,
        'va_support': ['Google', 'Alexa']
    },
    {
        'name': 'antique white',      # Google uses color_values for this color
        'color_values': '',
        'is_rgb': False,
        'va_support': ['Google', 'Alexa']
    },
    {
        'name': 'aqua',
        'color_values': (0, 255, 255),
        'is_rgb': True,
        'va_support': ['Google', 'Alexa']
    },
    {
        'name': 'aquamarine',
        'color_values': (127, 255, 212),
        'is_rgb': True,
        'va_support': ['Google', 'Alexa']
    },
    {
        'name': 'azure',
        'color_values': (0, 127, 255),
        'is_rgb': True,
        'va_support': ['Google', 'Alexa']
    },
    {
        'name': 'beige',              # Google uses color_values for this color
        'color_values': '',
        'is_rgb': False,
        'va_support': ['Google', 'Alexa']
    },
    {
        'name': 'bisque',             # Google uses color_values for this color
        'color_values': '',
        'is_rgb': False,
        'va_support': ['Google', 'Alexa']
    },
    {
        'name': 'black',
        'color_values': (0, 0, 0),
        'is_rgb': True,
        'va_support': ['Google', 'Alexa']
    },
    {
        'name': 'blanched almond',    # Google uses cct for this color
        'color_values': '',
        'is_rgb': False,
        'va_support': ['Google', 'Alexa']
    },
    {
        'name': 'blue',
        'color_values': (0, 0, 255),
        'is_rgb': True,
        'va_support': ['Google', 'Alexa']
    },
    {
        'name': 'blue violet',
        'color_values': (138, 43, 226),
        'is_rgb': True,
        'va_support': ['Google', 'Alexa']
    },
    {
        'name': 'brown',
        'color_values': (150, 75, 0),
        'is_rgb': True,
        'va_support': ['Google', 'Alexa']
    },
#     {
#         'name': 'burlywood',         # Google uses cct for this color
#         'color_values': '',
#         'is_rgb': False,
#         'va_support': ['Alexa']
#     },
    {
        'name': 'cadet blue',
        'color_values': (95, 158, 160),
        'is_rgb': True,
        'va_support': ['Google', 'Alexa']
    },
    {
        'name': 'charteuse',
        'color_values': (223, 255, 0),
        'is_rgb': True,
        'va_support': ['Google', 'Alexa']
    },
    {
        'name': 'chocolate',
        'color_values': (123, 63, 0),
        'is_rgb': True,
        'va_support': ['Google', 'Alexa']
    },
    {
        'name': 'coral',
        'color_values': (255, 127, 80),
        'is_rgb': True,
        'va_support': ['Google', 'Alexa']
    },
    {
        'name': 'cornflower',
        'color_values': (100, 149, 237),
        'is_rgb': True,
        'va_support': ['Google', 'Alexa']
    },
    {
        'name': 'cornflower blue',           # Need to test for Alexa
        'color_values': (100, 149, 237),
        'is_rgb': True,
        'va_support': ['Google']
    },
#     {
#         'name': 'corns ilk',          
#         'color_values': '',
#         'is_rgb': False,
#         'va_support': ['Google', 'Alexa']
#     },
    {
        'name': 'crimson',
        'color_values': (220, 20, 60),
        'is_rgb': True,
        'va_support': ['Google', 'Alexa']
    },
    {
        'name': 'cyan',
        'color_values': (0, 255, 255),
        'is_rgb': True,
        'va_support': ['Google', 'Alexa']
    },
    {
        'name': 'dark blue',
        'color_values': (0, 0, 139),
        'is_rgb': True,
        'va_support': ['Google', 'Alexa']
    },
    {
        'name': 'dark cyan',
        'color_values': (0, 139, 139),
        'is_rgb': True,
        'va_support': ['Google', 'Alexa']
    },
    {
        'name': 'dark goldenrod',
        'color_values': (184, 134, 11),
        'is_rgb': True,
        'va_support': ['Google', 'Alexa']
    },
    {
        'name': 'dark gray',
        'color_values': (169, 169, 169),
        'is_rgb': True,
        'va_support': ['Google', 'Alexa']
    },
    {
        'name': 'dark green',
        'color_values': (1, 50, 32),
        'is_rgb': True,
        'va_support': ['Google', 'Alexa']
    },
    {
        'name': 'dark khaki',
        'color_values': (189, 183, 107),
        'is_rgb': True,
        'va_support': ['Google', 'Alexa']
    },
    {
        'name': 'dark magenta',
        'color_values': (139, 0, 139),
        'is_rgb': True,
        'va_support': ['Google', 'Alexa']
    },
#     {
#         'name': 'dark olive green',
#         'color_values': (0, 0, 0),
#         'is_rgb': True,
#         'va_support': ['Alexa']
#     },
    {
        'name': 'dark orange',
        'color_values': (85, 107, 47),
        'is_rgb': True,
        'va_support': ['Google', 'Alexa']
    },
    {
        'name': 'dark orchid',
        'color_values': (153, 50, 204),
        'is_rgb': True,
        'va_support': ['Google', 'Alexa']
    },
    {
        'name': 'dark red',
        'color_values': (139, 0, 0),
        'is_rgb': True,
        'va_support': ['Google', 'Alexa']
    },
    {
        'name': 'dark salmon',
        'color_values': (233, 150, 122),
        'is_rgb': True,
        'va_support': ['Google', 'Alexa']
    },
#     {
#         'name': 'dark sea green',
#         'color_values': (0, 0, 0),
#         'is_rgb': True,
#         'va_support': ['Alexa']
#     },
#     {
#         'name': 'dark slate blue',
#         'color_values': (0, 0, 0),
#         'is_rgb': True,
#         'va_support': ['Alexa']
#     },
    {
        'name': 'dark slate gray',
        'color_values': (47, 79, 79),
        'is_rgb': True,
        'va_support': ['Google', 'Alexa']
    },
    {
        'name': 'dark turquoise',
        'color_values': (0, 206, 209),
        'is_rgb': True,
        'va_support': ['Google', 'Alexa']
    },
    {
        'name': 'dark violet',
        'color_values': (148, 0, 211),
        'is_rgb': True,
        'va_support': ['Google', 'Alexa']
    },
    {
        'name': 'deep pink',
        'color_values': (255, 20, 147),
        'is_rgb': True,
        'va_support': ['Google', 'Alexa']
    },
    {
        'name': 'deep sky blue',
        'color_values': (0, 191, 255),
        'is_rgb': True,
        'va_support': ['Google', 'Alexa']
    },
    {
        'name': 'dim gray',
        'color_values': (105, 105, 105),
        'is_rgb': True,
        'va_support': ['Google', 'Alexa']
    },
    {
        'name': 'dodger blue',
        'color_values': (30, 144, 255),
        'is_rgb': True,
        'va_support': ['Google', 'Alexa']
    },
    {
        'name': 'firebrick',
        'color_values': (178, 34, 34),
        'is_rgb': True,
        'va_support': ['Google', 'Alexa']
    },
    {
        'name': 'floral white',      # Google uses cct for this color
        'color_values': '',
        'is_rgb': False,
        'va_support': ['Google', 'Alexa']
    },
    {
        'name': 'forest green',
        'color_values': (34, 139, 34),
        'is_rgb': True,
        'va_support': ['Google', 'Alexa']
    },
    {
        'name': 'fuchsia',
        'color_values': (193, 84, 193),
        'is_rgb': True,
        'va_support': ['Google', 'Alexa']
    },
    {
        'name': 'gainsboro',         # Google uses cct for this color
        'color_values': '',
        'is_rgb': False,
        'va_support': ['Google', 'Alexa']
    },
#     {
#         'name': 'garnet',
#         'color_values': (0, 0, 0),
#         'is_rgb': True,
#         'va_support': ['Alexa']
#     },
    {
        'name': 'ghost white',       # Google uses cct for this color
        'color_values': '',
        'is_rgb': False,
        'va_support': ['Google', 'Alexa']
    },
    {
        'name': 'gold',
        'color_values': (220, 220, 220),
        'is_rgb': True,
        'va_support': ['Google', 'Alexa']
    },
    {
        'name': 'goldenrod',
        'color_values': (218, 165, 32),
        'is_rgb': True,
        'va_support': ['Google', 'Alexa']
    },
    {
        'name': 'gray',
        'color_values': (128, 128, 128),
        'is_rgb': True,
        'va_support': ['Google', 'Alexa']
    },
    {
        'name': 'green',
        'color_values': (0, 255, 0),
        'is_rgb': True,
        'va_support': ['Google', 'Alexa']
    },
    {
        'name': 'green yellow',
        'color_values': (173, 255, 47),
        'is_rgb': True,
        'va_support': ['Google', 'Alexa']
    },
    {
        'name': 'honeydew',
        'color_values': (240, 255, 240),
        'is_rgb': True,
        'va_support': ['Google', 'Alexa']
    },
    {
        'name': 'hot pink',
        'color_values': (255, 105, 180),
        'is_rgb': True,
        'va_support': ['Google', 'Alexa']
    },
    {
        'name': 'indian red',
        'color_values': (205, 92, 92),
        'is_rgb': True,
        'va_support': ['Google', 'Alexa']
    },
    {
        'name': 'indigo',
        'color_values': (75, 0, 130),
        'is_rgb': True,
        'va_support': ['Google', 'Alexa']
    },
    {
        'name': 'ivory',               # Google uses cct for this color
        'color_values': '',
        'is_rgb': False,
        'va_support': ['Google', 'Alexa']
    },
    {
        'name': 'khaki',
        'color_values': (195, 176, 145),
        'is_rgb': True,
        'va_support': ['Google', 'Alexa']
    },
    {
        'name': 'lavender',
        'color_values': (181, 126, 220),
        'is_rgb': True,
        'va_support': ['Google', 'Alexa']
    },
    {
        'name': 'lavender blush',
        'color_values': (255, 240, 245),
        'is_rgb': True,
        'va_support': ['Google', 'Alexa']
    },
    {
        'name': 'lawn green',
        'color_values': (124, 252, 0),
        'is_rgb': True,
        'va_support': ['Google', 'Alexa']
    },
    {
        'name': 'lemon chiffon',
        'color_values': (255, 250, 205),
        'is_rgb': True,
        'va_support': ['Google', 'Alexa']
    },
    {
        'name': 'light blue',
        'color_values': (173, 216, 230),
        'is_rgb': True,
        'va_support': ['Google', 'Alexa']
    },
    {
        'name': 'ligth coral',          # The is_rgb values shown here come from "hey google turn the lights to the color light coral.'
        'color_values': (240, 128, 128),  # Google results vary using 'light coral' and 'the color light coral'
        'is_rgb': True,
        'va_support': ['Google', 'Alexa']
    },
    {
        'name': 'light cyan',           # The is_rgb values shown here come from "hey google turn the lights to the color light cyan.'
        'color_values': (224, 255, 255),  # Google results vary using 'light cyan' and 'the color light cyan'
        'is_rgb': True,
        'va_support': ['Google', 'Alexa']
    },
    {
        'name': 'light goldenrod',      # The is_rgb values shown here come from "hey google turn the lights to the color light goldenrod.'
        'color_values': (255, 236, 139),  # Google results vary using 'light goldenrod' and 'the color light goldenrod'
        'is_rgb': True,
        'va_support': ['Google', 'Alexa']
    },
    {
        'name': 'light gray',           # The is_rgb values shown here come from "hey google turn the lights to the color light gray.'
        'color_values': (211, 211, 211),  # Google results vary using 'light gray' and 'the color light gray'
        'is_rgb': True,
        'va_support': ['Google', 'Alexa']
    },
    {
        'name': 'light green',          # The is_rgb values shown here come from "hey google turn the lights to the color light green.'
        'color_values': (144, 238, 144),  # Google results vary using 'light green' and 'the color light green'
        'is_rgb': True,
        'va_support': ['Google', 'Alexa']
    },
    {
        'name': 'light pink',           # The is_rgb values shown here come from "hey google turn the lights to the color light pink.'
        'color_values': (255, 182, 193),  # Google results vary using 'light pink' and 'the color light pink'
        'is_rgb': True,
        'va_support': ['Google', 'Alexa']
    },
    {
        'name': 'light salmon',         # The is_rgb values shown here come from "hey google turn the lights to the color light salmon.'
        'color_values': (255, 160, 122),  # Google results vary using 'light pink' and 'the color light salmon'
        'is_rgb': True,
        'va_support': ['Google', 'Alexa']
    },
    {
        'name': 'light sea green',      # The is_rgb values shown here come from "hey google turn the lights to the color light salmon.'
        'color_values': (32, 178, 170),   # Google results vary using 'light sea green' and 'the color light sea green'
        'is_rgb': True,
        'va_support': ['Google', 'Alexa']
    },
    {
        'name': 'light sky blue',       # The is_rgb values shown here come from "hey google turn the lights to the color light sky blue.'
        'color_values': (135, 206, 250),  # Google results vary using 'light sea sky blue' and 'the color light sea ky blue'
        'is_rgb': True,
        'va_support': ['Google', 'Alexa']
    },
    {
        'name': 'light slate gray',     # The is_rgb values shown here come from "hey google turn the lights to the color light slate gray.'
        'color_values': (119, 136, 153),  # Google results vary using 'light sea green' and 'the color light slate gray'
        'is_rgb': True,
        'va_support': ['Google', 'Alexa']
    },
    {
        'name': 'light steel blue',     # The is_rgb values shown here come from "hey google turn the lights to the color light steel blue.'
        'color_values': (176, 196, 222),  # Google results vary using 'light sea green' and 'the color light steel blue'
        'is_rgb': True,
        'va_support': ['Google', 'Alexa']
    },
    {
        'name': 'light turquoise',      # The is_rgb values shown here come from "hey google turn the lights to the color light turquoise.'
        'color_values': (175, 228, 222),  # Google results vary using 'light turquoise' and 'the color light turquoise'
        'is_rgb': True,
        'va_support': ['Google']
    },
    {
        'name': 'light yellow',         # The is_rgb values shown here come from "hey google turn the lights to the color light yellow.'
        'color_values': (255, 255, 224),  # Google results vary using 'light sea green' and 'the color light yellow'
        'is_rgb': True,
        'va_support': ['Google', 'Alexa']
    },
    {
        'name': 'lime',
        'color_values': (191, 255, 0),
        'is_rgb': True,
        'va_support': ['Google', 'Alexa']
    },
    {
        'name': 'lime green',
        'color_values': (50, 205, 50),
        'is_rgb': True,
        'va_support': ['Google', 'Alexa']
    },
    {
        'name': 'linen',             # Google uses cct for this color
        'color_values': '',
        'is_rgb': False,
        'va_support': ['Google', 'Alexa']
    },
    {
        'name': 'magenta',
        'color_values': (255, 0, 255),
        'is_rgb': True,
        'va_support': ['Google', 'Alexa']
    },
    {
        'name': 'maroon',
        'color_values': (128, 0, 0),
        'is_rgb': True,
        'va_support': ['Google', 'Alexa']
    },
    {
        'name': 'medium aquamarine',
        'color_values': (102, 221, 170),
        'is_rgb': True,
        'va_support': ['Google', 'Alexa']
    },
    {
        'name': 'medium blue',
        'color_values': (0, 0, 205),
        'is_rgb': True,
        'va_support': ['Google', 'Alexa']
    },
#     {
#         'name': 'medium orchid',
#         'color_values': (0, 0, 0),
#         'is_rgb': True,
#         'va_support': ['Alexa']
#     },
    {
        'name': 'medium purple',
        'color_values': (147, 112, 219),
        'is_rgb': True,
        'va_support': ['Google', 'Alexa']
    },
    {
        'name': 'medium sea green',
        'color_values': (60, 179, 113),
        'is_rgb': True,
        'va_support': ['Google', 'Alexa']
    },
#     {
#         'name': 'medium slate blue',
#         'color_values': (0, 0, 0),
#         'is_rgb': True,
#         'va_support': ['Alexa']
#     },
    {
        'name': 'medium spring green',
        'color_values': (0, 250, 154),
        'is_rgb': True,
        'va_support': ['Google', 'Alexa']
    },
    {
        'name': 'medium turquoise',
        'color_values': (72, 209, 204),
        'is_rgb': True,
        'va_support': ['Google', 'Alexa']
    },
#     {
#         'name': 'medium violet red',
#         'color_values': (0, 0, 0),
#         'is_rgb': True,
#         'va_support': ['Alexa']
#     },
    {
        'name': 'midnight blue',
        'color_values': (25, 25, 112),
        'is_rgb': True,
        'va_support': ['Google', 'Alexa']
    },
    {
        'name': 'mint cream',
        'color_values': (245, 255, 250),
        'is_rgb': True,
        'va_support': ['Google', 'Alexa']
    },
    {
        'name': 'misty rose',
        'color_values': (255, 228, 225),
        'is_rgb': True,
        'va_support': ['Google', 'Alexa']
    },
#     {
#         'name': 'moccasin',
#         'color_values': (0, 0, 0),
#         'is_rgb': True,
#         'va_support': ['Alexa']
#     },
    {
        'name': 'navajo white',      # Google uses cct for this color
        'color_values': '',
        'is_rgb': False,
        'va_support': ['Google', 'Alexa']
    },
    {
        'name': 'navy blue',
        'color_values': (0, 0, 128),
        'is_rgb': True,
        'va_support': ['Google', 'Alexa']
    },
    {
        'name': 'old lace',          # Google uses cct for this color
        'color_values': '',
        'is_rgb': False,
        'va_support': ['Google', 'Alexa']
    },
    {
        'name': 'olive',
        'color_values': (128, 128, 0),
        'is_rgb': True,
        'va_support': ['Alexa']
    },
#     {
#         'name': 'olive drab',
#         'color_values': (0, 0, 0),
#         'is_rgb': True,
#         'va_support': ['Alexa']
#     },
    {
        'name': 'olive green',
        'color_values': (107, 142, 35),
        'is_rgb': True,
        'va_support': ['Alexa']
    },
    {
        'name': 'orange',
        'color_values': (255, 102, 0),
        'is_rgb': True,
        'va_support': ['Google', 'Alexa']
    },
    {
        'name': 'orange red',
        'color_values': (255, 75, 0),
        'is_rgb': True,
        'va_support': ['Google', 'Alexa']
    },
    {
        'name': 'orchid',
        'color_values': (218, 112, 214),
        'is_rgb': True,
        'va_support': ['Google', 'Alexa']
    },
#     {
#         'name': 'pale goldenrod',
#         'color_values': (0, 0, 0),
#         'is_rgb': True,
#         'va_support': ['Alexa']
#     },
#     {
#         'name': 'pale green',
#         'color_values': (0, 0, 0),
#         'is_rgb': True,
#         'va_support': ['Alexa']
#     },
#     {
#         'name': 'pale turquoise',
#         'color_values': (0, 0, 0),
#         'is_rgb': True,
#         'va_support': ['Alexa']
#     },
#     {
#         'name': 'pale violet red',
#         'color_values': (0, 0, 0),
#         'is_rgb': True,
#         'va_support': ['Alexa']
#     },
    {
        'name': 'papaya whip',
        'color_values': (255, 239, 213),
        'is_rgb': True,
        'va_support': ['Google', 'Alexa']
    },
    {
        'name': 'peach puff',
        'color_values': (255, 218, 185),
        'is_rgb': True,
        'va_support': ['Google', 'Alexa']
    },
    {
        'name': 'peru',
        'color_values': (205, 133, 63),
        'is_rgb': True,
        'va_support': ['Google', 'Alexa']
    },
    {
        'name': 'pink',
        'color_values': (255, 192, 203),
        'is_rgb': True,
        'va_support': ['Google', 'Alexa']
    },
    {
        'name': 'plum',
        'color_values': (142, 69, 133),
        'is_rgb': True,
        'va_support': ['Google', 'Alexa']
    },
    {
        'name': 'powder blue',
        'color_values': (176, 224, 230),
        'is_rgb': True,
        'va_support': ['Google', 'Alexa']
    },
    {
        'name': 'purple',
        'color_values': (128, 0, 128),
        'is_rgb': True,
        'va_support': ['Google', 'Alexa']
    },
    {
        'name': 'pumpkin',                    # Need to test for Alexa
        'color_values': (255, 117, 24),
        'is_rgb': True,
        'va_support': ['Google']
    },
#     {
#         'name': 'rebecca purple',
#         'color_values': (0, 0, 0),
#         'is_rgb': True,
#         'va_support': ['Alexa']
#     },
    {
        'name': 'red',
        'color_values': (255, 0, 0),
        'is_rgb': True,
        'va_support': ['Google', 'Alexa']
    },
    {
        'name': 'rosy brown',
        'color_values': (188, 143, 143),
        'is_rgb': True,
        'va_support': ['Google', 'Alexa']
    },
    {
        'name': 'royal blue',
        'color_values': (0, 35, 102),
        'is_rgb': True,
        'va_support': ['Google', 'Alexa']
    },
#     {
#         'name': 'saddle brown',
#         'color_values': (0, 0, 0),
#         'is_rgb': True,
#         'va_support': ['Alexa']
#     },
    {
        'name': 'salmon',
        'color_values': (250, 128, 114),
        'is_rgb': True,
        'va_support': ['Google', 'Alexa']
    },
    {
        'name': 'sandy brown',
        'color_values': (244, 164, 96),
        'is_rgb': True,
        'va_support': ['Google', 'Alexa']
    },
    {
        'name': 'sea green',
        'color_values': (46, 139, 87),
        'is_rgb': True,
        'va_support': ['Google', 'Alexa']
    },
    {
        'name': 'seashell',          # Google uses cct for this color
        'color_values': '',
        'is_rgb': False,
        'va_support': ['Google', 'Alexa']
    },
    {
        'name': 'sienna',
        'color_values': (136, 45, 23),
        'is_rgb': True,
        'va_support': ['Google', 'Alexa']
    },
    {
        'name': 'silver',
        'color_values': (192, 192, 192),
        'is_rgb': True,
        'va_support': ['Google', 'Alexa']
    },
#     {
#         'name': 'sky',
#         'color_values': (0, 0, 0),
#         'is_rgb': True,
#         'va_support': ['Alexa']
#     },
    {
        'name': 'sky blue',
        'color_values': (135, 206, 235),
        'is_rgb': True,
        'va_support': ['Google', 'Alexa']
    },
#     {
#         'name': 'slate',
#         'color_values': (0, 0, 0),
#         'is_rgb': True,
#         'va_support': ['Alexa']
#     },
    {
        'name': 'slate blue',
        'color_values': (106, 90, 205),
        'is_rgb': True,
        'va_support': ['Google', 'Alexa']
    },
    {
        'name': 'slate gray',
        'color_values': (112, 128, 144),
        'is_rgb': True,
        'va_support': ['Google', 'Alexa']
    },
    {
        'name': 'smitten',
        'color_values': (200, 65, 134),
        'is_rgb': True,
        'va_support': ['Google']
    },
    {
        'name': 'snow',                # Google uses cct for this color
        'color_values': '',
        'is_rgb': False,
        'va_support': ['Google', 'Alexa']
    },
    {
        'name': 'spring green',
        'color_values': (0, 255, 127),
        'is_rgb': True,
        'va_support': ['Google', 'Alexa']
    },
    {
        'name': 'steel blue',
        'color_values': (70, 130, 180),
        'is_rgb': True,
        'va_support': ['Google', 'Alexa']
    },
    {
        'name': 'tan',
        'color_values': (210, 180, 140),
        'is_rgb': True,
        'va_support': ['Google', 'Alexa']
    },
    {
        'name': 'teal',
        'color_values': (0, 128, 128),
        'is_rgb': True,
        'va_support': ['Google', 'Alexa']
    },
    {
        'name': 'thistle',
        'color_values': (216, 191, 216),
        'is_rgb': True,
        'va_support': ['Google', 'Alexa']
    },
    {
        'name': 'tomato',
        'color_values': (255, 99, 71),
        'is_rgb': True,
        'va_support': ['Google', 'Alexa']
    },
    {
        'name': 'turquoise',
        'color_values': (64, 224, 208),
        'is_rgb': True,
        'va_support': ['Google', 'Alexa']
    },
    {
        'name': 'ultramarine',               # Need to test for Alexa
        'color_values': (18, 10, 143),
        'is_rgb': True,
        'va_support': ['Google']
    },
    {
        'name': 'vermillion',                # Need to test for Alexa
        'color_values': (217, 56, 30),
        'is_rgb': True,
        'va_support': ['Google']
    },
    {
        'name': 'violet',
        'color_values': (127, 0, 255),
        'is_rgb': True,
        'va_support': ['Google', 'Alexa']
    },
#     {
#         'name': 'web gray',
#         'color_values': (0, 0, 0),
#         'is_rgb': True,
#         'va_support': ['Alexa']
#     },
#     {
#         'name': 'web green',
#         'color_values': (0, 0, 0),
#         'is_rgb': True,
#         'va_support': ['Alexa']
#     },
    {
        'name': 'web maroon',
        'color_values': (128, 0, 0),
        'is_rgb': True,
        'va_support': ['Alexa']
    },
    {
        'name': 'web purple',
        'color_values': (128, 0, 128),
        'is_rgb': True,
        'va_support': ['Alexa']
    },
    {
        'name': 'wheat',
        'color_values': (245, 222, 179),
        'is_rgb': True,
        'va_support': ['Google', 'Alexa']
    },
    {
        'name': 'white',                   # Google uses cct for this color
        'color_values': '',
        'is_rgb': False,
        'va_support': ['Google', 'Alexa']
    },
    {
        'name': 'white smoke',             # Google uses cct for this color
        'color_values': '',
        'is_rgb': False,
        'va_support': ['Google', 'Alexa']
    },
    {
        'name': 'yellow',
        'color_values': (255, 255, 0),
        'is_rgb': True,
        'va_support': ['Google', 'Alexa']
    },
    {
        'name': 'yellow green',
        'color_values': (154, 205, 50),
        'is_rgb': True,
        'va_support': ['Google', 'Alexa']
    }
]

for color in supported_colors_list:
    if 'Alexa' in color['va_support']:
        print(color['name'])