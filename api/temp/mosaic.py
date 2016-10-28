from PIL import Image, ImageFilter
from os import listdir
from os.path import isfile, join
from ColourCost import *
from mosaic1 import *
from apitmp import *
import shutil
import tempfile


def SplitImage(img, N, token):
    temp = os.makedirs('/tmp/temps/user'+token+'/images')
    temp = '/tmp/temps/user'+token+'/images/'
    try:
        im = Image.open(img)
    except FileNotFoundError:
        print("Error opening main image")
        exit()
    imgwidth, imgheight = im.size
    if imgwidth > imgheight:
        diff = imgwidth - imgheight
        d = imgheight - N * int(imgheight // N)
        resized = im.crop((0, 0, imgheight - d, imgheight - d))

    elif imgwidth < imgheight:
        d = imgwidth - N * int(imgwidth // N)
        resized = im.crop((0, 0, imgwidth - d, imgwidth - d))

    elif imgwidth == imgheight:
        d = imgheight - N * int(imgheight // N)
        resized = im.crop((0, 0, imgheight - d, imgheight - d))

    resized.save('/tmp/temps/user'+token +'/' + "resized.jpeg")

    im2 = Image.open('/tmp/temps/user'+token +'/'+ "resized.jpeg")
    w2, h2 = im2.size
    
    rgb_value = get_rgb('resized.jpeg', N, w2, h2)
    tileWidth = w2 // N
    get_photos(tileWidth, temp)
    
    mosaic_images = [f for f in listdir(temp) if isfile(
        join(temp, f)) if not f.endswith('.DS_Store') if f.endswith('jpeg')]
    mosaic_images.sort()
    rgbimg = []
    for img in mosaic_images:
        try:
            rgbimg += [get_average_color(0, 0, tileWidth, temp+ img)]
        except IOError:
            print("Error")
            continue

    return rgb_value, rgbimg


def get_rgb(image, N, w, h):
    print("get rgb")
    div = w // N
    rgbimg = []
    htile = 0
    
    while htile < h:
        wtile = 0
        while wtile < w:
            r, g, b = get_average_color(wtile, htile, div, image)
            rgbimg += [(r, g, b)]
            wtile += div
        htile += div
    print("DONE getrgb")
    return rgbimg


def get_average_color(w, h, n, image):
    """ Returns a 3-tuple containing the RGB value of the average color of the
    given square bounded area of length = n whose origin (top left corner) 
    is (x, y) in the given image"""

    image = Image.open(image).load()
    r, g, b = 0, 0, 0
    count = 0
    for s in range(w, w + n):
        for t in range(h, h + n):
            pixlr, pixlg, pixlb = image[s, t]
            r += pixlr
            g += pixlg
            b += pixlb
            count += 1
    return ((r // count), (g // count), (b // count))
    

def grid(nj, orgimage, token):
    #change tmp to cgi-bin
    mosaic_images = [f for f in listdir('/tmp/temps/user'+token+'/images/') if isfile(
        join('/tmp/temps/user'+token+'/images/', f)) if f != '.DS_Store' if f.endswith("jpeg")]
    mosaic_images.sort()
    #print("LIST WITH IMAGES")
    #change tmp to cgi-bin
    tile = Image.open('/tmp/temps/user'+token+'/images/' + mosaic_images[0])
    w, h = tile.size  # width and height of tile
    #change tmp to cgi-bin
    orgimage = Image.open('/tmp/temps/user'+token +'/'+orgimage)
    total_w, total_h = orgimage.size
    print(total_w, total_h)
    x = 0
    y = 0
    t = 0
    result = Image.new('RGB', (total_w, total_h))  # new image
    print(nj)
    len_nj = len(nj)
    while y + h <= total_h and t < len_nj:
        x = 0
        while x + w <= total_w:
            img = mosaic_images[nj[t][1]]
            #change tmp to cgi-bin
            im = Image.open('/tmp/temps/user'+token +'/images/'+ img)
            result.paste(im, (x, y))
            t += 1
            x += w
        y += h
    #change tmp to cgi-bin
    result.save('/tmp/temps/user'+token + 'res.jpeg')
    #change tmp to cgi-bin
    im2 = Image.open('/tmp/temps/user'+token +'/'+'resized.jpeg') 
    im3 = im2.filter(ImageFilter.EDGE_ENHANCE_MORE)
    #change tmp to cgi-bin
    im3.save('/tmp/temps/user'+token +'/' +'im3.jpeg')
    final = Image.blend(result, im3, 0.25)
    #change tmp to cgi-bin
    final.save('/tmp/temps/user'+token +'/'+ 'final.jpeg')
    #deletes the user's folder
    #shutil.rmtree('/tmp/temps/user'+token +'/')
    final.show()

#the parameter 'token' will have the access token passed through there
si = SplitImage('kitty.jpeg', 50, '12345')
#the parameter 'token' will have the access token passed through there
grid(Final(si), 'resized.jpeg', '12345' )
