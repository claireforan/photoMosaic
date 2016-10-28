from PIL import Image
import image_slicer
from os import listdir
from os.path import isfile, join
from math import sqrt
from ColourCost import *
from mosaic1 import *
import re
import timeit
mypath= '/home/gabrielle/mosaic/'

start = timeit.default_timer()


def digit(text):
    #checks for digits
    return int(text) if text.isdigit() else text

def keys(text):
    #sorts strings with integers inside
    return [ digit(c) for c in re.split('(\d+)', text) ]

def crop(img, N):
    img = Image.open(img)
    imgwidth, imgheight = img.size
    width = imgwidth//N
    height = imgheight//N
    row = 0
    i=0
    k=0
    while i < imgheight:
        j = 0
        col = 0
        while j < imgwidth:
            k+=1
            box = (j, i, j+width, i+height)
            a = img.crop(box)
            a.save(mypath+"tiles/slices_" +"%i%s" % (k, ".jpeg"))
            j += width
            col += 1
        i += height
        row += 1



def SplitImage(img, N):
    img = Image.open(img)
    imgwidth, imgheight = img.size
    # Barry
    if imgwidth > imgheight:
        diff = imgwidth - imgheight
        h = imgheight - N * int( imgheight//N )
        print( "h = ", h)
        #resized = img.crop(((diff + h)//2,  h//2, imgheight + diff - h,imgheight - h//2))
        resized = img.crop((0,0, imgheight - h,imgheight - h))
        #Image.ANTIALIAS
        
    elif imgwidth < imgheight:
        w = imghwidth - N * int( imgwidth//N )
        print("w =", w)
        resized = img.crop((0,0,imgwidth - w, imgwidth - w))
        
    elif imgwidth == imgheight:
        h = imgheight - N * int( imgheight//N )
        resized = img.crop((0,0, imgheight - h,imgheight - h))
        print("same")
        
    resized.save(mypath + "resized.jpeg")
    w1,h1  = resized.size
    img.close()
    crop("resized.jpeg", N)
    tile_img = [f for f in listdir(mypath+"tiles/") if isfile(mypath+"tiles/"+f) if f.startswith('slices')]
    tile_img.sort(key=keys)
    rgbtiles = most_frequent_color(tile_img, 'tiles/')
    rgbimg = ResizeImg(tile_img[0])
    # a list of tuples containging rgb values are stored in variable 'rgbimg'
    #returns a list of rgb values in tuples   
    return rgbtiles,rgbimg



   
def most_frequent_color(lst, folder):
    # Finds most frequntly occuring color
    # in each image in the list
    
    rgb = []
    for image in lst:
        img = Image.open(mypath+folder+image)
        w, h = img.size
        pixels = img.convert('RGB').getcolors(w*h)
        most_frequent_pixel = pixels[0]
        for count, color in pixels:
            if count > most_frequent_pixel[0]:
                most_frequent_pixel = (count, color)
        rgb += [most_frequent_pixel[1]]
        print(image, ":", most_frequent_pixel[1])    
    return rgb


def ResizeImg(tile_image):
    # Resizes all images in lst to the size of
    # the split tiles of the original image
    # returns list of tuples containing rgb values

    lst = [f for f in listdir(mypath+"tiles/") if isfile(join(mypath+"tiles/", f)) if not f.endswith('.DS_Store')]
    lst.sort(key=keys)
    print(lst)
    lst2 = []
    i = Image.open(mypath+'tiles/'+tile_image)
    w,h = i.size
    for im in lst:
        
        lst2 += most_frequent_color([im], 'tiles/')
        img = Image.open(mypath+"tiles/"+im)
        #resizes images
        img = img.resize((w,h), Image.ANTIALIAS)
        #saves resized images in mypath
        img.save(mypath+'tiles/'+im)
    
    return lst2


def grid(nj, orgimage):
    lst = [f for f in listdir(mypath+"tiles/") if isfile(join(mypath+"tiles/", f)) if f != '.DS_Store']
    lst.sort(key=keys)
    print(lst)
    tile = Image.open(mypath+"tiles/"+lst[0])
    w,h = tile.size # width and height of tile
    orgimage = Image.open(orgimage)
    total_w, total_h = orgimage.size
    x = 0
    y = 0
    t = 0
    result = Image.new('RGB', (total_w,total_h)) # new image
    while y + h <= total_h and t < len(nj):
        x = 0
        while x + w <= total_w:
            img = lst[nj[t][1]]
            im = Image.open(mypath+"tiles/"+img)
            result.paste(im,(x, y))
            t += 1
            x+=w
        y += h   
        
    result.save(mypath+'final.jpeg')
    result.show()

        
si = SplitImage('index4.jpeg', 40)
grid(Final(si), 'resized.jpeg')
stop = timeit.default_timer()
#displays running time
print (stop - start) 
