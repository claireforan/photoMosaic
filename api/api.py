import requests
from io import BytesIO
from PIL import Image
import facebook
import os
from cgitb import enable
enable()
os.environ['http_proxy']="http://4c.ucc.ie:80"
os.environ['https_proxy']="http://4c.ucc.ie:80"

def some_action(tileWidth, photo, p, i, temp, token):
    #saves the photo in the folder 'photos' eg photos/0_0.jpeg
    
    response = requests.get(photo['source'])
    img = Image.open(BytesIO(response.content))
    img = img.resize((tileWidth, tileWidth), Image.ANTIALIAS)
    img.save(temp+'%s%s%s%s' % ('photo',str(p),str(i),'.png'), subsampling = 0, quality = 100)
    return img
    return

def get_photos(tileWidth, temp, token):
    user = 'me'
    graph = facebook.GraphAPI(token)
    profile = graph.get_object(user)
    photos = graph.get_connections(profile['id'], 'photos')
    return profile
    # Wrap this block in a while loop so we can keep paginating requests until
    # finished.
    page = -1
    count = 0
    limit = 50
    while True:
        page += 1  
        try:
            # Perform some action on each photo in the collection we receive from
            # Facebook.
            img = 0
            for photo in photos['data']:
                if count < limit:
                    try:
                        count+=1
                        return some_action(tileWidth, photo, page, img, temp, token)
                        img += 1
                    except:
                        print('error')
                        continue

            # Attempt to make a request to the next page of data, if it exists.
            photos = requests.get(photos['paging']['next']).json()    
        except KeyError:
            # When there are no more pages (['paging']['next']), break from the
            # loop and end the script.
            break
    print("Done!")
