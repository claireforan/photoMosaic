import flickrapi
from PIL import Image
from io import BytesIO
import urllib.request
import os

os.environ['http_proxy']="http://4c.ucc.ie:80"
os.environ['https_proxy']="http://4c.ucc.ie:80"


def getPhotos(tags_list, tileWidth, directory):
    path = '/var/www/html/demo/' + directory
    if not os.path.isdir(path):
        os.makedirs(path)
        os.chmod(path, 0o777)
    api_key = u'c33f09d4aa3ad2ccc098139a2da21339'
    api_secret = u'5cabb635113d15a5'

    flickr = flickrapi.FlickrAPI(api_key, api_secret, store_token=False)
    limit = 0
    count = 0
    dict = {}
    for tag in tags_list:
        limit += 25
        for photo in flickr.walk(tag_mode='all', tags=tag):
            count += 1
            if count <= limit:
                photo_id = photo.get('id')
                farm_id = photo.get('farm')
                server = photo.get('server')
                secret = photo.get('secret')
                url = 'http://farm' + farm_id + '.staticflickr.com/' + server + '/' + photo_id + '_' + secret + '.jpg'
                im = urllib.request.urlretrieve(url, path + '/test.png')
                im = Image.open(path + '/test.png')
                im = im.resize((tileWidth, tileWidth), Image.ANTIALIAS)
                im.save(path + '/%s%s%s' % ('photo',count,'.png'), subsampling = 0, quality = 100)
                dict[path+'/%s%s%s' % ('photo', count, '.png')] = get_average_color(0, 0, tileWidth, path+'/%s%s%s' % ('photo', count, '.png'))
            else:
                break
    print(dict)
    return
    fh = open('/usr/lib/cgi-bin/dictionary.py', 'w')
    fh.write(dict)
    
    return


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

getPhotos(['sea', 'gold', 'grass', 'sunset', 'green', 'red', 'blue','purple'], 10,'60by60')
