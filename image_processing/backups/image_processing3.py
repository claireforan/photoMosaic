from PIL import Image, ImageFilter
from os import listdir
from os.path import isfile, join
from ColourCost import *
from mosaic1 import *
from get_rgb import *

mypath = '/Users/alessianardotto/Numberjack/Numberjack/insight-project/'


def SplitImage(img, N):
    try:
        im = Image.open(img)
    except FileNotFoundError:
        print('Error opening main image')
        exit()
    imgwidth, imgheight = im.size
    # Barry
    if imgwidth > imgheight:
        diff = imgwidth - imgheight
        h = imgheight - N * int(imgheight // N)
        # resized = img.crop(((diff + h)//2,  h//2, imgheight + diff - h,imgheight - h//2))
        resized = im.crop((0, 0, imgheight - h, imgheight - h))

    elif imgwidth < imgheight:
        w = imgwidth - N * int(imgwidth // N)
        resized = im.crop((0, 0, imgwidth - w, imgwidth - w))

    elif imgwidth == imgheight:
        h = imgheight - N * int(imgheight // N)
        resized = im.crop((0, 0, imgheight - h, imgheight - h))

    print('MAIN IMAGE RESIZED')
    resized.save(mypath + "resized.jpeg")

    im2 = Image.open(mypath + "resized.jpeg")
    w2, h2 = im2.size
    print('CREATING TILES')
    rgb_values = get_rgb('resized.jpeg', N, w2, h2)
    # a list of tuples containging RGB values are stored in variable 'rgbimg'
    rgbimg = ResizeImg(w2 // N)
    # lists of tuples
    return rgb_values, rgbimg
    

def ResizeImg(tileWidth):
    # Resizes all images in lst to the size of
    # the split tiles of the original image and
    # returns list of tuples containing rgb values

    pictures = [f for f in listdir(mypath + "pictures/") if isfile(
        join(mypath + "pictures/", f)) if not f.endswith('.DS_Store')]
    pictures.sort()
    rgb_list = []
    print('RESIZING IMAGES')
    for im in pictures:
        try:
            img = Image.open(mypath + "pictures/" + im)
        except IOError:
            print('Problem opening %s' % (im))
            continue
        # resizes and saves images with the best quality as possible (100)
        img = img.resize((tileWidth, tileWidth), Image.ANTIALIAS)
        quality_val = 100
        img.save(mypath + 'pictures/' + im, subsampling = 0, quality = quality_val)
        # saves resized images in mypath   
        rgb_list += [(get_average_color(0, 0, tileWidth, mypath + 'pictures/' + im))]

    return rgb_list


def grid(nj, orgimage):
    # Grab all the file in the selected directory
    lst = [f for f in listdir(mypath + "pictures/") if isfile(
        join(mypath + "pictures/", f)) if f != '.DS_Store']
    print('SORTING NOW')
    # Sort the files
    lst.sort()
    print('SORTING DONE')
    tile = Image.open(mypath + "pictures/" + lst[0])
    # Get width and height of a tile
    w, h = tile.size 
    # opens and gets the dimensions of orgimage which is 'resized.jpeg'
    orgimage = Image.open(orgimage)
    total_w, total_h = orgimage.size
    x = 0
    y = 0
    t = 0
    # new image with same dimensions as 'resized.jpeg'
    result = Image.new('RGB', (total_w, total_h))  
    # print(nj)
    nj_len = len(nj)
    while y + h <= total_h and t < nj_len:
        x = 0
        while x + w <= total_w:
            img = lst[nj[t][1]]
            im = Image.open(mypath + "pictures/" + img)
            result.paste(im, (x, y))
            t += 1
            x += w
        y += h

    result.save(mypath + 'final.jpeg')
    # result.show()
    im2 = Image.open(mypath + 'resized.jpeg')
    im3 = im2.filter(ImageFilter.EDGE_ENHANCE_MORE)
    im3.save(mypath + 'fe.jpeg')
    # im3.show()
    res = Image.blend(result, im3, 0.3)
    res.save(mypath + 'filter.jpeg')
    res.show()

si = SplitImage('cat.jpg', 60)
grid(Final(si), 'resized.jpeg')
