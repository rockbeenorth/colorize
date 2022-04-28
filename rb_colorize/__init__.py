import json

from config import settings, about
from tools.color import degree_correction

# from previews.css import render_css_colors
# from previews.generate_preview import index_html, generate_basic_css

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

    from tools.color import Color
    # # red = Color(275, 90, 80)
    # red = Color(221, 90, 80)
    # red.set_name()
    # opposite = red.opposite

    # next = red.get_opposite_class()

    # print(red.name, red, opposite)
    # print(next.name, next, next.hsl, next.get_json())

    # make = main(333, 80)
    # palettes(333, 80)

    # print(type(make))

    # print(json.dumps(make, indent=4))

    from tools.collection import Collection

    y = Collection('Yella', 220, 80)
    
    print('dark', y.dark)
    print('light', y.light)