from PIL import Image
from time import process_time
from os import path
start = process_time()

# inp = input('enter the file path\ntype exit to exit the program\n')
#
# if inp.lower() == 'exit':
#     exit()
# if not inp:
#     inp = "upisidedown-'bar'.png"

inp = "upisidedown-'bar'.png"
im = Image.open(inp).convert('RGB')

img = im.load()


crop_pixels = []
crop_colors = ((255, 255, 255), (0, 0, 0))
xsize, ysize = im.size

top, bottom = 0, ysize
left, right = 0, xsize

lisx = list(range(xsize))
lisy = list(range(ysize))


y = 0

for _ in range(ysize):
    crop_pixels.append([])


while y < ysize:
    for x in range(xsize):
        if img[x, y] in crop_colors:
            crop_pixels[y].append(x)
        else:
            crop_pixels[y].clear()
            if y < ysize//2:
                y = ysize//2
            break
    y += 1


for y in range(ysize):
    if y <= ysize//2:
        if crop_pixels[y]:
            top = y
    elif y < bottom and crop_pixels[y]:
        bottom = y
        break


crop_pixels = []
for _ in range(xsize):
    crop_pixels.append([])

x = 0

while x < xsize:
    for y in range(ysize):
        if img[x, y] in crop_colors:
            crop_pixels[x].append(y)
        else:
            crop_pixels[x].clear()
            if x < xsize//2:
                x = xsize//2
            break
    x += 1


for x in range(xsize):
    if x <= xsize//2:
        if crop_pixels[x]:
            left = x
    elif x < right and crop_pixels[x]:
        right = x

end = process_time()
print('Processing took:', round(end - start, 2), 'seconds', end='\n\n')

im = im.crop((left + 1, top + 1, right, bottom))
im.show()
if input('Want to save image?\nYes or No\n').lower() == 'yes':

    im.save("cropped.png")