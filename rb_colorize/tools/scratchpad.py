from tools.color import Color

THRESHOLD = 140

from tools.color import Color

above = []
below = []
zero = []

lumes = []
diffs = []

for i in range(0, 360):
    c = Color(i, 80, 50)
    lume = int(c.luminocity)
    diff = lume - THRESHOLD
    lumes.append(lume)
    diffs.append(diff)

    if diff < 0:
        below.append(c)
    elif diff > 0:
        above.append(c)
    else:
        zero.append(c)

    print(i, c.name, f'\t{lume}', f'\t{diff}')

print('above', len(above))
print('below', len(below))
print('zero', len(zero))

print(min(lumes))
print(max(lumes))
print(min(diffs))
print(max(diffs))
