import math
from math import sqrt
from tools.color import Color, degree_correction, normalize_to_hundred
from config import settings

dark_desaturate = settings["DARK_DESATURATE"]



def create_log_scale(num_steps, start=0):
    if not 5 <= num_steps <= 17:
        raise ValueError("Number of steps must be between 5 and 17")
    if not 0 <= start <= 50:
        raise ValueError("Start value must be between 0 and 50")

    result = [start]
    base = math.exp(math.log(100) / (num_steps - 1))

    for i in range(1, num_steps):
        next_value = start + math.ceil(math.pow(base, i) - 1)
        result.append(next_value)

    return result

def step(x):
    """
    Calculate lightness value for a given number
    """
    return 1 - sqrt(1 - x * x)

def build_steps(n=10):
    n = n + 2
    step_size = 1 / n
    nums = []
    x = step_size
    for _ in range(1, n+1):
        nums.append(x)
        x = x + step_size

    return nums[1:-1]


def build_gradient(steps) -> tuple:

    light = set()
    dark = set()

    # generate steps for the LIGHT scheme
    for i in steps:
        x = int(100 - step(i) * 100)
        light.add(x)

    # generate steps for the DARK scheme
    for i in steps:
        x = int(step(i) * 100)
        x = x + settings["DARK_INCREASE_BRIGHTNESS"]
        dark.add(x)

    light_list = list(light)
    light_list.sort(reverse=True)
    dark_list = list(dark)
    dark_list.sort()

    return light_list, dark_list



def get_gradient(steps=12, light_initial=100, dark_initial=0) -> tuple:
    """
    Return `light` and `dark` gradients (lists of `int` lightness values)
    """
    steps = build_steps(steps)
    gradient = build_gradient(steps)

    return gradient



class Collection:

    def __init__(
        self,
        name: str,
        h: int,
        s: int = 50,
        l: int = 50,
        a=1,
        objects: bool = True,
        steps: int = 10,
        light_initial: int = 0,
        dark_initial: int = 100
    ):
        # self.gradient = get_gradient(steps)
        self.gradient = get_gradient(steps, light_initial, dark_initial)
        self.name = name.lower()
        self.h = degree_correction(h)
        self.s = normalize_to_hundred(s)
        self.l = normalize_to_hundred(l)
        self.a = a
        self.light_objects = self.get_collection(gradient=self.gradient[0])
        self.dark_objects = self.get_collection(gradient=self.gradient[1], dark=True)
        self.light = self.get_collection(
            gradient=self.gradient[0], objects=False)
        self.dark = self.get_collection(
            gradient=self.gradient[1], objects=False, dark=True)
        self.objects = objects
        self.steps = steps
        # print('collection gradient', self.gradient)

    def get_collection(self, gradient, objects=True, dark=False):
        collection = []
        for n in gradient:

            saturation = self.s
            if dark:
                saturation = self.s - dark_desaturate if self.s > dark_desaturate else self.s

            c = {
                "h": self.h,
                "s": saturation,
                "l": n,
            }
            color = Color(**c)
            color.set_order((gradient.index(n)) + 1)
            color.set_name(self.name)

            if objects:
                collection.append(color.get_object())
            else:
                collection.append(color)

        return collection

    def __repr__(self) -> str:
        scale = get_gradient(self.steps)
        return f'<Collection {self.name}, light: {scale[0]} dark: {scale[1]}>'
