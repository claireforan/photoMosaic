from PIL import Image
import image_slicer
from os import listdir
from os.path import isfile, join
from ColourCost import *
from mosaic1 import *
from get_rgb import *

mypath = '/Users/alessianardotto/Numberjack/Numberjack/insight-project/'


def SplitImage(img, N):
    im = Image.open(img)
    imgwidth, imgheight = im.size
    # Barry
    if imgwidth > imgheight:
        h = imgheight - N * int(imgheight // N)
        print("h = ", h)
        resized = im.crop((0, 0, imgheight - h, imgheight - h))
        # Image.ANTIALIAS

    elif imgwidth < imgheight:
        w = imghwidth - N * int(imgwidth // N)
        print("w =", w)
        resized = im.crop((0, 0, imgwidth - w, imgwidth - w))

    elif imgwidth == imgheight:
        h = imgheight - N * int(imgheight // N)
        resized = im.crop((0, 0, imgheight - h, imgheight - h))
    resized.save(mypath + "resized.jpeg")

    im2 = Image.open(mypath + "resized.jpeg")
    w2, h2 = im2.size

    rgb_values = get_rgb('resized.jpeg', N, w2, h2)

    rgbimg = ResizeImg(w2 // N)
    # a list of tuples containging rgb values are stored in variable 'rgbimg'
    # returns a list of rgb values in tuples

    return rgb_values, rgbimg


def most_frequent_color(lst, folder):
    # Finds most frequntly occuring color
    # in each image in the list

    rgb = []
    for image in lst:
        img = Image.open(mypath + folder + image)
        w, h = img.size
        pixels = img.convert('RGB').getcolors(w * h)
        most_frequent_pixel = pixels[0]
        for count, color in pixels:
            if count > most_frequent_pixel[0]:
                most_frequent_pixel = (count, color)
        rgb += [most_frequent_pixel[1]]
        print(image, ":", most_frequent_pixel[1])
    return rgb


def ResizeImg(tileWidth):
    # Resizes all images in lst to the size of
    # the to chosen width and height of tiles of the original image
    # returns list of tuples containing rgb values
    print(tileWidth)
    lst = [f for f in listdir(mypath + "pictures/") if isfile(
        join(mypath + "pictures/", f)) if not f.endswith('.DS_Store')]
    lst.sort()
    print("Images Before:", lst)
    lst2 = []

    for im in lst:
        lst2 += most_frequent_color([im], 'pictures/')
        img = Image.open(mypath + "pictures/" + im)
        # resizes images
        img = img.resize((tileWidth, tileWidth))
        # saves resized images in mypath
        img.save(mypath + 'pictures/' + im)

    return lst2


def grid(nj, orgimage):

    lst = [f for f in listdir(mypath + "pictures/") if isfile(
        join(mypath + "pictures/", f)) if f != '.DS_Store']
    lst.sort()
    print("Images:", lst)
    tile = Image.open(mypath + "pictures/" + lst[0])
    w, h = tile.size  # width and height of tile
    print(w, h)
    orgimage = Image.open(orgimage)
    total_w, total_h = orgimage.size
    print(total_w, total_h)
    x = 0
    y = 0
    t = 0
    result = Image.new('RGB', (total_w, total_h))  # new image
    print(nj)
    while y + h <= total_h and t < len(nj):
        x = 0
        while x + w <= total_w:
            img = lst[nj[t][1]]
            im = Image.open(mypath + "pictures/" + img)
            result.paste(im, (x, y))
            t += 1
            x += w
        y += h

    result.save(mypath + 'final.jpeg')
    result.show()

si = SplitImage('me.jpg', 8)
grid(Final(si), 'resized.jpeg')
