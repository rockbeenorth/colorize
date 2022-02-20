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

# # one
# h = 220/360
# s = 90/100
# l = 47/100

# h,s,l

# # two

# x = hls_to_rgb(h, l, s)
# r,g,b = x

# r,g,b

# R = r*255
# G = g*255
# B = b*255

# z = R,G,B

# jj = [int(round(i, 0)) for i in z]

# jj

# y = rgb_to_hls(r,g,b)
# y

# #  three

# H,S,L = y
# H = H*360
# S = S*100
# L = L*100

# H,S,L

# # https://css-tricks.com/converting-color-spaces-in-javascript/

# from colorsys import hls_to_rgb
# import colorsys

# # https://www.niwa.nu/2013/05/math-behind-colorspace-conversions-rgb-hsl/