from random import choice, shuffle, seed
import string
from functools import reduce
from operator import add

seed(0)

#fn = "muc"
#n = 2

#fn = "krava"
#n = 5

fn = "zadnji"
n = 6

vrstice = [x.strip("\n") for x in  open(fn + ".txt")]

w, h = max(map(len, vrstice)), len(vrstice)

hh = (h + n - 1) // n
ww = (w + n - 1) // n
print(hh, ww)
pad_hor = " " * (n * ww - h)
pad_ver = [" " * n * ww] * (ww * n - h)

vrstice = [x + pad_hor for x in vrstice] + pad_ver

allowed = string.ascii_letters + string.digits
print(allowed)
def rl():
    return choice(allowed)

sides = sorted({"".join(rl() for _ in range(n))
     for _ in range(10 * (ww + 1) * (hh + 1))})
shuffle(sides)
sides = iter(sides)


d = [[rl() for _ in range(ww + 1)] for _ in range(hh + 1)]
vers = [[d[row][col] + next(sides) + d[row + 1][col]
         for col in range(ww + 1)]
        for row in range(hh)]
hors = [[d[row][col] + next(sides) + d[row][col + 1]
         for col in range(ww)]
        for row in range(hh + 1)]

def tile(x, y):
    xs = slice(x * n, x * n + n)
    left, right = vers[y][x:x + 2]
    print(y * n + n - 1, len(vrstice))
    return [hors[y][x],
            *[left[yi] + vrstice[y * n + yi][xs] + right[yi] for yi in range(n)],
            hors[y + 1][x]]

def obrati(kos):
    vsi_obrati = []
    for i in range(2):
        for j in range(4):
            vsi_obrati.append(kos)
            kos = ["".join(v[i] for v in kos)[::-1] for i in range(len(kos))]
        kos = kos[::-1]
    return vsi_obrati

tiles = [[tile(x, y) for x in range(ww)] for y in range(hh)]
print("\n".join(repr(x) + "," for x in tiles))

flat_tiles = reduce(add, tiles)
shuffle(flat_tiles)
open(fn + "-puzzle.txt", "wt").write(
    "\n\n".join("\n".join(choice(obrati(tile))) for tile in flat_tiles))
