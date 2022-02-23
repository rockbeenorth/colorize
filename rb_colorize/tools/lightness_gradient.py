import math

def step(x):
    return 1 - math.sqrt(1 - x * x)


def build_gradient(steps):

    light = set()
    dark = set()

    for i in steps:
        x = 100 - round(step(i) * 100, 0)
        light.add(x)

    for i in steps:
        x = round(step(i) * 100, 0)
        dark.add(x)

    light_list = list(light)
    light_list.sort(reverse=True)

    dark_list = list(dark)
    dark_list.sort()

    return light_list, dark_list

def build_steps(n=12):
    step_size = 1 / n
    nums = []
    x = 0
    for i in range(0, n):
        if x == 0:
            nums.append(0)

        nums.append(x + step_size)
        x = x + step_size

    return nums

if __name__ == "__main__":
    rez = build_gradient(build_steps(12))
    print(rez[0], len(rez[0]))
    print(rez[1], len(rez[1]))