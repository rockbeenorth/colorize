# DEPRECATED
def generate_color_scheme(collections:dict) -> list:
    """
    Generates output CSS file with light and dark schemes for each collection in the `collections:dict`.
    """

    lines = []
    
    open_string = ":root {\n"
    close_string = "}"
    light = []
    dark = []
    open_dark = "\t@media (prefers-color-scheme: dark) {\n"
    close_dark = "\t}\n"

    lines.append(open_string)

    for collection in collections:

        dark_layers = []
        dark_values = []

        for color in collections[collection]:
            if color.get("light"):
                c = color["light"]
                hsla_string = f'--{color["name"]}: hsla({c["hsla"][0]}, {c["hsla"][1]}%, {c["hsla"][2]}%, {c["hsla"][3]});' 
                string = "\t" + hsla_string + "\n"
                light.append(string)
            if color.get("dark"):
                if color["layer"] == 0:
                    c = color["dark"]
                    hsla_string = f'--{color["name"]}: hsla({c["hsla"][0]}, {c["hsla"][1]}%, {c["hsla"][2]}%, {c["hsla"][3]});' 
                    string = "\t\t" + hsla_string + "\n"
                    dark.append(string)
                if color["layer"] != 0:
                    c = color["dark"]
                    hsla_string = f'hsla({c["hsla"][0]}, {c["hsla"][1]}%, {c["hsla"][2]}%, {c["hsla"][3]});' 
                    dark_layers.append(f'--{color["name"]}: ')
                    dark_values.append(hsla_string)


            dark_zipped = list(zip(dark_layers, dark_values[::-1]))
        
        for c in dark_zipped:
            string = f'{c[0]}{c[1]}'
            dark.append("\t\t" + string + "\n")
        

    for line in light:
        lines.append(line)
    
    lines.append(open_dark)

    for line in dark:
        lines.append(line)

    lines.append(close_dark)

    lines.append(close_string)

    with open("./source/_output_colors.scss", "w") as f:
        for line in lines:
            f.write(line)

    return lines

# DEPRECATED
def generate_layers(collections: dict) -> list:

    layers = []
    names = []

    for collection in collections:
        for color in collections[collection]:
            if color.get("light"):
                c = color["light"]

                layer_name = f'{collection}-layer-{color["layer"]}'

                if c["light_text"]:
                    text_color = "\tcolor: var(--text-color-light);\n"
                else:
                    text_color = "\tcolor: var(--text-color-dark);\n"

                # if color["layer"] == 0:
                #     text_color = "\tcolor: var(--text-color-white);\n"

                if collection == "grayscale" and color["layer"] == 0:
                    text_color = "\tcolor: var(--text-color-black);\n"

                layer = "." + layer_name + " {\n"
                bg_color = f'\tbackground-color: var(--{color["name"]});\n'
                close_line = "}\n"

                layers.append(layer + text_color + bg_color + close_line)
                names.append(layer_name)


    with open("./source/_output_layers.scss", "w") as f:
        for line in layers:
            f.write(line)

    print(names)
    
    return names

# DEPRECATED
def render_html_swatches(names:list):
    html_strings = []

    for name in names:
        html_string = f'''
<div class="{name} colorize__demo_card">
    <h1>Demo lorem ipsum</h1>
    <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Odit vitae minus, quaerat vero sit sed rem debitis distinctio hic laboriosam optio error! Incidunt corporis veniam asperiores modi ducimus, inventore sit!</p>
    <p class="small-paragraph">Lorem ipsum dolor sit, amet consectetur adipisicing elit. Odit vitae minus, quaerat vero sit sed rem debitis distinctio hic laboriosam optio error! Incidunt corporis veniam asperiores modi ducimus, inventore sit!</p>
</div>'''
        html_strings.append(html_string)

    with open("./core/templates/__colorize_generated_stand.html", "w") as f:
        for element in html_strings:
            f.write(element + "\n")
