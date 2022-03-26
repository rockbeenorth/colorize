import os

PROJECT_DIRECTORY = os.getcwd().replace('/rb_colorize', '')

settings = {
    "COLLECTIONS": ["art", "bart", "cart"],
    "DARK_DESATURATE": 15,
    "FONT": '-apple-system, BlinkMacSystemFont, "Helvetica Neue", "Segoe UI", "Fira Sans", Roboto, Ubuntu, "Droid Sans", "Arial", sans-serif',
}

color_settings = {
    "BACKGROUND_COLOR_LIGHT" : "hsl(0, 0%, 99%)",
    "BACKGROUND_COLOR_DARK" : "hsl(0, 0%, 6%)",
    "TEXT_WHITE" : "hsl(0, 0%, 99%)",
    "TEXT_BLACK" : "hsl(0, 0%, 6%)",
}

file_paths = {
    "PATH":         f"{PROJECT_DIRECTORY}/core/",
    "BASIC_CSS" :   "_color_scheme.scss",
    "COLOR_SCHEME": "_colors.scss",
    "COLOR_LAYERS": "_color_layers.scss",
    "CARDS_HTML":   "_cards.html",
    "CARDS_LAYERED_HTML":   "_cards_layered.html",
    "INDEX_HTML":   "index.html",
}