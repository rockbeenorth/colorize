from config import settings, about
from tools.color import degree_correction

from previews.css import render_css_colors
from previews.generate_preview import index_html, generate_basic_css

collection_names = settings["COLLECTIONS"]
version = about["VERSION"]


def main(h: int, s=100) -> list:

    palettes = {}

    collections = [
        {
            "h": h,
            "s": s,
            "name": collection_names[0],
        },
        {
            "h": degree_correction(h+120),
            "s": s,
            "name": collection_names[1],
        },
        {
            "h": degree_correction(h-120),
            "s": s,
            "name": collection_names[2],
        },
        {
            "h": 0,
            "s": 0,
            "name": "grey",
        },
        {
            "h": degree_correction(h+37),
            "s": s,
            "name": 'error',
        },
        {
            "h": degree_correction(h-37),
            "s": s,
            "name": 'notify',
        },
    ]

    for collection in collections:
        palettes[collection["name"]] = get_collection_json(**collection)

    return palettes


def palettes(h, s):
    print('hue:', h, 'saturation', s)
    render_css_colors(h=h, s=s)
    generate_basic_css()
    index_html()

    return render_css_colors(h=h, s=s)

#     # curl -H "Content-Type: application/json" -X POST -d '{"hue": 202, "steps": 7, "saturation": 90, "lightness": 90}' http://localhost:5005/colorize/api > dump.json

if __name__ == "__main__":

    # palettes(14, 90)

    THRESHOLD = 140

    from tools.color import Color

    above = []
    below = []
    zero = []
    
    lumes = []
    diffs = []

    for i in range(0, 360):
        c = Color(i, 80, 50)
        lume = int(c.luminocity)
        diff = lume - THRESHOLD
        lumes.append(lume)
        diffs.append(diff)

        if diff < 0:
            below.append(c)
        elif diff > 0:
            above.append(c)
        else:
            zero.append(c)

        print(i, c.name, f'\t{lume}', f'\t{diff}')

    print('above', len(above))
    print('below', len(below))
    print('zero', len(zero))

    print(min(lumes))
    print(max(lumes))
    print(min(diffs))
    print(max(diffs))
