def normalize_color(hue:int) -> tuple:
    """
Normalizes any HSLA `hue` (color, in range from 1 to 360) to the basic settings.

Incoming: `hue` from HSLA system.

Returns a tuple with normalized HSLA:

`hue`: incoming, `saturation`: 100, `lightness`: 50, `opacity`: 1"""
    
    if hue > 0:
        return (hue, 100, 50, 1)
    else:
        return (hue, 100, 100, 1)


def normalize_to_hundred(value:int) -> int:
    """
    Double-check if saturation or brightness contained within 0 to 100.
    """

    if value > 100:
        return 100
    elif value < 0:
        return 0
    else:
        return value
    
def degree_correction(hue:int) -> int:
    """
Checks if hue number is more than 360 degrees or less and returns correted number.
    """

    if  hue < 0 or hue > 360:
        return hue % 360
    else:
        return hue


if __name__ == "__main__":
    print(normalize_color(1))
    print(normalize_color(0))
    print(normalize_color(400))
    print(normalize_color(359))
    print(normalize_color(360))
    print(normalize_color(-450))