import json

from tools.color_conversions import hsl_to_rgb, rgb_to_hex
from tools.normalize_color import degree_correction, normalize_color, normalize_to_hundred
from tools.check_brightness import is_light_text_rgb


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
        self.rgb = self.get_rgb()
        self.hex = self.get_hex_value()
        self.bright_text = is_light_text_rgb(self.rgb)
        self.normalized = normalize_color(self.h)

    # Setters

    def set_layer(self, layer: int):
        self.layer = int(layer)

    def set_order(self, order: int):
        self.order = int(order)

    def set_name(self, name: str):
        self.name = str(name)

    # Getters

    def get_opposite(self):
        opposite_hue = degree_correction(self.h + 180)
        return opposite_hue

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
