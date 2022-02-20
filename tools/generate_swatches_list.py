from tools.color_conversions import hsl_to_rgb, rgb_to_hex
from tools.check_brightness import is_light_text
from tools.normalize_color import normalize_to_hundred, normalize_color, degree_correction

def generate_swatches_list(
        hue: int,
        steps: int,
        saturation = 100,
        lightness = 100,
        opacity = 1,
        name = "main",
        detailed = True,
        dark_desaturate = 5,
        ) -> list:
    """
Returns a collection of swatches. The number depends on a given `step` (how many swatches you want). We recommend 5-12 steps.

`step` is an integer, depends on `lightness` (which is 100% max.)
    """
    step_size = int(round(lightness / steps))

    collection = []
    
    # correct colors

    hue = degree_correction(hue)
    saturation = normalize_to_hundred(saturation)
    lightness = normalize_to_hundred(lightness)

    # generate swatches

    layer = 1
    

    for _ in range(steps):

        color = {}

        # Light - main collections
        
        if saturation < 0:
            saturation = 0

        hsla = (hue, saturation, lightness, opacity)
        rgb = hsl_to_rgb(hsla[0], hsla[1], hsla[2])
        hsl = hsla[0], hsla[1], hsla[2]
        
        color["light"] = {
            "hsla": hsla,
            "rgba": rgb + (opacity,),
            "hex": rgb_to_hex(*rgb),
            "light_text": is_light_text(hsl),
            }

        # Dark - main collections

        if saturation - dark_desaturate < 0:
            hsla = (hue, 0, lightness, opacity)
        else:
            hsla = (hue, saturation - dark_desaturate, lightness, opacity)

        if hsla[1] < 0:
            hsla[1] = 0

        hsl = hsla[0], hsla[1], hsla[2]
        rgb = hsl_to_rgb(*hsl)


        color["dark"] = {
            "hsla": hsla,
            "rgba": rgb + (opacity,),
            "hex": rgb_to_hex(*rgb),
            "light_text": is_light_text(hsl),
            }
        
        if detailed:
            variable_name = f"{name}-color-{layer}"
            color["name"] = variable_name
            color["layer"] = layer

        collection.append(color)
        
        layer += 1

        lightness = lightness - step_size

    # append absolute swatch

    absolute_color = {}

    hsla = normalize_color(hue)
    rgb = hsl_to_rgb(hsla[0], hsla[1], hsla[2])
    hsl = hsla[0], hsla[1], hsla[2]

    
    absolute_color["light"] = {
            "hsla": hsla,
            "rgba": rgb + (opacity,),
            "hex": rgb_to_hex(*rgb),
            "light_text": is_light_text(hsl),
    }


    hsla = hsla[0], hsla[1] - dark_desaturate, hsla[2], hsla[3]

    if hsla[1] < 0:
        hsla[1] = 0

    rgb = hsl_to_rgb(hsla[0], hsla[1], hsla[2])
    hsl = hsla[0], hsla[1], hsla[2]

    absolute_color["dark"] = {
            "hsla": hsla,
            "rgba": rgb + (opacity,),
            "hex": rgb_to_hex(*rgb),
            "light_text": is_light_text(hsl),
    }

    absolute_color["layer"] = 0

    if detailed:
        variable_name = f"{name}-color-0"
        absolute_color["name"] = variable_name

    collection.append(absolute_color)
    
    return collection

if __name__ == "__main__":

    x = generate_swatches_list(201, 6, 85, 90, .75)
    print(x)