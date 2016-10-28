from PIL import Image
import image_slicer
from os import listdir
from os.path import isfile, join
from math import sqrt
from ColourCost import *
from mosaicnj import *
mypath= '/Users/claire/mosaic/'


def crop_tiles(img, N):
    # Crops the original image into tiles
    img = Image.open(img)
    imgwidth, imgheight = img.size
    width = imgwidth//N
    height = imgheight//N
    k = 0
    i=0
    while i < imgheight:
        
        j = 0
        col = 0
        while j < imgwidth:
            k+=1
            box = (j, i, j+width, i+height)
            a = img.crop(box)
            a.save(mypath+"tiles/slices_" +"%i%s" % (k,".jpeg"))
            j += width
            #col += 1
        i += height
        k += 1



def SplitImage(img, N):
    im = Image.open(img)
    imgwidth, imgheight = im.size
    # Barry
    if imgwidth > imgheight:
        diff = imgwidth - imgheight
        h = imgheight - N * int( imgheight//N )
        print( "h = ", h)
        resized = im.crop((0,0, imgheight - h,imgheight - h))
        
    elif imgwidth < imgheight:
        w = imghwidth - N * int( imgwidth//N )
        print("w =", w)
        resized = im.crop((0,0,imgwidth - w, imgwidth - w))
        
    elif imgwidth == imgheight:
        h = imgheight - N * int( imgheight//N )
        resized = im.crop((0,0, imgheight - h,imgheight - h))
    resized.save(mypath + "resized.jpeg")    
    
    #crop_tiles("resized.jpeg", N)
    tiles = image_slicer.slice("resized.jpeg", N*N, save = False)
    image_slicer.save_tiles(tiles, directory=mypath+'tiles/', prefix='slices')
    
    tile_img = [f for f in listdir(mypath+"tiles/") if isfile(mypath+"tiles/"+f) if f.startswith('slices')]
    tile_img.sort()
    print("Tiles:",tile_img)
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

    lst = [f for f in listdir(mypath+"mosaic_images/") if isfile(join(mypath+"mosaic_images/", f)) if not f.endswith('.DS_Store')]
    lst.sort()
    print("Images Before:", lst)
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
    lst = [f for f in listdir(mypath+"mosaic_images/") if isfile(join(mypath+"mosaic_images/", f)) if f != '.DS_Store']
    lst.sort()
    print("Images:", lst)
    tile = Image.open(mypath+"mosaic_images/"+lst[0])
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
            im = Image.open(mypath+"mosaic_images/"+img)
            result.paste(im,(x, y))
            t += 1
            x+=w
        y += h
        
    '''for t in nj:
        img = lst[t[1]]
        print(img)
        img = Image.open(img)
        if x < total_w and y < total_h:
            result.paste(img,(x,y))
            x += w
        elif y < total_h:
            x = 0
            y += h
            result.paste(img,(x,y))
            x += w'''
        
    result.save(mypath+'final.jpeg')
    result.show()
    

    #for f in tile_img:
        #os.remove(mypath+"tiles/"+f)
    
    #[os.remove(mypath+"mosaic_images/"+file) for file in os.listdir(mypath+"mosaic_images/")]
    #[os.remove(mypath+"tiles/"+file) for file in os.listdir(mypath+"tiles/") if file != '.DS_Store']
    
#SplitImage('68_1.jpg', 3307)    
si = SplitImage('test.jpg', 44)
grid(Final(si), 'resized.jpeg')
