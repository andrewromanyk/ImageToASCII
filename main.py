from PIL import Image

def ImageToAscii(image_name, scale, destination = 'ImageToAscii.txt'):
    image = Image.open(image_name).convert('RGB')
    width, height = image.size
    width, height = width//scale, height//scale

    resized_image = image.resize((width, height))
    resized_image = resized_image.load()

    asciiImage = [['*']*width for i in range(height)]

    for i in range(height):
        for j in range(width):
            brightness = sum(resized_image[i, j])//3
            if brightness <= 32: char = '⠀⠀'
            elif brightness <= 64: char = '⠀⠐'
            elif brightness <= 96: char = '⠀⠌'
            elif brightness <= 128: char = '⠀⠜'
            elif brightness <= 160: char = '⠀⠝'
            elif brightness <= 192: char = '⠀⠞'
            elif brightness <= 224: char = '⠀⠻'
            elif brightness <= 255: char = '⠀⠿'
            asciiImage[j][i] = char

    result = ''
    for line in asciiImage:
        result += ''.join(line) + '\n'

    with open(destination, 'w', encoding="utf-8") as file:
        file.write(result)

    return result

def main():
    print(ImageToAscii("test.png", 15))

if __name__ == "__main__":
   main()

