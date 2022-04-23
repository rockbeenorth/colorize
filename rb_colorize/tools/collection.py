from tools.color import Color
from tools.lightness_gradient import get_gradient

from config import settings

dark_desaturate = settings["DARK_DESATURATE"]


def generate_collection(
        h: int,
        s: int,
        gradient: list, # gradient is a list of integers containing lightness steps (e.g. [100, ... , 0])
        a=1,
        name="core",
        json_mode=False
) -> list:
    """
    Return a collection for a given lightness gradient (list).
    """

    collection = []

    for n in gradient:
        c = {
            "h": h,
            "s": s,
            "l": n,
        }
        color = Color(**c)
        color.set_order(gradient.index(n) + 1)
        color.set_name(name)

        if json_mode:
            collection.append(color.get_json())

        else:
            collection.append(color)

    return collection


def get_collection(
        h: int,
        s=100,
        name="core"):

    gradient = get_gradient()
    light = gradient[0]
    dark = gradient[1]

    palette = {
        "light": generate_collection(h, s, light, name=name),
        "dark": generate_collection(h, s - dark_desaturate, dark, name=name)
    }

    return palette


def get_collection_json(
        h: int,
        s=100,
        a=1,
        name="core"):

    gradient = get_gradient()
    light = gradient[0]
    dark = gradient[1]

    palette = {
        "light": generate_collection(h, s, light, name=name, json_mode=True),
        "dark": generate_collection(h, s - dark_desaturate, dark, name=name, json_mode=True)
    }

    return palette


if __name__ == "__main__":
    x = get_collection(220, 90, name="arte")
    print(x)
    for k, v in x.items():
        # print("\n", k, v)
        for color in v:
            print(color.order, color.hsl, color.bright_text, k)
