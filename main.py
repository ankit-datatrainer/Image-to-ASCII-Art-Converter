from PIL import Image
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

def resize_image(image, new_width=100):
    """Resizes an image while maintaining aspect ratio."""
    width, height = image.size
    ratio = height / width / 2
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image

def grayify(image):
    """Converts an image to grayscale."""
    return image.convert("L")

def pixels_to_ascii(image):
    """Converts pixels to a string of ASCII characters."""
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel // 25] for pixel in pixels])
    return characters

def main(image_path, new_width=100):
    """Main function to convert an image to ASCII art."""
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(f"Unable to open image file {image_path}.")
        print(e)
        return

    resized_image = resize_image(image, new_width)

    grayscaled_image = grayify(resized_image)

    new_image_data = pixels_to_ascii(grayscaled_image)

    pixel_count = len(new_image_data)
    ascii_image = "\n".join(
        new_image_data[i:(i + new_width)] for i in range(0, pixel_count, new_width)
    )

    print(ascii_image)

    with open("ascii_image.txt", "w") as f:
        f.write(ascii_image)
    print("ASCII art saved to ascii_image.txt")

if __name__ == '__main__':
    main('ankit-profile.png')
