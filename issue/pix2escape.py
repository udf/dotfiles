# hacky script that attempts to make "terminal art" using escape codes

from PIL import Image
import math
# fucking stupid americans
import colorsys as coloursys
import collections

p_dark  = [0x000000, 0xaa0000, 0x00aa00, 0xaa5500, 0x0000aa, 0xaa00aa, 0x00aaaa, 0xaaaaaa]
p_light = [0x555555, 0xFF5555, 0x55FF55, 0xFFFF55, 0x5555FF, 0xFF55FF, 0x55FFFF, 0xFFFFFF]

p_off = {}
for i, col in enumerate(p_dark):
    p_off[col] = i
for i, col in enumerate(p_light):
    p_off[col] = i + 8

def get_esc(colour, fore=True):
    colour = p_off[colour]
    return "{};{}".format(
        "1" if colour > 7 else "22",
        (30 if fore else 40) + colour % 8
    )

def get_esc_str(codes):
    if isinstance(codes, collections.Iterable) and not isinstance(codes, str):
        codes = ';'.join(codes)
    return '\\e[{}m'.format(codes)

def get_pixel(image, x, y):
    try:
        c = image.getpixel( (x, y,) )
        return c[0] << 16 | c[1] << 8 | c[2]
    except:
        return 0

def get_char(top, bottom):
    top_is_bright = top > 7
    bottom_is_bright = bottom > 7

    if top == bottom:
        if top_is_bright:
            return get_esc_str(get_esc(top, True)), '█'
        else:
            return get_esc_str(get_esc(top, False)), ' '
    elif top_is_bright and not bottom_is_bright:
        return get_esc_str([get_esc(top, True), get_esc(bottom, False)]), '▀'
    else:
        return get_esc_str([get_esc(top, False), get_esc(bottom, True)]), '▄'

im = Image.open('karen.png')

last_top = None
last_bottom = None
last_char = None
with open('out.txt', 'w') as file:
    for y in range(0, im.height, 2):
        for x in range(im.width):
            top = get_pixel(im, x, y)
            bottom = get_pixel(im, x, y+1)
            if top != last_top or bottom != last_bottom:
                esc, last_char = get_char(top, bottom)
                file.write(esc)
            file.write(last_char)

            last_top = top
            last_bottom = bottom
        file.write('\n')