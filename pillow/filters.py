from PIL import Image

# Load an image
image = Image.open("landscape.png")

# Display the image
image.show()

# Display some information about the image
print(f'Format: {image.format}, Size: {image.size}, Mode: {image.mode}')
xsize=image.size[0]
ysize=image.size[1]
new_image = Image.new('RGB', (xsize, ysize))
pixels = new_image.load()
for x in range(xsize):
    for y in range(ysize):
        pixels[x,y] = 0,image.getpixel((x,y))[1],image.getpixel((x,y))[2]
new_image.show()


new_image2 = Image.new('RGB', (xsize, ysize))
pixels = new_image2.load()
for x in range(xsize):
    for y in range(ysize):
        pixels[x,y] = sum(image.getpixel((x,y)))//3,sum(image.getpixel((x,y)))//3,sum(image.getpixel((x,y)))//3
new_image2.show()


new_image3 = Image.new('RGB', (xsize, ysize))
pixels = new_image3.load()
for x in range(xsize):
    for y in range(ysize):
        pixels[x,y] = image.getpixel(((xsize-x-1),(y)))

new_image3.show()