from PIL import Image


def get_rgb(image, N, x, y):

    div = x // N
    rgbimg = []
    ytile = 0

    while ytile < y:
        xtile = 0
        while xtile < x:
            r, g, b = get_average_color(xtile, ytile, div, image)
            rgbimg += [(r, g, b)]
            xtile += div
        ytile += div
    return rgbimg


def get_average_color(x, y, n, image):
    """ Returns a 3-tuple containing the RGB value of the average color of the
    given square bounded area of length = n whose origin (top left corner) 
    is (x, y) in the given image"""

    image = Image.open(image).load()
    r, g, b = 0, 0, 0
    count = 0
    for s in range(x, x + n):
        for t in range(y, y + n):
            pixlr, pixlg, pixlb = image[s, t]
            r += pixlr
            g += pixlg
            b += pixlb
            count += 1
    return ((r // count), (g // count), (b // count))


# r, g, b = get_average_color(528,528,528,'resized.jpeg')
# print(r,g,b)
# print(get_rgb('resized.jpeg',16))
