from colorsys import hls_to_rgb #, rgb_to_hls

def hsl_to_rgb(hue:int, saturation:int, lightness:int) -> tuple:
    """
    *In:* `Hue` (0-360), `saturation` (0-100), `lightness` (0-100) as in HSL model.

    *Out:* `(r, g, b)` normalized to RGB model (tuple).
    """

    H = hue/360
    S = saturation/100
    L = lightness/100

    RGB = hls_to_rgb(H, L, S)

    r,g,b = (int(round(i*255, 0)) for i in RGB)

    return r,g,b


def rgb_to_hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)