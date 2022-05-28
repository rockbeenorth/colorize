def get_color(h:int, level:int, s:int=90) -> tuple:

    # Lightness scales for light and dark modes
    SCALE_LIGHT = [98, 96, 94, 90, 86, 81, 74, 66, 55, 39]
    SCALE_DARK = [4, 6, 8, 12, 16, 21, 28, 36, 47, 63]
    DARK_DESATURATE = 10

    # Check if level is within range 1-10
    if level > 10:
        level = 10
    elif level < 1:
        level = 2

    # Check if hue is within range 0-360:
    if h < 0 or h > 360:
        h = h % 360

    light = f'hsl: ({h}, {s}%, {SCALE_LIGHT[level-1]}%)'
    dark = f'hsl: ({h}, {s-DARK_DESATURATE}%, {SCALE_DARK[level-1]}%)'

    return light, dark

if __name__ == '__main__':
    print(get_color(12, 10))
