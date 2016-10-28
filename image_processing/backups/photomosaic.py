from PIL import Image
import image_slicer
from os import listdir
from os.path import isfile, join

# directory in where the image we want to use is
mypath = '/Users/Claire/mosaic/'


def SplitImage(img):

    tiles = image_slicer.slice(img, 4, save=False)
    image_slicer.save_tiles(tiles, directory=mypath, prefix='slices')
    # stores a list of sorted tiles in variable 'onlyfiles' with file
    # extension '.png'
    files = [f for f in listdir(mypath) if isfile(
        join(mypath, f)) if f.endswith(".png")]
    files.sort()
    # a list of tuples containging rgb values are stored in variable 'rgbtiles'
    rgb = most_frequent_color(files)
    # returns a list of rgb values of tiles in tuples
    images_rgb = ResizeImg(files[0])

    # list of rgb of tiles and list of rgb of mosaic images
    return rgb, images_rgb


def most_frequent_color(lst):
    # Finds most frequently occuring color
    # in each image in the list
    rgb = []
    for image in lst:
        img = Image.open(image)
        w, h = img.size
        pixels = img.convert('RGB').getcolors(w * h)
        most_frequent_pixel = pixels[0]
        for count, color in pixels:
            if count > most_frequent_pixel[0]:
                most_frequent_pixel = (count, color)
        rgb += [most_frequent_pixel[1]]
    return rgb


def ResizeImg(image):
    # Resizes all images in lst to the size of
    # the split tiles of the original image
    # and give back most frequent color of each image
    lst = [f for f in listdir(mypath) if isfile(
        join(mypath, f)) if f.endswith(".png")]
    lst2 = []
    i = Image.open(image)
    w, h = i.size

    for im in lst:
        lst2 += most_frequent_color([im])
        img = Image.open(im)
        img = img.resize((w, h), Image.ANTIALIAS)
        img.save(mypath + im)

    return lst2


def grid(img, tile, lst):
    # Puts images into mosaic
    tile = Image.open(tile)
    w, h = tile.size
    original = Image.open(img)
    total_w, total_h = original.size
    x = 0
    y = 0
    result = Image.new('RGB', (total_w, total_h))  # new image
    for t in nj:
        img = imageslst[t[1]]
        img = Image.open(img)
        if x < total_w and y < total_h:
            result.paste(img, (x, y))
            x += w
        elif y < total_h:
            x = 0
            y += h
            result.paste(img, (x, y))
            x += w

    result.save(mypath + 'final.jpeg')
    result.show()
