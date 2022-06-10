import os
from tools.color import Color

PROJECT_DIRECTORY = os.getcwd().replace('/rb_colorize', '')

settings = {
    "THRESHOLD": 140,
    "COLLECTIONS": ["arrow", "bungee", "cable"],
    "DARK_DESATURATE": 10,
    "DARK_INCREASE_BRIGHTNESS": 3,
    "FONT": '-apple-system, BlinkMacSystemFont, "Helvetica Neue", "Segoe UI", "Fira Sans", Roboto, Ubuntu, "Droid Sans", "Arial", sans-serif',
}

color_settings = {
    "BACKGROUND_COLOR_LIGHT": Color(0, 0, 99).get_hsla_value(),
    "BACKGROUND_COLOR_DARK": Color(0, 0, 6).get_hsla_value(),
    "TEXT_WHITE": Color(0, 0, 99).get_hsla_value(),
    "TEXT_BLACK": Color(0, 0, 6).get_hsla_value(),
}

collection_names = {
    'styling': [
        'arrow',
        'bungee',
        'cable',
        'dream',
        'edge',
        'fruit',
    ],
    'gray': [
        'gray',
        'gray-warm',
        'gray-cool',
    ],
    'ui': [
        'notification',
        'warning',
    ]
}

color_schemes = {
    "complementary": [0, 180],
    "split_complementary": [0, 150, -150],
    "double_complementary": [0, 30, 180, 210],
    "triadic": [0, 120, 240],
    "square": [0, 90, 180, 270],
    "analogous": [0, -30, 30],
}

file_paths = {
    "PATH":         f"{PROJECT_DIRECTORY}/core/",
    "BASIC_CSS":   "_color_scheme.scss",
    "COLOR_SCHEME": "_colors.scss",
    "COLOR_LAYERS": "_color_layers.scss",
    "CARDS_HTML":   "_cards.html",
    "CARDS_LAYERED_HTML":   "_cards_layered.html",
    "INDEX_HTML":   "index.html",
}

about = {
    "VERSION": "Alpha 0.1.1"
}
