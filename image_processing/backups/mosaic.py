from PIL import Image
import image_slicer
from os import listdir
from os.path import isfile,join
from math import sqrt
from Numberjack import *
from ColourCost import *
from mosaicnj import *
mypath= '/Users/claire/mosaic/'

def SplitImage(img, N):
    #creates tiles from image given 
    #image is split into equally sized tiles
    tiles = image_slicer.slice(img, N, save = False)
    #saves files in directory
    image_slicer.save_tiles(tiles, directory=mypath, prefix='slices')
    #stores a list of sorted tiles in variable 'onlyfiles' with file extension '.png'
    tile_img = [f for f in listdir(mypath) if isfile(join(mypath, f)) if f.startswith('slices') if f.endswith(".png")]
    tile_img.sort()
    rgbtiles = most_frequent_color(tile_img)
    rgbimg = ResizeImg(tile_img[0])
    # a list of tuples containging rgb values are stored in variable 'rgbimg'
    #returns a list of rgb values in tuples
    return rgbtiles,rgbimg


   
def most_frequent_color(lst):
    # Finds most frequntly occuring color
    # in each image in the list

    rgb = []
    for image in lst:
        img = Image.open(image)
        w, h = img.size
        pixels = img.convert('RGB').getcolors(w*h)
        most_frequent_pixel = pixels[0]
        for count, color in pixels:
            if count > most_frequent_pixel[0]:
                most_frequent_pixel = (count, color)
        rgb += [most_frequent_pixel[1]]
    return rgb

def ResizeImg(image):
    # Resizes all images in lst to the size of
    # the split tiles of the original image
    #returns list of tuples containing rgb values

    lst = [f for f in listdir(mypath) if isfile(join(mypath, f)) if f.endswith('.jpeg')]
    lst.sort()
    lst2 = []
    i = Image.open(image)
    w,h = i.size
    print(lst)
    for im in lst:
        lst2 += most_frequent_color([im])
        img = Image.open(im)
        #resizes images
        img = img.resize((w,h), Image.ANTIALIAS)
        #saves resized images in mypath
        img.save(mypath+im)
    
    return lst2

####################################################


def ColourDiff(tup1,tup2):
    
    r1,g1,b1 = tup1
    r2,g2,b2 = tup2
    rChange = (r1 - r2) ** 2
    gChange = (g1 - g2) ** 2
    bChange = (b1 - b2) ** 2
    rMean = (r1 + r2) // 2
    
    return int(round(sqrt((2 + rMean // 256 ) * rChange + 4 * gChange + (2 + (255 - rMean) // 256) * bChange)))

def DiffTable(tup):
    (lt1, lt2) = tup
    table = []
    
    for colour1 in lt1:
        row = []
        for colour2 in lt2:
            row += [ColourDiff(colour1, colour2)]
        table += [row]
    return table





def grid(nj, orgimage):
    #nj = [(0,3), (1,0), (2,2),(3,1)]
    lst = [f for f in listdir(mypath) if isfile(join(mypath, f))  if not f.startswith(orgimage) if f.endswith(".jpeg" )]
    lst.sort()
    print(nj)
    tile = Image.open(lst[0])
    w,h = tile.size # width and height of tile
    orgimage = Image.open(orgimage)
    total_w, total_h = orgimage.size
    x=0
    y=0
    result = Image.new('RGB', (total_w,total_h)) # new image
    print(nj)
    for t in nj:
        img = lst[t[1]]
        img = Image.open(img)
        if x < total_w and y < total_h:
            result.paste(img,(x,y))
            x += w
        elif y < total_h:
            x = 0
            y += h
            result.paste(img,(x,y))
            x += w
    result.save(mypath+'final.jpeg')
    result.show()

    
si = SplitImage('lion.png', 64)
grid(Final(si), 'lion.png')
