from PIL import Image
import random
import os

w = int(input("Width: "))
h = int(input("Height: "))
code = random.randint(0,1000)

img = Image.new('RGB', (w, h), "black")
img.save(f'Generated/image_{code}.png')

pic = Image.open(f'Generated/image_{code}.png')
count = 0

r = random.randint(0, 255)
g = random.randint(0, 255)
b = random.randint(0, 255)

for x in range(pic.size[0]):
    for y in range(pic.size[1]):
        if count == 64:
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            count = 0

        pic.putpixel((x, y), (r, g, b))
        count += 1
        

pic.save(f'Generated/image_{code}.png')