from PIL import Image, ImageFilter
import os
from os import listdir
from os.path import isfile, join
from ColourCost import *
from nj import *
from flickr_api import *
import tempfile


def SplitImage(img, N, token, tags):
    try:
        im = Image.open(img)       
    except FileNotFoundError:
        return 'Error opening main image'
        exit()
    usr_fold = '/var/www/html/tmp_fold/usr_' + token

    im.save(usr_fold + '/resized.png')
    im2 = Image.open(usr_fold + '/resized.png')
    w2, h2 = im2.size
    if w2 != 600 or  h2 != 600:
        im2 = im2.resize((600,600))
        im2.save(usr_fold + '/resized.png')
        im2 = Image.open(usr_fold + '/resized.png')
        w2, h2 = im2.size            
    rgb_original = get_rgb(usr_fold +'/resized.png', N, w2, h2)
    tileWidth = w2 // N
    message = getPhotos(token, tags, tileWidth) # Photos are now collected when the access token is receicved
    if message == 'Go away':
        return 'Tags no good'    
    mosaic_images = [f for f in listdir(usr_fold + '/images/') if isfile(
        join(usr_fold + '/images/', f)) if not f.endswith('.DS_Store') if f.endswith('png')]
    mosaic_images.sort()
    rgb_images = []
    for img in mosaic_images:
        try: 
            rgb_images += [get_average_color(0, 0, tileWidth, usr_fold + '/images/' + img)]
        except IOError:
            return "Error"
            continue

    return rgb_original, rgb_images


def get_rgb(image, N, w, h):
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
    return rgbimg

def get_average_color(w, h, n, image):
    """ Returns a 3-tuple containing the RGB value of the average color of the
    given square bounded area of length = n whose origin (top left corner) 
    is (x, y) in the given image
    """
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

def grid(nj, orgimage, token, opacity):

    path_to_images = '/var/www/html/tmp_fold/usr_' + token + '/images/'
    mosaic_images = [f for f in listdir(path_to_images) if isfile(
        join(path_to_images, f)) if f != '.DS_Store' if f.endswith("png")]
    tile = Image.open(path_to_images + mosaic_images[0])
    w, h = tile.size  # width and height of tile
    orgimage = Image.open(orgimage)
    total_w, total_h = orgimage.size
    x,y,t = 0,0,0
    result = Image.new('RGB',(total_w, total_h))  # new image
    len_nj = len(nj)
    while y + h <= total_h and t < len_nj:
        x = 0
        while x + w <= total_w:
            img = mosaic_images[nj[t][1]]
            im = Image.open(path_to_images + img)
            result.paste(im, (x, y))
            t += 1
            x += w
        y += h

    usr_fold = '/var/www/html/tmp_fold/usr_' + token
    result.save(usr_fold + '/res.png')
    im2 = Image.open(usr_fold + '/resized.png') 
    im3 = im2.filter(ImageFilter.EDGE_ENHANCE_MORE)
 
    im3.save(usr_fold + '/edge.png')
    
    final = Image.blend(result, im3, int(opacity)/10)
    
    final.save(usr_fold + '/final.png')
    os.chmod(usr_fold + '/final.png', 0o777)
    
    return
