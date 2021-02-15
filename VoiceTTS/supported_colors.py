# Color values can be found here: https://en.wikipedia.org/wiki/List_of_colors_(compact)

# RGB color values given in tuples are (R, G, B)

supported_colors_list = [
    {
        'name': 'alice blue',
        'google': {
            'is_rgb': True,
            'color_values': (240, 248, 255),
            'tsl_brt_100': 17000,
            'tcs_color': (31, 25, 31),
            'm': 164.67,
            'b': 2497
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (240, 248, 255),
            'tsl_brt_100': 17000,
            'tcs_color': (31, 25, 31),
            'm': 164.67,
            'b': 2497
        }
    },
    # {
    #     'name': 'almond',
    #     'google': {
    #         'is_rgb': True,
    #         'color_values': (239, 222, 205),
    #         'tsl_brt_100': None,
    #         'tcs_color': None,
    #         'm': None,
    #         'b': None
    #     },
    #     # 'alexa': {
    #     #     'is_rgb': True,
    #     #     'color_values': (0, 0, 0),
    #     #     'tsl_brt_100': None,
    #     #     'tcs_color': None,
    #     #     'm': None,
    #     #     'b': None
    #     # }
    # },
    {
        'name': 'antique white',      # Google uses cct for this color
        'google': {
            'is_rgb': False,
            'color_values': 5500,
            'tsl_brt_100': 71500,
            'tcs_color': 4380,
            'm': None,
            'b': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (250, 235, 215),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        }
    },
    {
        'name': 'aqua',
        'google': {
            'is_rgb': True,
            'color_values': (0, 255, 255),
            'tsl_brt_100': 15000,
            'tcs_color': (0, 62, 87),
            'm': 144.95,
            'b': 2623
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 255, 255),
            'tsl_brt_100': 15000,
            'tcs_color': (0, 62, 87),
            'm': 144.95,
            'b': 2623
        }
    },
    {
        'name': 'aquamarine',
        'google': {
            'is_rgb': True,
            'color_values': (127, 255, 212),
            'tsl_brt_100': 16500,
            'tcs_color': (17, 39, 29),
            'm': 157.81,
            'b': 2640
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (127, 255, 212),
            'tsl_brt_100': 16500,
            'tcs_color': (17, 39, 29),
            'm': 157.81,
            'b': 2640
        }
    },
    {
        'name': 'azure',
        'google': {
            'is_rgb': True,
            'color_values': (0, 127, 255),
            'tsl_brt_100': 15300,
            'tcs_color': (0, 52, 128),
            'm': 155,
            'b': 1925
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (240, 255, 255),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        }
    },
    {
        'name': 'beige',              # Google uses cct for this color
        'google': {
            'is_rgb': False,
            'color_values': 5000,
            'tsl_brt_100': None,
            'tcs_color': 4150,
            'm': None,
            'b': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (245, 245, 220),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        }
    },
    {
        'name': 'bisque',             # Google uses cct for this color
        # 'google': {
        #     'is_rgb': False,
        #     'color_values': '',
        #     'tsl_brt_100': None,
        #     'tcs_color': None,
        #     'm': None,
        #     'b': None
        # },
        'alexa': {
            'is_rgb': True,
            'color_values': (255, 228, 196),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        }
    },
    # {
    #     'name': 'black',
    #     'google': {
    #         'is_rgb': True,
    #         'color_values': (0, 0, 0),
    #         'tsl_brt_100': None,
    #         'tcs_color': None,
    #         'm': None,
    #         'b': None
    #     },
    #     'alexa': {
    #         'is_rgb': True,
    #         'color_values': (0, 0, 0),
    #         'tsl_brt_100': None,
    #         'tcs_color': None,
    #         'm': None,
    #         'b': None
    #     }
    # },
    {
        'name': 'blanched almond',    # Google uses cct for this color
        # 'google': {
        #     'is_rgb': False,
        #     'color_values': '',
        #     'tsl_brt_100': None,
        #     'tcs_color': None,
        #     'm': None,
        #     'b': None
        # },
        'alexa': {
            'is_rgb': True,
            'color_values': (255, 235, 205),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        }
    },
    {
        'name': 'blue',
        'google': {
            'is_rgb': True,
            'color_values': (0, 0, 255),
            'tsl_brt_100': 15600,
            'tcs_color': (0, 34, 223),
            'm': 155,
            'b': 2000
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 0, 255),
            'tsl_brt_100': 15600,
            'tcs_color': (0, 34, 223),
            'm': 155,
            'b': 2000
        }
    },
    {
        'name': 'blue violet',
        'google': {
            'is_rgb': True,
            'color_values': (138, 43, 226),
            'tsl_brt_100': 17000,
            'tcs_color': (17, 16, 119),
            'm': 175,
            'b': 1450
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (138, 43, 226),
            'tsl_brt_100': 17000,
            'tcs_color': (17, 16, 119),
            'm': 175,
            'b': 1450
        }
    },
    {
        'name': 'brown',
        'google': {
            'is_rgb': True,
            'color_values': (150, 75, 0),
            'tsl_brt_100': 18000,
            'tcs_color': (111, 9, 5),
            'm': 190,
            'b': 1150
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (165, 42, 42),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        }
    },
    # {
    #     'name': 'burlywood',         # Google uses cct for this color
    #     'google': {
    #         'is_rgb': False,
    #         'color_values': '',
    #         'tsl_brt_100': None,
    #         'tcs_color': None,
    #         'm': None,
    #         'b': None
    #     },
    #     'alexa': {
    #         'is_rgb': False,
    #         'color_values': '',
    #         'tsl_brt_100': None,
    #         'tcs_color': None,
    #         'm': None,
    #         'b': None
    #     }
    # },
    {
        'name': 'candlelight',       # Google uses cct for this color
        'google': {
            'is_rgb': False,
            'color_values': 2000,
            'tsl_brt_100': None,
            'tcs_color': 2000,
            'm': None,
            'b': None
        },
        'alexa': {
            'is_rgb': False,
            'color_values': 2200,
            'tsl_brt_100': None,
            'tcs_color': 3340,
            'm': None,
            'b': None
        }
    },
    {
        'name': 'cadet blue',
        'google': {
            'is_rgb': True,
            'color_values': (95, 158, 160),
            'tsl_brt_100': 16500,
            'tcs_color': (18, 34, 37),
            'm': 170,
            'b': 1600
        },
        'alexa': {                           # Need to tell Alexa to set a Full Color bulb 'to the color cadet blue'
            'is_rgb': True,
            'color_values': (95, 158, 160),
            'tsl_brt_100': 16500,
            'tcs_color': (18, 34, 37),
            'm': 170,
            'b': 1600
        }
    },
    {
        'name': 'chartreuse',
        'google': {
            'is_rgb': True,
            'color_values': (223, 255, 0),
            'tsl_brt_100': 17000,
            'tcs_color': (53, 23, 7),
            'm': 175,
            'b': 1450
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (127, 255, 0),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        }
    },
    {
        'name': 'chocolate',
        'google': {
            'is_rgb': True,
            'color_values': (123, 63, 0),
            'tsl_brt_100': 18000,
            'tcs_color': (109, 9, 5),
            'm': 190,
            'b': 1150
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (210, 105, 30),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        }
    },
    {
        'name': 'cool',                # Google uses cct for this color
        # 'google': {
        #     'is_rgb': False,
        #     'color_values': '',
        #     'tsl_brt_100': None,
        #     'tcs_color': None,
        #     'm': None,
        #     'b': None
        # },
        'alexa': {
            'is_rgb': False,
            'color_values': 7000,
            'tcs_value': 5340,
            'tcs_color': 5340,
            'm': None,
            'b': None
        }
    },
    {
        'name': 'cool white',                # Google uses cct for this color
        'google': {
            'is_rgb': False,
            'color_values': 4000,
            'tcs_value': 3350,
            'tsl_brt_100': None,
            'tcs_color': 3350,
            'm': None,
            'b': None
        },
        'alexa': {
            'is_rgb': False,
            'color_values': 7000,
            'tcs_value': 5340,
            'tsl_brt_100': None,
            'tcs_color': 5340,
            'm': None,
            'b': None
        }
    },
    {
        'name': 'coral',
        'google': {
            'is_rgb': True,
            'color_values': (255, 127, 80),
            'tsl_brt_100': 18000,
            'tcs_color': (120, 7, 7),
            'm': 190,
            'b': 1000
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (255, 127, 80),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        }
    },
    {
        'name': 'cornflower',
        'google': {
            'is_rgb': True,
            'color_values': (100, 149, 237),
            'tsl_brt_100': 16500,
            'tcs_color': (18, 31, 79),
            'm': 165,
            'b': 1600
        },
        # 'alexa': {
        #     'is_rgb': True,
        #     'color_values': (0, 0, 0),
        #     'tsl_brt_100': None,
        #     'tcs_color': None,
        #     'm': None,
        #     'b': None
        # }
    },
    {
        'name': 'cornflower blue',           # Need to test for Alexa
        'google': {
            'is_rgb': True,
            'color_values': (100, 149, 237),
            'tsl_brt_100': 16500,
            'tcs_color': (18, 31, 79),
            'm': 165,
            'b': 1600
        },
        # 'alexa': {
        #     'is_rgb': True,
        #     'color_values': (0, 0, 0),
        #     'tsl_brt_100': None,
        #     'tcs_color': None,
        #     'm': None,
        #     'b': None
        # }
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
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        }
    },
    {
        'name': 'crimson',
        'google': {
            'is_rgb': True,
            'color_values': (220, 20, 60),
            'tsl_brt_100': 18500,
            'tcs_color': (194, 1, 6),
            'm': 195,
            'b': 900
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (220, 20, 60),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        }
    },
    {
        'name': 'cyan',
        'google': {
            'is_rgb': True,
            'color_values': (0, 255, 255),
            'tsl_brt_100': 15000,
            'tcs_color': (0, 62, 87),
            'm': 144.95,
            'b': 2623
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 255, 255),
            'tsl_brt_100': 15000,
            'tcs_color': (0, 62, 87),
            'm': 144.95,
            'b': 2623
        }
    },
    {
        'name': 'dark blue',
        'google': {
            'is_rgb': True,
            'color_values': (0, 0, 139),
            'tsl_brt_100': 15600,
            'tcs_color': (0, 34, 223),
            'm': 155,
            'b': 2000
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 0, 139),
            'tsl_brt_100': 15600,
            'tcs_color': (0, 34, 223),
            'm': 155,
            'b': 2000
        }
    },
    {
        'name': 'dark cyan',
        'google': {
            'is_rgb': True,
            'color_values': (0, 139, 139),
            'tsl_brt_100': 15000,
            'tcs_color': (0, 62, 87),
            'm': 144.95,
            'b': 2623
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 139, 139),
            'tsl_brt_100': 15000,
            'tcs_color': (0, 62, 87),
            'm': 144.95,
            'b': 2623
        }
    },
    {
        'name': 'dark goldenrod',
        'google': {
            'is_rgb': True,
            'color_values': (184, 134, 11),
            'tsl_brt_100': 17500,
            'tcs_color': (83, 14, 6),
            'm': 185,
            'b': 1250
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (184, 134, 11),
            'tsl_brt_100': 17500,
            'tcs_color': (83, 14, 6),
            'm': 185,
            'b': 1250
        }
    },
    {
        'name': 'dark gray',
        'google': {
            'is_rgb': True,
            'color_values': (169, 169, 169),
            'tsl_brt_100': 17000,
            'tcs_color': (34, 24, 29),
            'm': 175,
            'b': 1450
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (169, 169, 169),
            'tsl_brt_100': 17000,
            'tcs_color': (34, 24, 29),
            'm': 175,
            'b': 1450
        }
    },
    {
        'name': 'dark green',
        'google': {
            'is_rgb': True,
            'color_values': (1, 50, 32),
            'tsl_brt_100': 16000,
            'tcs_color': (12, 47, 27),
            'm': 160,
            'b': 1750
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 100, 0),
            'tsl_brt_100': 14000,
            'tcs_color': (0, 93, 10),
            'm': 135,
            'b': 2250
        }
    },
    {
        'name': 'dark khaki',
        'google': {
            'is_rgb': True,
            'color_values': (189, 183, 107),
            'tsl_brt_100': 17000,
            'tcs_color': (48, 22, 14),
            'm': 180,
            'b': 1350
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (189, 183, 107),
            'tsl_brt_100': 17000,
            'tcs_color': (48, 22, 14),
            'm': 180,
            'b': 1350
        }
    },
    {
        'name': 'dark magenta',
        'google': {
            'is_rgb': True,
            'color_values': (139, 0, 139),
            'tsl_brt_100': 17500,
            'tcs_color': (61, 8, 60),
            'm': 185,
            'b': 1200
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (139, 0, 139),
            'tsl_brt_100': 17500,
            'tcs_color': (61, 8, 60),
            'm': 185,
            'b': 1200
        }
    },
    {
        'name': 'dark olive green',
        # 'google': {
        #     'is_rgb': True,
        #     'color_values': (0, 0, 0),
        #     'tsl_brt_100': None,
        #     'tcs_color': None,
        #     'm': None,
        #     'b': None
        # },
        'alexa': {
            'is_rgb': True,
            'color_values': (86, 103, 51),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        }
    },
    {
        'name': 'dark orange',
        'google': {
            'is_rgb': True,
            'color_values': (255, 140, 0),
            'tsl_brt_100': 17500,
            'tcs_color': (183, 10, 5),
            'm': 185,
            'b': 1150
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (255, 140, 0),
            'tsl_brt_100': 17500,
            'tcs_color': (183, 10, 5),
            'm': 185,
            'b': 1150
        }
    },
    {
        'name': 'dark orchid',
        'google': {
            'is_rgb': True,
            'color_values': (153, 50, 204),
            'tsl_brt_100': 17000,
            'tcs_color': (30, 13, 85),
            'm': 175,
            'b': 1400
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (153, 50, 204),
            'tsl_brt_100': 17000,
            'tcs_color': (30, 13, 85),
            'm': 175,
            'b': 1400
        }
    },
    {
        'name': 'dark red',
        'google': {
            'is_rgb': True,
            'color_values': (139, 0, 0),
            'tsl_brt_100': 18500,
            'tcs_color': (245, 0, 3),
            'm': 200,
            'b': 800
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (139, 0, 0),
            'tsl_brt_100': 18500,
            'tcs_color': (245, 0, 3),
            'm': 200,
            'b': 800
        }
    },
    {
        'name': 'dark salmon',
        'google': {
            'is_rgb': True,
            'color_values': (233, 150, 122),
            'tsl_brt_100': 17500,
            'tcs_color': (80, 11, 14),
            'm': 185,
            'b': 1200
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (233, 150, 122),
            'tsl_brt_100': 17500,
            'tcs_color': (80, 11, 14),
            'm': 185,
            'b': 1200
        }
    },
    {
        'name': 'dark sea green',
        # 'google': {
        #     'is_rgb': True,
        #     'color_values': (0, 0, 0),
        #     'tsl_brt_100': None,
        #     'tcs_color': None,
        #     'm': None,
        #     'b': None
        # },
        'alexa': {
            'is_rgb': True,
            'color_values': (143, 188, 143),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        }
    },
    {
        'name': 'dark slate blue',
        # 'google': {
        #     'is_rgb': True,
        #     'color_values': (0, 0, 0),
        #     'tsl_brt_100': None,
        #     'tcs_color': None,
        #     'm': None,
        #     'b': None
        # },
        'alexa': {
            'is_rgb': True,
            'color_values': (72, 61, 139),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        }
    },
    {
        'name': 'dark slate gray',
        'google': {
            'is_rgb': True,
            'color_values': (47, 79, 79),
            'tsl_brt_100': 16500,
            'tcs_color': (19, 33, 36),
            'm': 165,
            'b': 1600
        },
        'alexa': {                            # Need to tell Alexa to set a Full Color bulb 'to the color dark slate gray'
            'is_rgb': True,
            'color_values': (47, 79, 79),
            'tsl_brt_100': 16500,
            'tcs_color': (19, 33, 36),
            'm': 165,
            'b': 1600
        }
    },
    {
        'name': 'dark turquoise',
        'google': {
            'is_rgb': True,
            'color_values': (0, 206, 209),
            'tsl_brt_100': 15000,
            'tcs_color': (0, 62, 80),
            'm': 150,
            'b': 1950
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 210, 210),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        }
    },
    {
        'name': 'dark violet',
        'google': {
            'is_rgb': True,
            'color_values': (148, 0, 211),
            'tsl_brt_100': 16500,
            'tcs_color': (9, 21, 144),
            'm': 170,
            'b': 1600
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (148, 0, 211),
            'tsl_brt_100': 16500,
            'tcs_color': (9, 21, 144),
            'm': 170,
            'b': 1600
        }
    },
    {
        'name': 'daylight',                # Google uses cct for this color
        'google': {
            'is_rgb': False,
            'color_values': 5000,
            'tsl_brt_100': None,
            'tcs_color': 4150,
            'm': None,
            'b': None
        },
        'alexa': {
            'is_rgb': False,
            'color_values': 5500,
            'tsl_brt_100': None,
            'tcs_color': 4360,
            'm': None,
            'b': None
        }
    },
    {
        'name': 'deep pink',
        'google': {
            'is_rgb': True,
            'color_values': (255, 20, 147),
            'tsl_brt_100': 18500,
            'tcs_color': (138, 3, 18),
            'm': 195,
            'b': 1000
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (255, 20, 147),
            'tsl_brt_100': 18500,
            'tcs_color': (138, 3, 18),
            'm': 195,
            'b': 1000
        }
    },
    {
        'name': 'deep sky blue',
        'google': {
            'is_rgb': True,
            'color_values': (0, 191, 255),
            'tsl_brt_100': 15000,
            'tcs_color': (0, 57, 105),
            'm': 155,
            'b': 1900
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 191, 255),
            'tsl_brt_100': 15000,
            'tcs_color': (0, 57, 105),
            'm': 155,
            'b': 1900
        }
    },
    {
        'name': 'dim gray',
        'google': {
            'is_rgb': True,
            'color_values': (105, 105, 105),
            'tsl_brt_100': 17000,
            'tcs_color': (34, 24, 29),
            'm': 175,
            'b': 1450
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (105, 105, 105),
            'tsl_brt_100': 17000,
            'tcs_color': (34, 24, 29),
            'm': 175,
            'b': 1450
        }
    },
    {
        'name': 'dodger blue',
        'google': {
            'is_rgb': True,
            'color_values': (30, 144, 255),
            'tsl_brt_100': 16000,
            'tcs_color': (5, 34, 103),
            'm': 165,
            'b': 1650
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (30, 144, 255),
            'tsl_brt_100': 16000,
            'tcs_color': (5, 34, 103),
            'm': 165,
            'b': 1650
        }
    },
    {
        'name': 'firebrick',
        'google': {
            'is_rgb': True,
            'color_values': (178, 34, 34),
            'tsl_brt_100': 18500,
            'tcs_color': (186, 2, 5),
            'm': 195,
            'b': 900
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (178, 34, 34),
            'tsl_brt_100': 18500,
            'tcs_color': (186, 2, 5),
            'm': 195,
            'b': 900
        }
    },
    {
        'name': 'floral white',      # Google uses cct for this color
        'google': {
            'is_rgb': False,
            'color_values': 6100,
            'tsl_brt_100': None,
            'tcs_color': 4640,
            'm': None,
            'b': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (255, 250, 240),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        }
    },
    {
        'name': 'forest green',
        'google': {
            'is_rgb': True,
            'color_values': (34, 139, 34),
            'tsl_brt_100': 16000,
            'tcs_color': (17, 46, 10),
            'm': 160,
            'b': 1750
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (34, 139, 34),
            'tsl_brt_100': 16000,
            'tcs_color': (17, 46, 10),
            'm': 160,
            'b': 1750
        }
    },
    {
        'name': 'fuchsia',
        'google': {
            'is_rgb': True,
            'color_values': (193, 84, 193),
            'tsl_brt_100': 17500,
            'tcs_color': (50, 11, 49),
            'm': 180,
            'b': 1300
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (255, 0, 255),
            'tsl_brt_100': 17500,
            'tcs_color': (61, 8, 60),
            'm': 185,
            'b': 1200
        }
    },
    {
        'name': 'gainsboro',         # Google uses cct for this color
        'google': {
            'is_rgb': True,
            'color_values': (220, 220, 220),
            'tsl_brt_100': 17000,
            'tcs_color': (34, 24, 29),
            'm': 175,
            'b': 1450
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (220, 220, 220),
            'tsl_brt_100': 17000,
            'tcs_color': (34, 24, 29),
            'm': 175,
            'b': 1450
        }
    },
    # {
    #     'name': 'garnet',
    #     'google': {
    #         'is_rgb': True,
    #         'color_values': (0, 0, 0),
    #         'tsl_brt_100': None,
    #         'tcs_color': None,
    #         'm': None,
    #         'b': None
    #     },
    #     'alexa': {
    #         'is_rgb': True,
    #         'color_values': (0, 0, 0),
    #         'tsl_brt_100': None,
    #         'tcs_color': None,
    #         'm': None,
    #         'b': None
    #     }
    # },
    {
        'name': 'ghost white',       # Google uses cct for this color
        'google': {
            'is_rgb': False,
            'color_values': 7000,
            'tsl_brt_100': None,
            'tcs_color': 5335,
            'm': None,
            'b': None
        },
        'alexa': {                   # Need to tell Alexa to set a Full Color bulb 'to the color dark slate gray'
            'is_rgb': True,
            'color_values': (248, 248, 255),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        }
    },
    {
        'name': 'gold',
        'google': {
            'is_rgb': True,
            'color_values': (165, 124, 0),
            'tsl_brt_100': 17500,
            'tcs_color': (73, 17, 6),
            'm': 185,
            'b': 1300
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (255, 215, 0),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        }
    },
    {
        'name': 'goldenrod',
        'google': {
            'is_rgb': True,
            'color_values': (218, 165, 32),
            'tsl_brt_100': 17500,
            'tcs_color': (78, 15, 6),
            'm': 185,
            'b': 1250
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (218, 165, 32),
            'tsl_brt_100': 17500,
            'tcs_color': (78, 15, 6),
            'm': 185,
            'b': 1250
        }
    },
    {
        'name': 'gray',
        'google': {
            'is_rgb': True,
            'color_values': (128, 128, 128),
            'tsl_brt_100': 17000,
            'tcs_color': (34, 24, 29),
            'm': 175,
            'b': 1450
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (128, 128, 128),
            'tsl_brt_100': 17000,
            'tcs_color': (34, 24, 29),
            'm': 175,
            'b': 1450
        }
    },
    {
        'name': 'green',
        'google': {
            'is_rgb': True,
            'color_values': (0, 255, 0),
            'tsl_brt_100': 14000,
            'tcs_color': (0, 93, 10),
            'm': 135,
            'b': 2250
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 255, 0),
            'tsl_brt_100': 14000,
            'tcs_color': (0, 93, 10),
            'm': 135,
            'b': 2250
        }
    },
    {
        'name': 'green yellow',
        'google': {
            'is_rgb': True,
            'color_values': (173, 255, 47),
            'tsl_brt_100': 16500,
            'tcs_color': (31, 35, 8),
            'm': 170,
            'b': 1600
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (173, 255, 47),
            'tsl_brt_100': 16500,
            'tcs_color': (31, 35, 8),
            'm': 170,
            'b': 1600
        }
    },
    {
        'name': 'honeydew',
        'google': {
            'is_rgb': True,
            'color_values': (240, 255, 240),
            'tsl_brt_100': 17000,
            'tcs_color': (32, 27, 28),
            'm': 175,
            'b': 1500
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (240, 255, 240),
            'tsl_brt_100': 17000,
            'tcs_color': (32, 27, 28),
            'm': 175,
            'b': 1500
        }
    },
    {
        'name': 'hot pink',
        'google': {
            'is_rgb': True,
            'color_values': (255, 105, 180),
            'tsl_brt_100': 18000,
            'tcs_color': (87, 7, 24),
            'm': 190,
            'b': 1140
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (255, 105, 180),
            'tsl_brt_100': 18000,
            'tcs_color': (87, 7, 24),
            'm': 190,
            'b': 1140
        }
    },
    {
        'name': 'incandescent',                # Google uses cct for this color
        'google': {
            'is_rgb': False,
            'color_values': 2700,
            'tsl_brt_100': None,
            'tcs_color': 2630,
            'm': None,
            'b': None
        },
        'alexa': {
            'is_rgb': False,
            'color_values': 2700,
            'tsl_brt_100': None,
            'tcs_color': 2630,
            'm': None,
            'b': None
        }
    },
    {
        'name': 'indian red',
        'google': {
            'is_rgb': True,
            'color_values': (205, 92, 92),
            'tsl_brt_100': 18000,
            'tcs_color': (114, 6, 11),
            'm': 190,
            'b': 1000
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (200, 100, 100),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        }
    },
    {
        'name': 'indigo',
        'google': {
            'is_rgb': True,
            'color_values': (75, 0, 130),
            'tsl_brt_100': 16500,
            'tcs_color': (16, 17, 122),
            'm': 175,
            'b': 1450
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (75, 0, 130),
            'tsl_brt_100': 16500,
            'tcs_color': (16, 17, 122),
            'm': 175,
            'b': 1450
        }
    },
    {
        'name': 'ivory',               # Google uses cct for this color
        'google': {
            'is_rgb': False,
            'color_values': 6100,
            'tsl_brt_100': None,
            'tcs_color': 4640,
            'm': None,
            'b': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (255, 255, 240),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        }
    },
    {
        'name': 'khaki',
        'google': {
            'is_rgb': True,
            'color_values': (195, 176, 145),
            'tsl_brt_100': 17000,
            'tcs_color': (46, 21, 21),
            'm': 175,
            'b': 1400
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (240, 230, 140),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        }
    },
    {
        'name': 'lavender',
        'google': {
            'is_rgb': True,
            'color_values': (181, 126, 220),
            'tsl_brt_100': 17000,
            'tcs_color': (31, 17, 55),
            'm': 175,
            'b': 1400
        },
        'alexa': {                          # These are custom values to match what Alexa chose for lavender
            'is_rgb': True,
            'color_values':(150, 127, 255),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        }
    },
    {
        'name': 'lavender blush',
        'google': {
            'is_rgb': True,
            'color_values': (255, 240, 245),
            'tsl_brt_100': 17000,
            'tcs_color': (26, 24, 46),
            'm': 175,
            'b': 1500
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (255, 240, 245),
            'tsl_brt_100': 17000,
            'tcs_color': (26, 24, 46),
            'm': 175,
            'b': 1500
        }
    },
    {
        'name': 'lawn green',
        'google': {
            'is_rgb': True,
            'color_values': (124, 252, 0),
            'tsl_brt_100': 16000,
            'tcs_color': (28, 37, 8),
            'm': 165,
            'b': 1650
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (124, 252, 0),
            'tsl_brt_100': 16000,
            'tcs_color': (28, 37, 8),
            'm': 165,
            'b': 1650
        }
    },
    {
        'name': 'lemon chiffon',
        'google': {
            'is_rgb': True,
            'color_values': (255, 250, 205),
            'tsl_brt_100': 17000,
            'tcs_color': (29, 23, 39),
            'm': 175,
            'b': 1400
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (255, 250, 205),
            'tsl_brt_100': 17000,
            'tcs_color': (29, 23, 39),
            'm': 175,
            'b': 1400
        }
    },
    {
        'name': 'light blue',
        'google': {
            'is_rgb': True,
            'color_values': (173, 216, 230),
            'tsl_brt_100': 16500,
            'tcs_color': (23, 29, 37),
            'm': 170,
            'b': 1550
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (191, 239, 255),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        }
    },
    {
        'name': 'light coral',          # The rgb values shown here come from "hey google turn the lights to the color light coral.'
        'google': {                     # Google results vary using 'light coral' and 'the color light coral'
            'is_rgb': True,
            'color_values': (240, 128, 128),
            'tsl_brt_100': 18000,
            'tcs_color': (93, 9, 15),
            'm': 185,
            'b': 1200
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (240, 128, 128),
            'tsl_brt_100': 18000,
            'tcs_color': (93, 9, 15),
            'm': 185,
            'b': 1200
        }
    },
    {
        'name': 'light cyan',           # The rgb values shown here come from "hey google turn the lights to the color light cyan.'
        'google': {                     # Google results vary using 'light cyan' and 'the color light cyan'
            'is_rgb': True,
            'color_values': (224, 255, 255),
            'tsl_brt_100': 15000,
            'tcs_color': (0, 62, 88),
            'm': 150,
            'b': 1950
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (224, 255, 255),
            'tsl_brt_100': 15000,
            'tcs_color': (0, 62, 88),
            'm': 150,
            'b': 1950
        }
    },
    {
        'name': 'light goldenrod',      # The rgb values shown here come from "hey google turn the lights to the color light goldenrod.'
        'google': {                     # Google results vary using 'light goldenrod' and 'the color light goldenrod'
            'is_rgb': True,
            'color_values': (255, 236, 139),
            'tsl_brt_100': 17000,
            'tcs_color': (44, 23, 18),
            'm': 175,
            'b': 1450
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (250, 250, 210),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        }
    },
    {
        'name': 'light gray',           # The rgb values shown here come from "hey google turn the lights to the color light gray.'
        'google': {                     # Google results vary using 'light gray' and 'the color light gray'
            'is_rgb': True,
            'color_values': (211, 211, 211),
            'tsl_brt_100': 17000,
            'tcs_color': (34, 24, 29),
            'm': 175,
            'b': 1450
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (211, 211, 211),
            'tsl_brt_100': 17000,
            'tcs_color': (34, 24, 29),
            'm': 175,
            'b': 1450
        }
    },
    {
        'name': 'light green',          # The rgb values shown here come from "hey google turn the lights to the color light green.'
        'google': {                     # Google results vary using 'light green' and 'the color light green'
            'is_rgb': True,
            'color_values': (144, 238, 144),
            'tsl_brt_100': 16500,
            'tcs_color': (23, 37, 18),
            'm': 165,
            'b': 1650
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (144, 238, 144),
            'tsl_brt_100': 16500,
            'tcs_color': (23, 37, 18),
            'm': 165,
            'b': 1650
        }
    },
    {
        'name': 'light pink',           # The rgb values shown here come from "hey google turn the lights to the color light pink.'
        'google': {                     # Google results vary using 'light pink' and 'the color light pink'
            'is_rgb': True,
            'color_values': (255, 182, 193),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (255, 182, 193),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        }
    },
    {
        'name': 'light salmon',         # The rgb values shown here come from "hey google turn the lights to the color light salmon.'
        'google': {                     # Google results vary using 'light pink' and 'the color light salmon'
            'is_rgb': True,
            'color_values': (255, 160, 122),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (250, 160, 122),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        }
    },
    {
        'name': 'light sea green',      # The rgb values shown here come from "hey google turn the lights to the color light salmon.'
        'google': {                     # Google results vary using 'light sea green' and 'the color light sea green'
            'is_rgb': True,
            'color_values': (32, 178, 170),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (46, 196, 182),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        }
    },
    {
        'name': 'light sky blue',       # The rgb values shown here come from "hey google turn the lights to the color light sky blue.'
        'google': {                     # Google results vary using 'light sea sky blue' and 'the color light sea ky blue'
            'is_rgb': True,
            'color_values': (135, 206, 250),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (135, 206, 250),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        }
    },
    {
        'name': 'light slate gray',     # The rgb values shown here come from "hey google turn the lights to the color light slate gray.'
        'google': {                     # Google results vary using 'light sea green' and 'the color light slate gray'
            'is_rgb': True,
            'color_values': (119, 136, 153),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (119, 136, 153),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        }
    },
    {
        'name': 'light steel blue',     # The rgb values shown here come from "hey google turn the lights to the color light steel blue.'
        'google': {                     # Google results vary using 'light sea green' and 'the color light steel blue'
            'is_rgb': True,
            'color_values': (176, 196, 222),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (174, 194, 223),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        }
    },
    {
        'name': 'light turquoise',      # The rgb values shown here come from "hey google turn the lights to the color light turquoise.'
        'google': {                     # Google results vary using 'light turquoise' and 'the color light turquoise'
            'is_rgb': True,
            'color_values': (175, 228, 222),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 0, 0),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        }
    },
    {
        'name': 'light yellow',         # The rgb values shown here come from "hey google turn the lights to the color light yellow.'
        'google': {                     # Google results vary using 'light sea green' and 'the color light yellow'
            'is_rgb': True,
            'color_values': (255, 255, 224),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (255, 255, 224),  # -bVal could be 237
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        }
    },
    {
        'name': 'lime',
        'google': {
            'is_rgb': True,
            'color_values': (191, 255, 0),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (166, 214, 40),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        }
    },
    {
        'name': 'lime green',
        'google': {
            'is_rgb': True,
            'color_values': (50, 205, 50),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (50, 205, 50),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        }
    },
    {
        'name': 'linen',             # Google uses cct for this color
        'google': {
            'is_rgb': False,
            'color_values': 6100,
            'tsl_brt_100': None,
            'tcs_color': 4640,
            'm': None,
            'b': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (250, 240, 230),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        }
    },
    {
        'name': 'magenta',
        'google': {
            'is_rgb': True,
            'color_values': (255, 0, 255),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (255, 0, 255),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        }
    },
    {
        'name': 'maroon',
        'google': {
            'is_rgb': True,
            'color_values': (128, 0, 0),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (178, 48, 96),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        }
    },
    {
        'name': 'medium aquamarine',
        'google': {
            'is_rgb': True,
            'color_values': (102, 221, 170),  # -gVal could be 205
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (97, 210, 180),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        }
    },
    {
        'name': 'medium blue',
        'google': {
            'is_rgb': True,
            'color_values': (0, 0, 205),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 0, 205),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        }
    },
    {
        'name': 'medium orchid',
        # 'google': {
        #     'is_rgb': True,
        #     'color_values': (0, 0, 0),
        #     'tsl_brt_100': None,
        #     'tcs_color': None,
        #     'm': None,
        #     'b': None
        # },
        'alexa': {
            'is_rgb': True,
            'color_values': (186, 85, 211),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        }
    },
    {
        'name': 'medium purple',
        'google': {
            'is_rgb': True,
            'color_values': (147, 112, 219),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (147, 112, 219),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        }
    },
    {
        'name': 'medium sea green',
        'google': {
            'is_rgb': True,
            'color_values': (60, 179, 113),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (60, 179, 113),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        }
    },
    {
        'name': 'medium slate blue',
        # 'google': {
        #     'is_rgb': True,
        #     'color_values': (0, 0, 0),
        #     'tsl_brt_100': None,
        #     'tcs_color': None,
        #     'm': None,
        #     'b': None
        # },
        'alexa': {
            'is_rgb': True,
            'color_values': (123, 104, 238),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        }
    },
    {
        'name': 'medium spring green',
        'google': {
            'is_rgb': True,
            'color_values': (0, 250, 154),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 250, 154),
            'tsl_brt': None,
            'tcs_color': None,
            'm': None,
            'b': None
        }
    },
    {
        'name': 'medium turquoise',
        'google': {
            'is_rgb': True,
            'color_values': (72, 209, 204),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (72, 209, 204),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        }
    },
    {
        'name': 'medium violet red',
        # 'google': {
        #     'is_rgb': True,
        #     'color_values': (0, 0, 0),
        #     'tsl_brt_100': None,
        #     'tcs_color': None,
        #     'm': None,
        #     'b': None
        # },
        'alexa': {
            'is_rgb': True,
            'color_values': (199, 21, 133),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        }
    },
    {
        'name': 'midnight blue',
        'google': {
            'is_rgb': True,
            'color_values': (25, 25, 112),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (25, 25, 112),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        }
    },
    {
        'name': 'mint cream',
        'google': {
            'is_rgb': True,
            'color_values': (245, 255, 250),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (245, 255, 250),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        }
    },
    {
        'name': 'misty rose',
        'google': {
            'is_rgb': True,
            'color_values': (255, 228, 225),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (255, 228, 225),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        }
    },
    {
        'name': 'moccasin',
        # 'google': {
        #     'is_rgb': True,
        #     'color_values': (0, 0, 0),
        #     'tsl_brt_100': None,
        #     'tcs_color': None,
        #     'm': None,
        #     'b': None
        # },
        'alexa': {                   # Need to tell Alexa to set bulb 'to the color moccasin'
            'is_rgb': True,
            'color_values': (255, 228, 181),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        }
    },
    {
        'name': 'navajo white',      # Google uses cct for this color
        'google': {
            'is_rgb': False,
            'color_values': 5000,
            'tsl_brt_100': None,
            'tcs_color': 4150,
            'm': None,
            'b': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (255, 222, 173),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        }
    },
    {
        'name': 'navy blue',
        'google': {
            'is_rgb': True,
            'color_values': (0, 0, 128),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 0, 128),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        }
    },
    {
        'name': 'old lace',          # Google uses cct for this color
        'google': {
            'is_rgb': False,
            'color_values': 6100,
            'tsl_brt_100': None,
            'tcs_color': 4640,
            'm': None,
            'b': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (253, 245, 230),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        }
    },
    {
        'name': 'olive',
        'google': {
            'is_rgb': True,
            'color_values': (128, 128, 0),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (128, 128, 0),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        }
    },
    {
        'name': 'olive drab',
        'google': {                  # Need to tell Google, set the bulb 'to the color olive drab'
            'is_rgb': True,
            'color_values': (107, 142, 35),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (107, 142, 35),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        }
    },
    # {
    #     'name': 'olive green',
    #     'google': {
    #         'is_rgb': True,
    #         'color_values': (0, 0, 0),
    #         'tsl_brt_100': None,
    #         'tcs_color': None,
    #         'm': None,
    #         'b': None
    #     },
    #     'alexa': {
    #         'is_rgb': True,
    #         'color_values': (0, 0, 0),
    #         'tsl_brt_100': None,
    #         'tcs_color': None,
    #         'm': None,
    #         'b': None
    #     }
    # },
    {
        'name': 'orange',
        'google': {
            'is_rgb': True,
            'color_values': (255, 102, 0),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (255, 165, 0),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        }
    },
    {
        'name': 'orange red',
        'google': {
            'is_rgb': True,
            'color_values': (255, 75, 0),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (255, 75, 0),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        }
    },
    {
        'name': 'orchid',
        'google': {
            'is_rgb': True,
            'color_values': (218, 112, 214),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (218, 112, 214),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        }
    },
    {
        'name': 'pale goldenrod',
        # 'google': {
        #     'is_rgb': True,
        #     'color_values': (0, 0, 0),
        #     'tsl_brt_100': None,
        #     'tcs_color': None,
        #     'm': None,
        #     'b': None
        # },
        'alexa': {
            'is_rgb': True,
            'color_values': (238, 232, 170),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        }
    },
    {
        'name': 'pale green',
        # 'google': {
        #     'is_rgb': True,
        #     'color_values': (0, 0, 0),
        #     'tsl_brt_100': None,
        #     'tcs_color': None,
        #     'm': None,
        #     'b': None
        # },
        'alexa': {
            'is_rgb': True,
            'color_values': (152, 251, 152),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        }
    },
    {
        'name': 'pale turquoise',
        # 'google': {
        #     'is_rgb': True,
        #     'color_values': (0, 0, 0),
        #     'tsl_brt_100': None,
        #     'tcs_color': None,
        #     'm': None,
        #     'b': None
        # },
        'alexa': {
            'is_rgb': True,
            'color_values': (180, 255, 255),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        }
    },
    {
        'name': 'pale violet red',
        # 'google': {
        #     'is_rgb': True,
        #     'color_values': (0, 0, 0),
        #     'tsl_brt_100': None,
        #     'tcs_color': None,
        #     'm': None,
        #     'b': None
        # },
        'alexa': {
            'is_rgb': True,
            'color_values': (219, 112, 147),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        }
    },
    {
        'name': 'papaya whip',
        'google': {
            'is_rgb': True,
            'color_values': (255, 239, 213),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (255, 239, 213),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        }
    },
    {
        'name': 'peach puff',
        'google': {
            'is_rgb': True,
            'color_values': (255, 218, 185),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (255, 218, 185),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        }
    },
    {
        'name': 'peru',
        'google': {
            'is_rgb': True,
            'color_values': (205, 133, 63),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (205, 133, 63),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        }
    },
    {
        'name': 'pink',
        'google': {
            'is_rgb': True,
            'color_values': (255, 192, 203),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (250, 185, 204),  # (250, 185, 203)
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        }
    },
    {
        'name': 'plum',
        'google': {
            'is_rgb': True,
            'color_values': (142, 69, 133),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (221, 160, 221),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        }
    },
    {
        'name': 'powder blue',
        'google': {
            'is_rgb': True,
            'color_values': (176, 224, 230),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (174, 224, 221),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        }
    },
    {
        'name': 'pumpkin',                    # Need to test for Alexa
        'google': {
            'is_rgb': True,
            'color_values': (255, 117, 24),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        },
        # 'alexa': {
        #     'is_rgb': True,
        #     'color_values': (0, 0, 0),
        #     'tsl_brt_100': None,
        #     'tcs_color': None,
        #     'm': None,
        #     'b': None
        # }
    },
    {
        'name': 'purple',
        'google': {
            'is_rgb': True,
            'color_values': (128, 0, 128),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (160, 32, 240),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        }
    },
    {
        'name': 'rebecca purple',
        # 'google': {
        #     'is_rgb': True,
        #     'color_values': (0, 0, 0),
        #     'tsl_brt_100': None,
        #     'tcs_color': None,
        #     'm': None,
        #     'b': None
        # },
        'alexa': {
            'is_rgb': True,
            'color_values': (102, 51, 153),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        }
    },
    {
        'name': 'red',
        'google': {
            'is_rgb': True,
            'color_values': (255, 0, 0),
            'tsl_brt_100': 18500,
            'tcs_color': (245, 0, 3),
            'm': 200,
            'b': 800
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (255, 0, 0),
            'tsl_brt_100': 18500,
            'tcs_color': (245, 0, 3),
            'm': 200,
            'b': 800
        }
    },
    {
        'name': 'rosy brown',
        'google': {
            'is_rgb': True,
            'color_values': (188, 143, 143),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (188, 143, 143),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        }
    },
    {
        'name': 'royal blue',
        'google': {
            'is_rgb': True,
            'color_values': (0, 5, 102),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (65, 105, 225),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        }
    },
    {
        'name': 'saddle brown',
        # 'google': {
        #     'is_rgb': True,
        #     'color_values': (0, 0, 0),
        #     'tsl_brt_100': None,
        #     'tcs_color': None,
        #     'm': None,
        #     'b': None
        # },
        'alexa': {
            'is_rgb': True,
            'color_values': (139, 69, 19),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        }
    },
    {
        'name': 'salmon',
        'google': {
            'is_rgb': True,
            'color_values': (250, 128, 114),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        },
        'alexa': {                            # Alexa uses the 'light salmon' rgb values for salmon
            'is_rgb': True,
            'color_values': (255, 160, 125),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        }
    },
    {
        'name': 'sandy brown',
        'google': {
            'is_rgb': True,
            'color_values': (244, 164, 96),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (244, 164, 96),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        }
    },
    {
        'name': 'sea green',
        'google': {
            'is_rgb': True,
            'color_values': (46, 139, 87),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (46, 139, 87),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        }
    },
    {
        'name': 'seashell',          # Google uses cct for this color
        'google': {
            'is_rgb': False,
            'color_values': 6100,
            'tsl_brt_100': None,
            'tcs_color': 4640,
            'm': None,
            'b': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (255, 245, 238),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        }
    },
    {
        'name': 'sienna',
        'google': {
            'is_rgb': True,
            'color_values': (136, 45, 23),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (160, 82, 45),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        }
    },
    {
        'name': 'silver',
        'google': {
            'is_rgb': True,
            'color_values': (192, 192, 192),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (192, 192, 192),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        }
    },
    # {
    #     'name': 'sky',
    #     'google': {
    #         'is_rgb': True,
    #         'color_values': (0, 0, 0),
    #         'tsl_brt_100': None,
    #         'tcs_color': None,
    #         'm': None,
    #         'b': None
    #     },
    #     'alexa': {
    #         'is_rgb': True,
    #         'color_values': (0, 0, 0),
    #         'tsl_brt_100': None,
    #         'tcs_color': None,
    #         'm': None,
    #         'b': None
    #     }
    # },
    {
        'name': 'sky blue',
        'google': {
            'is_rgb': True,
            'color_values': (135, 206, 235),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (135, 206, 235),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        }
    },
    # {
    #     'name': 'slate',
    #     'google': {
    #         'is_rgb': True,
    #         'color_values': (0, 0, 0),
    #         'tsl_brt_100': None,
    #         'tcs_color': None,
    #         'm': None,
    #         'b': None
    #     },
    #     'alexa': {
    #         'is_rgb': True,
    #         'color_values': (0, 0, 0),
    #         'tsl_brt_100': None,
    #         'tcs_color': None,
    #         'm': None,
    #         'b': None
    #     }
    # },
    {
        'name': 'slate blue',
        'google': {
            'is_rgb': True,
            'color_values': (106, 90, 205),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (106, 90, 205),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        }
    },
    {
        'name': 'slate gray',
        'google': {
            'is_rgb': True,
            'color_values': (112, 128, 144),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (112, 128, 144),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        }
    },
    {
        'name': 'smitten',
        'google': {
            'is_rgb': True,
            'color_values': (200, 65, 134),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        },
        # 'alexa': {
        #     'is_rgb': True,
        #     'color_values': (0, 0, 0),
        #     'tsl_brt_100': None,
        #     'tcs_color': None,
        #     'm': None,
        #     'b': None
        # }
    },
    {
        'name': 'snow',                # Google uses cct for this color
        'google': {
            'is_rgb': False,
            'color_values': 6500,
            'tsl_brt_100': None,
            'tcs_color': 4850,
            'm': None,
            'b': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (255, 250, 250),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        }
    },
    {
        'name': 'soft white',                # Google uses cct for this color
        'google': {
            'is_rgb': False,
            'color_values': 3000,
            'tsl_brt_100': None,
            'tcs_color': 2830,
            'm': None,
            'b': None
        },
        'alexa': {
            'is_rgb': False,
            'color_values': 2700,
            'tsl_brt_100': None,
            'tcs_color': 2630,
            'm': None,
            'b': None
        }
    },
    {
        'name': 'spring green',
        'google': {
            'is_rgb': True,
            'color_values': (0, 255, 127),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 255, 127),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        }
    },
    {
        'name': 'steel blue',
        'google': {
            'is_rgb': True,
            'color_values': (70, 130, 180),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (70, 130, 180),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        }
    },
    {
        'name': 'tan',
        'google': {
            'is_rgb': True,
            'color_values': (210, 180, 140),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        },
        'alexa': {                           # Need to tell Alexa turn bulb 'to the color tan'
            'is_rgb': True,
            'color_values': (210, 180, 140),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        }
    },
    {
        'name': 'teal',
        'google': {
            'is_rgb': True,
            'color_values': (0, 128, 128),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 128, 128),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        }
    },
    {
        'name': 'thistle',
        'google': {
            'is_rgb': True,
            'color_values': (216, 191, 216),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (216, 191, 216),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        }
    },
    {
        'name': 'tomato',
        'google': {
            'is_rgb': True,
            'color_values': (255, 99, 71),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (255, 99, 71),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        }
    },
    {
        'name': 'turquoise',
        'google': {
            'is_rgb': True,
            'color_values': (64, 224, 208),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (64, 224, 208),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        }
    },
    {
        'name': 'ultramarine',               # Need to test for Alexa
        'google': {
            'is_rgb': True,
            'color_values': (18, 10, 143),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        },
        # 'alexa': {
        #     'is_rgb': True,
        #     'color_values': (0, 0, 0),
        #     'tsl_brt_100': None,
        #     'tcs_color': None,
        #     'm': None,
        #     'b': None
        # }
    },
    {
        'name': 'vermillion',                # Need to test for Alexa
        'google': {
            'is_rgb': True,
            'color_values': (217, 56, 30),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        },
        # 'alexa': {
        #     'is_rgb': True,
        #     'color_values': (0, 0, 0),
        #     'tsl_brt_100': None,
        #     'tcs_color': None,
        #     'm': None,
        #     'b': None
        # }
    },
    {
        'name': 'violet',
        'google': {
            'is_rgb': True,
            'color_values': (127, 0, 255),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (238, 130, 238),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        }
    },
    {
        'name': 'warm',                # Google uses cct for this color
        # 'google': {
        #     'is_rgb': False,
        #     'color_values': '',
        #     'tsl_brt_100': None,
        #     'tcs_color': None,
        #     'm': None,
        #     'b': None
        # },
        'alexa': {
            'is_rgb': False,
            'color_values': 2200,
            'tsl_brt_100': None,
            'tcs_color': 2320,
            'm': None,
            'b': None
        }
    },
    {
        'name': 'warm white',                # Google uses cct for this color
        'google': {
            'is_rgb': False,
            'color_values': 3000,
            'tsl_brt_100': None,
            'tcs_color': 2830,
            'm': None,
            'b': None
        },
        'alexa': {
            'is_rgb': False,
            'color_values': 2200,
            'tsl_brt_100': None,
            'tcs_color': 2320,
            'm': None,
            'b': None
        }
    },
    {
        'name': 'web gray',
        # 'google': {
        #     'is_rgb': True,
        #     'color_values': (0, 0, 0),
        #     'tsl_brt_100': None,
        #     'tcs_color': None,
        #     'm': None,
        #     'b': None
        # },
        'alexa': {
            'is_rgb': True,
            'color_values': (128, 128, 128),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        }
    },
    {
        'name': 'web green',
        # 'google': {
        #     'is_rgb': True,
        #     'color_values': (0, 0, 0),
        #     'tsl_brt_100': None,
        #     'tcs_color': None,
        #     'm': None,
        #     'b': None
        # },
        'alexa': {
            'is_rgb': True,
            'color_values': (0, 128, 0),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        }
    },
    {
        'name': 'web maroon',
        'google': {
            'is_rgb': True,
            'color_values': (128, 0, 0),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (178, 48, 96),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        }
    },
    {
        'name': 'web purple',
        'google': {
            'is_rgb': True,
            'color_values': (128, 0, 128),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (128, 0, 128),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        }
    },
    {
        'name': 'wheat',
        'google': {
            'is_rgb': True,
            'color_values': (245, 222, 179),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (245, 222, 179),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        }
    },
    {
        'name': 'white',                   # Google uses cct for this color
        'google': {
            'is_rgb': False,
            'color_values': 5000,
            'tsl_brt_100': None,
            'tcs_color': 4150,
            'm': None,
            'b': None
        },
        'alexa': {
            'is_rgb': False,
            'color_values': 4000,
            'tsl_brt_100': None,
            'tcs_color': 3350,
            'm': None,
            'b': None
        }
    },
    {
        'name': 'white smoke',             # Google uses cct for this color
        'google': {
            'is_rgb': False,
            'color_values': 7000,
            'tsl_brt_100': None,
            'tcs_color': 5335,
            'm': None,
            'b': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (245, 245, 245),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        }
    },
    {
        'name': 'yellow',
        'google': {
            'is_rgb': True,
            'color_values': (255, 255, 0),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (255, 255, 0),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        }
    },
    {
        'name': 'yellow green',
        'google': {
            'is_rgb': True,
            'color_values': (154, 205, 50),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
        },
        'alexa': {
            'is_rgb': True,
            'color_values': (154, 205, 50),
            'tsl_brt_100': None,
            'tcs_color': None,
            'm': None,
            'b': None
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

    voice_agent = 'alexa'
    # color_list = []
    # for color in supported_colors_list:
    #     if color.get(voice_agent):
    #         if color.get(voice_agent).get('is_rgb'):
    #             color_list.append(color)

    for color in supported_colors_list:
        if color.get(voice_agent).get('color_values'):
            print(color['name'], color[voice_agent]['color_values'])
        # print(color['name'], color[voice_agent]['color_values'])

    # print('color_list length: ', len(color_list))

else:
    print('Successfully imported supported colors.py')


