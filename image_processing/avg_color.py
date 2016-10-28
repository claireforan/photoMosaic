from PIL import Image

def average_rgb(image):
    '''
    Calculates the average RGB of an image.
    Returns 3-tuple (R, G, B)
    '''
    image = Image.open(image)
    average_red = 0
    average_green = 0
    average_blue = 0
    maxcolors = image.size[0]*image.size[1]
    colors = image.getcolors(maxcolors)
    for color in colors:
        average_red += color[1][0] * color[0]
        average_green += color[1][1] * color[0]
        average_blue += color[1][2] * color[0]
    average_red //= maxcolors
    average_green //= maxcolors
    average_blue //= maxcolors
    return (average_red, average_green, average_blue)

print(average_rgb('/Users/alessianardotto/forest.jpg'))