import json
from colorsys import hls_to_rgb  # , rgb_to_hls
from math import sqrt


THRESHOLD = 140

def get_luminocity(HSL: tuple, optional=False) -> int:

    # https://alienryderflex.com/hsp.html
    
    h, s, l = HSL
    r, g, b = hsl_to_rgb(h, s, l)

    optional_values = (.241, .691, .068)
    informed_values = (.299, .587, .114)

    X, Y, Z = informed_values

    if optional:
        X, Y, Z = optional_values
    
    luminocity = sqrt(
        r * r * X +
        g * g * Y +
        b * b * Z
    )

    return luminocity

def get_luminocity_percetage(luminocity):
    return int((luminocity/255)*100)


def is_light_text(HSL: tuple, threshhold: int = THRESHOLD) -> bool:
    """
    Check if HSL color works with white font. Default brightness threshold is set to `140` (can be safely adjusted between 130 to 145).

    In: `(h,s,l)` tuple;

    Returns `bool`:

    - `True` if text should be bright (white)
    - `False` if text should be dark (black)
    """

    brightness = get_luminocity(HSL)

    if brightness < threshhold:
        return True
    else:
        return False


def is_light_text_rgb(rgb: tuple, threshhold=THRESHOLD) -> bool:
    """
Check if RGB color works with white font. Default brightness threshold is set to `140` (can be safely adjusted between 130 to 145).

In: `(r,g,b)` tuple;

Returns `bool`:
- `True` if text should be bright (white)
- `False` if text should be dark (black)
    """

    r, g, b = rgb

    brightness = sqrt(
        r * r * .241 +
        g * g * .691 +
        b * b * .068
    )

    if brightness < threshhold:
        return True
    else:
        return False


def normalize_color(hue: int) -> tuple:
    """
Normalizes any HSLA `hue` (color, in range from 1 to 360) to the basic settings.

Incoming: `hue` from HSLA system.

Returns a tuple with normalized HSLA:

`hue`: incoming, `saturation`: 100, `lightness`: 50, `opacity`: 1"""

    if hue > 0:
        return (hue, 100, 50, 1)
    else:
        return (hue, 100, 100, 1)


def normalize_to_hundred(value: int) -> int:
    """
    Double-check if saturation or brightness contained within 0 to 100.
    """

    if value > 100:
        return 100
    elif value < 0:
        return 0
    else:
        return value


def degree_correction(hue: int) -> int:
    """
Checks if hue number is more than 360 degrees or less and returns correted number.
    """

    if hue < 0 or hue > 360:
        return hue % 360
    else:
        return hue


def hsl_to_rgb(hue: int, saturation: int, lightness: int) -> tuple:
    """
    *In:* `Hue` (0-360), `saturation` (0-100), `lightness` (0-100) as in HSL model.

    *Out:* `(r, g, b)` normalized to RGB model (tuple).
    """

    H = hue/360
    S = saturation/100
    L = lightness/100

    RGB = hls_to_rgb(H, L, S)

    r, g, b = (int(round(i*255, 0)) for i in RGB)

    return r, g, b


def rgb_to_hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)


# Hue name adjustments
cool = 'cool'
warm = 'warm'
mid = 'mid'

# Lightness name modificators
dark = 'dark'
medium = 'medium'
light = 'light'
q1 = 'darker'
q2 = 'dark'
q3 = 'light'
q4 = 'lighter'

hue_group_names = {
    ('red', cool): range(345, 345+15),
    ('red', mid): range(0, 0+15),
    ('red', warm): range(15, 15+15),
    ('orange', ''): range(30, 30+15),
    ('yellow', warm): range(45, 45+15),
    ('yellow', mid): range(60, 60+15),
    ('yellow', cool): range(75, 75+15),
    ('green', 'yellow'): range(90, 90+15),
    ('green', warm): range(105, 105+15),
    ('green', mid): range(125, 125+15),
    ('green', cool): range(135, 135+15),
    ('cyan', 'green'): range(150, 150+15),
    ('cyan', warm): range(165, 165+15),
    ('cyan', mid): range(180, 180+15),
    ('cyan', cool): range(195, 195+15),
    ('cyan', 'blue'): range(210, 210+15),
    ('blue', cool): range(225, 225+15),
    ('blue', mid): range(240, 240+15),
    ('blue', warm): range(255, 255+15),
    ('violet', ''): range(270, 270+15),
    ('magenta', cool): range(285, 285+15),
    ('magenta', mid): range(300, 300+15),
    ('magenta', warm): range(315, 315+15),
    ('magenta', 'red'): range(330, 330+15),
}


def get_hue_group_name(hue: int) -> str:
    hue = degree_correction(hue)
    for k, v in hue_group_names.items():
        if hue in v:
            if k[1]:
                return(f'{k[0]}-{k[1]}')
            elif not k[1]:
                return(f'{k[0]}')


class Color:

    name = None
    layer = None
    order = None

    def __init__(self, h: int, s=50, l=50, a=1):
        self.h = degree_correction(h)
        self.s = normalize_to_hundred(s)
        self.l = normalize_to_hundred(l)
        self.a = a
        self.hsl = (h, s, l)
        self.opposite = self.get_opposite()
        self.rgb = self.get_rgb()
        self.hex = self.get_hex_value()
        self.bright_text = is_light_text_rgb(self.rgb)
        self.normalized = normalize_color(self.h)
        self.luminocity = get_luminocity(self.hsl)
        self.luminocity_percentage = get_luminocity_percetage(self.luminocity)
        self.set_name()
        self.set_layer()
        self.set_order()

    # Setters

    def set_layer(self, layer: int = None):
        if layer == None:
            self.layer = int(self.l)
        else:
            self.layer = int(layer)

    def set_order(self, order: int = None):
        if self.order == None:
            self.order = 0
        else:
            self.order = int(order)

    def set_name(self, name: str = None):
        if self.l <= 25:
            lighness_title = q1
        elif 25 < self.l <= 50:
            lighness_title = q2
        elif 50 < self.l <= 75:
            lighness_title = q3
        elif 75 < self.l <= 100:
            lighness_title = q4

        if name == None:
            self.name = str(f'{get_hue_group_name(self.h)}-{lighness_title}')
        else:
            self.name = str(name)

    # Getters

    def get_opposite(self, type=None) -> str:
        """
        Get a color that is on the opposite side of the color wheel (hue + 180 degrees).

        Accepts `'rgb'`, `'hsl'` and `'hex'` keys (`hsl` is default and returns an hsl tuple even when argument is empty).

        Example: `get_opposite('rgb')` will return a tuple with red, green, blue values.
        """
        types = ['rgb', 'hex', 'hsl']
        opposite_hue = degree_correction(self.h + 180)
        opposite = (opposite_hue, self.s, self.l)

        if not type or type == 'hsl':
            return opposite

        if type in types:
            if type == 'rgb':
                return hsl_to_rgb(*opposite)
            elif type == 'hex':
                return rgb_to_hex(*hsl_to_rgb(*opposite))

        return opposite

    def get_opposite_class(self):
        opposite_hue = degree_correction(self.h + 180)
        return Color(opposite_hue, self.s, self.l)

    def get_rgb(self):
        return hsl_to_rgb(*self.hsl)

    def get_variable(self):
        if self.name and self.order:
            return f'--{self.name}-{self.order}'
        else:
            return f'--color-{self.l}'

    def get_hsla_value(self):
        return f'hsla({self.h}, {self.s}%, {self.l}%, {self.a})'

    def get_rgba_value(self):
        r, g, b = self.rgb
        return f'rgba({r}, {g}, {b}, {self.a})'

    def get_hex_value(self):
        return rgb_to_hex(*self.rgb)

    def get_light_bg_color(self) -> tuple:
        """
        returns H,S,L values for bg color if it is more than a given threshold, else returns values for white background.
        """

        lightBg = 100;
        lightThresholdStep = 30
        lightThreshold = lightBg - lightThresholdStep

        if self.luminocity_percentage > lightThreshold:
            return self.h, 3, lightBg - self.luminocity_percentage - 5
        else:
            return self.h, 0, 100

    def get_dark_bg_color(self):
        darkBg = 0
        darkThresholdStep = 40
        darkThreshold = darkBg + darkThresholdStep

        if self.luminocity_percentage <= darkThreshold:
            return self.h, 3, 100 - self.luminocity_percentage + 20
        else:
            return self.h, 0, 0
        


    def get_object(self):
        return {
            "order": self.order,
            "name": self.name,
            "var": self.get_variable(),
            "hex": self.hex,
            "rgb": self.rgb,
            "hsl": self.hsl,
            "bright_text": self.bright_text,
            "luminocity": self.luminocity,
            "luminocity_percentage": self.luminocity_percentage,
            "light_bg": self.get_light_bg_color(),
            "dark_bg": self.get_dark_bg_color(),
        }

    def get_json(self):
        return json.dumps(self.get_object())

    def __repr__(self):
        return f"Color({self.name}-{self.order}: {self.h}, {self.s}, {self.l})"


if __name__ == "__main__":

    color = {
        "h": 220,
        "s": 90,
        "l": 98,
    }

    c = Color(**color)
    print(c.hex)
    print(c.name)
    print(c.opposite)
