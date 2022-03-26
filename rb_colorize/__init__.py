from config import settings
from previews.css import render_css_colors
from previews.generate_preview import index_html

# from tools.generate_swatches_list import generate_swatches_list
# from tools.normalize_color import degree_correction

names = settings["COLLECTIONS"]


# def swatcher(
#     hue: int,
#     steps: int,
#     saturation = 100,
#     lightness = 100,
#     opacity = 1,
#     name = "main",
#     detailed = True,
#     dark_desaturate = 5,
#     ) -> dict:

#     params = {
#         "hue" : hue,
#         "steps" : steps,
#         "saturation" : saturation,
#         "lightness" : lightness,
#         "opacity" : opacity,
#         "detailed" : detailed,
#         "dark_desaturate" : dark_desaturate,
#     }


#     if steps > 100:
#         steps = 100
    
#     if steps < 0:
#         steps = 1
    
#     if saturation > 100:
#         saturation = 100
    
#     if saturation < 0:
#         saturation = 0
    
#     if lightness > 100:
#         lightness = 100
    
#     if lightness < 0:
#         lightness = 0

#     hue = degree_correction(hue)
#     # second = degree_correction(hue-120)
#     # third = degree_correction(hue+120)

    
#     palettes = {}
    
#     for palette in names:
#         palettes[palette] = generate_swatches_list(**params, name=palette)

#     # GENERATE GRAYSCALE IF THE ORIGINAL WAS NOT GRAY
#     if saturation != 0:
#         palettes["grayscale"] = generate_swatches_list(0, steps, 0, lightness, opacity, "grayscale", True)

    
#     return palettes
    
#     # curl -H "Content-Type: application/json" -X POST -d '{"hue": 202, "steps": 7, "saturation": 90, "lightness": 90}' http://localhost:5005/colorize/api > dump.json


if __name__ == "__main__":
    
    # import json

    # jsonified = json.dumps(swatcher(201, 5), sort_keys=True, indent=4)

    # print(jsonified)

    # with open("../output/colors.json", "w") as f:
    #     f.write(jsonified)

    render_css_colors(341)
    index_html()