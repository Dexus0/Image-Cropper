from PIL import Image
from time import process_time
from os import path
start = process_time()


im = Image.open(input('')).convert('RGB')

img = im.load()


crop_pixels = []
crop_colors = ((255, 255, 255), (0, 0, 0))
xsize, ysize = im.size

top, bottom = 0, ysize
left, right = 0, xsize

lisx = list(range(xsize))
lisy = list(range(ysize))
for y in range(ysize):
    crop_pixels.append([])
    for x in range(xsize):
        if img[x, y] in crop_colors:
            crop_pixels[y].append(x)


for y in range(ysize):
    if y <= round(ysize/2):
        if crop_pixels[y] == lisx:
            top = y
    elif y < bottom and crop_pixels[y] == lisx:
        bottom = y


crop_pixels = []
for x in range(xsize):
    crop_pixels.append([])
    for y in range(ysize):
        if img[x, y] in crop_colors:
            crop_pixels[x].append(y)


for x in range(xsize):
    if x <= round(xsize/2):
        if crop_pixels[x] == lisy:
            left = x

    elif x < right and crop_pixels[x] == lisy:
        right = x

end = process_time()
print('Processing took:', round(end - start, 2), 'seconds', end='\n\n')

im = im.crop((left + 1, top + 1, right, bottom))
if input('Want to save image?\n Yes or No\n') == 'Yes':

    im.save("upisidedown-'bar'.png")

im.show()