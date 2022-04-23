from math import sqrt
from tools.color_conversions import hsl_to_rgb
# from config import settings

# THRESHOLD = settings["THRESHOLD"]
THRESHOLD = 140

# from color_conversions import hsl_to_rgb


def is_light_text(HSL: tuple, threshhold: int = THRESHOLD) -> bool:
    """
    Check if HSL color works with white font. Default brightness threshold is set to `140` (can be safely adjusted between 130 to 145).

    In: `(h,s,l)` tuple;

    Returns `bool`:

    - `True` if text should be bright (white)
    - `False` if text should be dark (black)
    """
    h, s, l = HSL

    r, g, b = hsl_to_rgb(h, s, l)

    brightness = sqrt(
        r * r * .241 +
        g * g * .691 +
        b * b * .068
    )

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


if __name__ == "__main__":

    print(is_light_text((220, 80, 70)))
