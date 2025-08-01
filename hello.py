from PIL import Image

def asciiConvert(imageName):
    file = open("lebron.txt", "w")

    img = Image.open(imageName)
    img = img.convert("RGB")

    w = img.width
    h = img.height

    for y in range(h):
        for x in range(w):
            px = img.getpixel([x,y])
            bright = px[0] + px[1] + px[2]
            if bright == 0:
                file.write("@")
            elif bright < 100:
                file.write("%")
            elif bright < 200:
                file.write("X")
            elif bright < 300:
                file.write("k")
            elif bright < 400:
                file.write("l")
            elif bright < 500:
                file.write("/")
            elif bright < 600:
                file.write(";")
            elif bright < 700:
                file.write("'")
            else:
                file.write("`")
        file.write("\n")

if __name__ == '__main__':
    imageName = input("Enter the name of the image file you would like to convert to ASCII: ")
    asciiConvert(imageName)
    print("Your ASCII art has been created!")


