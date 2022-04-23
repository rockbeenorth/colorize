import json

from tools.color_conversions import hsl_to_rgb, rgb_to_hex
from tools.normalize_color import degree_correction, normalize_color, normalize_to_hundred
from tools.check_brightness import is_light_text_rgb

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
    ('orange'): range(30, 30+15),
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
    ('violet'): range(270, 270+15),
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
            else:
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

        self.set_name()
        self.set_layer()
        self.set_order()

    # Setters

    def set_layer(self, layer: int = None) -> int:
        if layer == None:
            self.layer = int(self.l)
        else:
            self.layer = int(layer)

    def set_order(self, order: int = None):
        if self.order == None:
            self.order = 0
        else:
            self.order = int(order)

    def set_name(self, name: str = None) -> str:

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

    def get_json(self):
        repr = {
            "var": self.get_variable(),
            "hex": self.hex,
            "rgb": self.rgb,
            "hsl": self.hsl,
            "bright_text": self.bright_text
        }
        return json.dumps(repr)

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
