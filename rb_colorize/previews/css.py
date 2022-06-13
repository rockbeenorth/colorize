from config import settings, file_paths
from tools.collection import Collection
from tools.scheme import Scheme
from tools.color import degree_correction
from previews.generate_preview import divs_sum_recursive

collection_names = settings["COLLECTIONS"]


def render_css_colors(h: int, s=100, model=None) -> list:

    MODEL = Scheme(h, s, model=model, steps=10)
    palettes = {}

    # Template
    open_string = [":root {\n"]
    light_lines = []
    open_dark = ["\n\t@media (prefers-color-scheme: dark) {\n"]
    dark_lines = []
    close_dark = ["\t}\n"]
    close_string = ["}"]

    # Layers
    layers = []
    layers_html = []
    layers_titles = []

    # for name, palette in palettes.items():
    for palette in MODEL.collections:
        name = palette.name
        for c in palette.light:
            light_lines.append("\t" + c.get_variable() +
                               ": " + c.get_hsla_value() + ";\n")

            if c.bright_text:
                text_color = "\tcolor: var(--text-color-light);\n"
            else:
                text_color = "\tcolor: var(--text-color-dark);\n"

            layer = layers_css_template(
                name, c.order, text_color, c.get_variable())
            layers.append(layer)

            html_classname = f'{name}-{c.order}'
            preview_line = layers_html_template(html_classname)
            layers_titles.append(html_classname)
            layers_html.append(preview_line)

        for c in palette.dark:
            dark_lines.append("\t\t" + c.get_variable() +
                            #   ":\t" + c.get_hsla_value() + ";\n")
                              ": " + c.get_hsla_value() + ";\n")


    # write file
    lines = open_string + light_lines + open_dark + \
        dark_lines + close_dark + close_string
    layered_html = divs_sum_recursive(layers_titles)

    with open(f"{file_paths['PATH']}{file_paths['COLOR_SCHEME']}", "w") as f:
        for line in lines:
            f.write(line)

    with open(f"{file_paths['PATH']}{file_paths['COLOR_LAYERS']}", "w") as f:
        for line in layers:
            f.write(line)

    with open(f"{file_paths['PATH']}{file_paths['CARDS_HTML']}", "w") as f:
        for line in layers_html:
            f.write(line)

    with open(f"{file_paths['PATH']}{file_paths['CARDS_LAYERED_HTML']}", "w") as f:
        for line in layered_html:
            f.write(line)

    return palettes


def layers_html_template(name):
    return f'''
<div class="{name} colorize__demo_card">
    <h1>Demo lorem ipsum</h1>
    <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Odit vitae minus, quaerat vero sit sed rem debitis distinctio hic laboriosam optio error! Incidunt corporis veniam asperiores modi ducimus, inventore sit!</p>
</div>'''


def layers_css_template(name, layer, text_color, c_var):
    return f'.{name}-{layer}' + '{\n' + \
        f'{text_color}\tbackground-color: var({c_var});\n' \
        '}\n'


if __name__ == "__main__":
    x = render_css_colors(204, 100)

    # for k, v in x.items():
    #     print(k, v.name)
