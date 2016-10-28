from PIL import Image
import image_slicer
from os import listdir
from os.path import isfile,join
from math import sqrt
from ColourCost import *
from mosaicnj import *
mypath= '/Users/claire/mosaic/'
 
def crop(img, N):
    im = Image.open(img)
    imgwidth, imgheight = im.size
    width = imgwidth/N
    height = imgheight/N
    
    im = Image.open(img)
    row = 0
    i=0
    while i < imgheight:
        j = 0
        col = 0
        while j < imgwidth:
            box = (j, i, j+width, i+height)
            a = im.crop(box)
            a.save(mypath+"mosaic_images/slices_" +"%i_%i%s" % (row, col, ".jpeg"))
            j += width
            col += 1
        i += height
        row += 1
x - n*floor(x/n)
def SplitImage(img, N):
    
    # Barry
    if imgwidth > imgheight:
        h = imgheight - N * int( imgheight/N )
        img.crop((h,h), Image.ANTIALIAS)
        
    elif imgwidth < imgheight:
        h = imgheight - N * int( imgheight/N )
        img.crop((h,h), Image.ANTIALIAS)
        
    elif imgwidth = imgheight:
        h = imgheight - N * int( imgheight/N )
        img.crop((h,h), Image.ANTIALIAS)
        
        
        
    if imgwidth > imgheight:
        img.crop((h,h), Image.ANTIALIAS)
        if imgwidth % N != 0:
            img.crop(h-(imgwidth % N),h)
    else:
        img.crop((w,w), Image.ANTIALIAS)
        if imgheight % N != 0:
            img.crop(w,w-(imgheight % N))
    crop(img, N)
    tile_img = [f for f in listdir(mypath+"mosaic_images/") if isfile(mypath+"mosaic_images/"+f) if f.startswith('slices')]
    tile_img.sort()
    print("Tiles:",tile_img)
    rgbtiles = most_frequent_color(tile_img, 'mosaic_images/')
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
    return rgb


def ResizeImg(tile_image):
    # Resizes all images in lst to the size of
    # the split tiles of the original image
    # returns list of tuples containing rgb values

    lst = [f for f in listdir(mypath+"mosaic_images/") if isfile(join(mypath+"mosaic_images/", f)) if not f.endswith('.DS_Store')]
    lst.sort()
    print("Images Before:", lst)
    lst2 = []
    i = Image.open(mypath+'mosaic_images/'+tile_image)
    w,h = i.size
    for im in lst:
        
        lst2 += most_frequent_color([im], 'mosaic_images/')
        img = Image.open(mypath+"mosaic_images/"+im)
        #resizes images
        img = img.resize((w,h), Image.ANTIALIAS)
        #saves resized images in mypath
        img.save(mypath+'mosaic_images/'+im)
    
    return lst2




def grid(nj, orgimage):
    #nj = [(0,3), (1,0), (2,2),(3,1)]
    lst = [f for f in listdir(mypath+"mosaic_images/") if isfile(join(mypath+"mosaic_images/", f)) if f != '.DS_Store']
    lst.sort()
    print("Images:", lst)
    print(nj)
    tile = Image.open(mypath+"mosaic_images/"+lst[0])
    w,h = tile.size # width and height of tile
    orgimage = Image.open(orgimage)
    total_w, total_h = orgimage.size
    x=0
    y=0
    t = 0
    result = Image.new('RGB', (total_w,total_h)) # new image
    while y < total_h:
        x = 0
        while x < total_w:
            img = lst[nj[t][1]]
            img = Image.open(mypath+"mosaic_images/"+img)
            result.paste(img,(x, y))
            t += 1
            x+=w
        y += h
        
        
    result.save(mypath+'final.jpeg')
    result.show()
    

    #for f in tile_img:
        #os.remove(mypath+"tiles/"+f)
    
    #[os.remove(mypath+"mosaic_images/"+file) for file in os.listdir(mypath+"mosaic_images/")]
    #[os.remove(mypath+"tiles/"+file) for file in os.listdir(mypath+"tiles/") if file != '.DS_Store']
    
#SplitImage('68_1.jpg', 3307)    
si = SplitImage('68_1.jpg', 8)
grid(Final(si), '68_1.jpg')
