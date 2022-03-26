from config import color_settings, file_paths, settings

def generate_basic_css():
    template = ':root {\n' + \
    f'''
    --text-color: {color_settings["TEXT_BLACK"]};
    --text-color-dark: {color_settings["TEXT_BLACK"]};
    --text-color-light: {color_settings["TEXT_WHITE"]};
    --text-color-white: {color_settings["TEXT_WHITE"]};
    --text-color-black: {color_settings["TEXT_BLACK"]};
    --bg-color: {color_settings["BACKGROUND_COLOR_LIGHT"]};
    --font-display: {settings["FONT"]};

    @media (prefers-color-scheme: dark) ''' + ' {\n' + \
    f'''
        --text-color: {color_settings["TEXT_WHITE"]};
        --text-color-dark: {color_settings["TEXT_WHITE"]};
        --text-color-light: {color_settings["TEXT_BLACK"]};

        --bg-color: {color_settings["BACKGROUND_COLOR_DARK"]};
        ''' + "\n" + \
    '''}
    }

    * {
        box-sizing: border-box;
        margin: 0;
        margin: 0;
        font-family: var(--font-display);
    }

    body {
        background-color: var(--bg-color);
        color: var(--text-color);
    }
    ''' + \
    '''
    .colorize__demo_card {
        padding: 16px;
    }
    
    '''

    with open(f'{file_paths["PATH"]}{file_paths["BASIC_CSS"]}', "w") as f:
        f.write(template)

    return True

def index_html():
    """Renders index.html"""

    # file_path = f'{file_paths["PATH"]}{file_paths["INDEX_HTML"]}'

    with open(f'{file_paths["PATH"]}{file_paths["CARDS_HTML"]}', "r") as f:
        cards = f.read().replace('\n', '')

    with open(f'{file_paths["PATH"]}{file_paths["CARDS_LAYERED_HTML"]}', "r") as f:
        layers = f.read().replace('\n', '')

    template = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="static/style.css">
    <title>Colorize preview</title>
</head>
<body>
    {cards}
    {layers}
</body>
</html>
'''

    with open(f'{file_paths["PATH"]}{file_paths["INDEX_HTML"]}', "w") as f:
        f.write(template)

    return True


def render_html_layered(collections:dict) -> list:

    lines = []
    r_collections = {}

    for collection in collections:

        r_collections[collection] = []

        for color in collections[collection]:
            if color.get("light"):
                layer_name = f'{collection}-layer-{color["layer"]}'
                r_collections[collection].append(layer_name)

    for r in r_collections:
        string = divs_sum_recursive(r_collections[r])
        lines.append(string)

    with open("./core/templates/__colorize_generated_stand-layers.html", "w") as f:
        for line in lines:
            f.write(line + "\n")

def divs_sum_recursive(input_list):
    # Base case
    if input_list == []:
        return ""

    # Recursive case
    # Decompose the original problem into simpler instances of the same problem
    # by making use of the fact that the input is a recursive data structure
    # and can be deﬁned in terms of a smaller version of itself
    else:
        head = input_list[0]
        smaller_list = input_list[1:]
        string = f'<div class="{head} colorize__demo_card"><code class="small-paragraph">Class: {head}</code>{divs_sum_recursive(smaller_list)}</div>'
        return string

if __name__ == "__main__":

    # swatches = ["layer-1","layer-2","layer-3","layer-4","layer-5","layer-6"]
    # print(divs_sum_recursive(swatches))

    generate_basic_css()
    index_html()