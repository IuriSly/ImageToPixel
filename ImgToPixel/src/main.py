from PIL import Image

def open_image(path):
    newImage = Image.open(path)
    return newImage

def get_pixel(image, i, j):
    width, height = image.size
    if i > width or j > height:
        return None

    pixel = image.getpixel((i, j))
    return pixel

def write_pixel_colors_and_coordinates(img):
    width, height = img.size
    f = open("pixel-data.txt", "w+")
    for i in range(height):
        for j in range(width):
            print("i: " + str(i) + " j: " + str(j))
            p = get_pixel(img, j, i)
            red = p[0]
            green = p[1]
            blue = p[2]
            line = "; colors: " + str(red) + " " + str(green) + " " + str(blue) + "\n"
            f.write(line)
            line = "mov dword ptr[esi], " + str(i) + "\n"
            f.write(line)
            line = "mov dword ptr[esi+4], " + str(j) + "\n"
            f.write(line)
    f.close()

location = input("Image location? => ")
print(location)
image = open_image(location)
write_pixel_colors_and_coordinates(image)
