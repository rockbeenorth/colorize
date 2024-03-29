from tools.scheme import Scheme
from tools.color import Color
from tools.collection import Collection
from config import settings, about
from previews.css import render_css_colors
from previews.generate_preview import index_html, generate_basic_css

collection_names = settings["COLLECTIONS"]
version = about["VERSION"]

def main(h, s, model=None):
    print('hue:', h, 'saturation:', s, 'model:', model)
    render_css_colors(h=h, s=s, model=model)
    generate_basic_css()
    index_html()

    return render_css_colors(h=h, s=s, model=model)

#     # curl -H "Content-Type: application/json" -X POST -d '{"hue": 202, "steps": 7, "saturation": 90, "lightness": 90}' http://localhost:5005/colorize/api > dump.json

if __name__ == "__main__":

    h = 90
    s = 50
    # model = 'triadic'
    model = 'complementary'


    main(h, s, model=model)
    # # print(x)
    # result = []
    # s = Scheme(210, 90, model='split_complementary', steps=12)
    # for c in s.collections:

    #     collection = {
    #         c.name : [[color.get_json() for color in c.light], [color.get_json() for color in c.dark]]
    #     }

    #     result.append(collection)
    #     print(collection)

        # print("\n")
        # print("\n")
        # print(c.name, 'light', c.light)
        # print(c.name, 'dark', c.dark)


    # color = Color(220)
    # print(color)