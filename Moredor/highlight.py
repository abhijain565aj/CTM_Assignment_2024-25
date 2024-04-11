import sys
from PIL import Image
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True


def find_color(image_path, r, g, b):
    range_val = 2
    try:
        r, g, b = int(r), int(g), int(b)
        if not (0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255):
            print(
                "Invalid arguments. Syntax is ./findColorin [IMAGE] [R VALUE] [G VALUE] [B VALUE]")
            return
    except ValueError:
        print(
            "Invalid arguments. Syntax is ./findColorin [IMAGE] [R VALUE] [G VALUE] [B VALUE]")
        return

    try:
        image = Image.open(image_path)
    except FileNotFoundError:
        print("Image file not found.")
        return

    width, height = image.size
    for x in range(width):
        for y in range(height):
            pixel = image.getpixel((x, y))
            if (
                (r - range_val <= pixel[0] <= r + range_val) and
                (g - range_val <= pixel[1] <= g + range_val) and
                (b - range_val <= pixel[2] <= b + range_val)
            ):
                image.putpixel((x, y), (0, 0, 0))
            else:
                image.putpixel((x, y), (255, 255, 255))

    print("Saving to output.png")
    image.save('output.png')


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print(
            "Invalid number of arguments. Syntax is ./findColorin [IMAGE] [R VALUE] [G VALUE] [B VALUE]")
    else:
        image_path, r, g, b = sys.argv[1:]
        find_color(image_path, r, g, b)
