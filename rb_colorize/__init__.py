from config import settings

from tools.collection import get_collection, get_collection_json
from tools.normalize_color import degree_correction

collection_names = settings["COLLECTIONS"]

def main(h:int, s=100) -> list:

    palettes = {}

    collections = [
        {
            "h": h, "s": s,
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
            "h": degree_correction(h+37),
            "s": s,
            "name": 'error',
            },
        {
            "h": degree_correction(h-37),
            "s": s,
            "name": 'notify',
            },
        {
            "h": 1,
            "s": 100,
            "name": 'grey',
            },
    ]

    for collection in collections:
        palettes[collection["name"]] = get_collection_json(**collection)

    return palettes

    
#     # curl -H "Content-Type: application/json" -X POST -d '{"hue": 202, "steps": 7, "saturation": 90, "lightness": 90}' http://localhost:5005/colorize/api > dump.json


if __name__ == "__main__":
    
    x = main(220)
    print(x)

    from previews.css import render_css_colors
    from previews.generate_preview import index_html

    render_css_colors(147)
    index_html()

