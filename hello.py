from PIL import Image

file = open("lebron.txt", "w")

img = Image.open("lebron.png")
img = img.convert("RGB")

w = img.width
h = img.height

for y in range(h):
    for x in range(w):
        px = img.getpixel([x,y])
        bright = px[0] + px[1] + px[2]
        if bright == 0:
            file.write("#")
        elif bright < 100:
            file.write("X")
        elif bright < 200:
            file.write("%")
        elif bright < 300:
            file.write("&")
        elif bright < 400:
            file.write("*")
        elif bright < 500:
            file.write("+")
        elif bright < 600:
            file.write("/")
        elif bright < 700:
            file.write("(")
        else:
            file.write("'")
    file.write("\n")

