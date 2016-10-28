import flickrapi
from PIL import Image
from io import BytesIO
import urllib.request
import os

os.environ['http_proxy']="http://4c.ucc.ie:80"
os.environ['https_proxy']="http://4c.ucc.ie:80"


def getPhotos(token, tags_list, tileWidth):
    if len(tags_list) == 0:
        return 'Go away'
    path = '/var/www/html/tmp_fold/usr_'+token+'/images/'
    if not os.path.isdir(path):
        os.makedirs(path)
        os.chmod(path, 0o777)
    api_key = u'c33f09d4aa3ad2ccc098139a2da21339'
    api_secret = u'5cabb635113d15a5'

    flickr = flickrapi.FlickrAPI(api_key, api_secret, store_token=False)
    limit = 0
    count = 0
    failures = 0
    for tag in tags_list:
        worked = False                                                                                                                                               
        limit += 25                                                                                                                                                  
        try:                                                                                                                                                         
            for photo in flickr.walk(tag_mode='all', tags=tag):                                                                                                      
                worked = True                                                                                                                                        
                count += 1                                                                                                                                           
                if photo == "None":                                                                                                                                  
                    failures += 1                                                                                                                                    
                    break                                                                                                                                            
                if count <= limit:                                                                                                                                   
                    photo_id = photo.get('id')
                    farm_id = photo.get('farm')
                    server = photo.get('server')
                    secret = photo.get('secret')
                    url = 'http://farm' + farm_id + '.staticflickr.com/' + server + '/' + photo_id + '_' + secret + '.jpg'
                    im = urllib.request.urlretrieve(url, path + 'test.png')
                    im = Image.open(path + 'test.png')
                    im = im.resize((tileWidth, tileWidth), Image.ANTIALIAS)
                    im.save(path + '%s%s%s' % ('photo',count,'.png'), subsampling = 0, quality = 100)
                else:
                    break
            if not worked:
                failures += 1        
        except:
            failures += 1
            continue
    if failures == len(tags_list):
        return 'Go away'
    return 'gr8'
