import timeit
start = timeit.default_timer()
from PIL import Image
import image_slicer
from os import listdir
from os.path import isfile, join
from ColourCost import *
from mosaic1 import *
from function import *
mypath = '/home/gabrielle/mosaic/'

#split = timeit.default_timer()
def SplitImage(img, N):
    im = Image.open(img)
    imgwidth, imgheight = im.size
    # Barry
    if imgwidth > imgheight:
        diff = imgwidth - imgheight
        h = imgheight - N * int(imgheight // N)
        print("h = ", h)
        resized = im.crop((0, 0, imgheight - h, imgheight - h))

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
    #stopsplit = timeit.default_timer()
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
    return rgb


def ResizeImg(tileWidth):
    #resize = timeit.default_timer()
    
    # Resizes all images in lst to the size of
    # the split tiles of the original image
    # returns list of tuples containing rgb values
    lst = [f for f in listdir(mypath + "mosaic_images/") if isfile(
        join(mypath + "mosaic_images/", f)) if not f.endswith('.DS_Store')]
    lst.sort()
    lst2 = []

    for im in lst:
        lst2 += most_frequent_color([im], 'mosaic_images/')
        img = Image.open(mypath + "mosaic_images/" + im)
        img = img.resize((tileWidth, tileWidth), Image.ANTIALIAS)
        img.save(mypath + 'mosaic_images/' + im, subsampling=0, quality=100)
        print(im)
    #stopresize = timeit.default_timer()
    return lst2


def grid(nj, orgimage):
    #grids = timeit.default_timer()
    lst = [f for f in listdir(mypath + "mosaic_images/") if isfile(
        join(mypath + "mosaic_images/", f)) if f != '.DS_Store']
    lst.sort()
    tile = Image.open(mypath + "mosaic_images/" + lst[0])
    w, h = tile.size  # width and height of tile
    orgimage = Image.open(orgimage)
    total_w, total_h = orgimage.size
    x = 0
    y = 0
    t = 0
    result = Image.new('RGB', (total_w, total_h))  # new image
    while y + h <= total_h and t < len(nj):
        x = 0
        while x + w <= total_w:
            img = lst[nj[t][1]]
            im = Image.open(mypath + "mosaic_images/" + img)
            result.paste(im, (x, y))
            t += 1
            x += w
        y += h

    result.save(mypath + 'final.jpeg')
    #stopgrids = timeit.default_timer()
    result.show()

    #for f in tile_img:
    #os.remove(mypath+"tiles/"+f)

    #[os.remove(mypath+"mosaic_images/"+file) for file in os.listdir(mypath+"mosaic_images/")]
    #[os.remove(mypath+"tiles/"+file) for file in os.listdir(mypath+"tiles/") if file != '.DS_Store']
split = timeit.default_timer()
si = SplitImage('index4.jpeg', 25)
stopsplit = timeit.default_timer()
grids = timeit.default_timer()
grid(Final(si), 'resized.jpeg')
stopgrids = timeit.default_timer()
stop = timeit.default_timer()
print('SplitImage time:',stopsplit-split)
print('Grids:', stopgrids-grids)
print ('Totaltime',stop - start) 

