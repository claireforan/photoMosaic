from PIL import Image
import image_slicer
from os import listdir
from os.path import isfile,join
from math import sqrt
from ColourCost import *
from mosaicnj import *
mypath = '/Users/claire/mosaic/'

def SplitImage(img, N):
    #creates tiles from image given 
    #image is split into equally sized tiles
    tiles = image_slicer.slice(img, N, save = False)
    #saves files in directory
    image_slicer.save_tiles(tiles, directory=mypath+'tiles/', prefix='slices')
    #stores a list of sorted tiles in variable 'onlyfiles' with file extension '.png'
    tile_img = [f for f in listdir(mypath+"tiles/") if isfile(mypath+"tiles/"+f) if f.startswith('slices') if f.endswith(".png")]
    tile_img.sort()
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
    return rgb

def ResizeImg(tile_image):
    # Resizes all images in lst to the size of
    # the split tiles of the original image
    # returns list of tuples containing rgb values

    lst = [f for f in listdir(mypath+"mosaic_images/") if isfile(join(mypath+"mosaic_images/", f)) if not f.endswith('.DS_Store')]
    lst.sort()
    lst2 = []
    i = Image.open(mypath+'tiles/'+tile_image)
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
    lst = [f for f in listdir(mypath+"mosaic_images/") if isfile(join(mypath+"mosaic_images/", f))  if not f.startswith(orgimage) if f.endswith(".jpeg" )]
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

    for f in tile_img:
        os.remove(mypath+"tiles/"+f)
    
    #[os.remove(mypath+"mosaic_images/"+file) for file in os.listdir(mypath+"mosaic_images/")]
    #[os.remove(mypath+"tiles/"+file) for file in os.listdir(mypath+"tiles/")]
    
    
si = SplitImage('lion.png', 64)
grid(Final(si), 'lion.png')
