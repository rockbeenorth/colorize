from previews.css import render_css_colors
from previews.generate_preview import index_html, generate_basic_css


def main(h, s):
    print('hue:', h, 'saturation', s)
    render_css_colors(h=h, s=s)
    generate_basic_css()
    index_html()

    return render_css_colors(h=h, s=s)

#     # curl -H "Content-Type: application/json" -X POST -d '{"hue": 202, "steps": 7, "saturation": 90, "lightness": 90}' http://localhost:5005/colorize/api > dump.json


if __name__ == "__main__":

    from tools.color import Color
    red = Color(1312, 700, 80)
    red.set_name()
    opposite = red.opposite

    print(red.name, red, opposite)

    main(220, 80)
