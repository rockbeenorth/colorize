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

    main(207, 100, 'split_complementary')
