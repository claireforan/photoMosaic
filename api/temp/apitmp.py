"""
A simple example script to get all photos on a user's timeline.
Originally created by Mitchell Stewart.
<https://gist.github.com/mylsb/10294040>
"""
import facebook
import requests
from PIL import Image
from io import BytesIO
import os
import tempfile 

def some_action(photo, p, i, tileWidth,temp):
    response = requests.get(photo['source'])
    img = Image.open(BytesIO(response.content))
    #the picture is coming through
    img = img.resize ((tileWidth, tileWidth), Image.ANTIALIAS)
    quality_val = 100
    #saves the image in the temporary directory ''
    img.save(temp+"/"+'%s%s%s%s' % ('photo',str(p),str(i),'.jpeg'), subsampling = 0, quality = quality_val)
    return(photo['source'])
    

def get_photos(tileWidth, temp):
    # You'll need an access token here to do anything.  You can get a temporary one
    # here: https://developers.facebook.com/tools/explorer/
    access_token = 'EAACEdEose0cBAA1JAhFCvU7t50Nxf0eN0ZBZAtvDPqVmWsiZCeTJdnOqWzeb120BN2w7gHyhSY28gBOKMSjxiAezNm2yQlTUU37ujJjKB5pX1eSMP9TOP4VsQuuEad3i5CvUZCAM32L5t9HoVoYydYQJyYZBovPdpFgaenJfbKAZDZD'
    # Look at my profile!
    user = 'me'

    graph = facebook.GraphAPI(access_token)
    profile = graph.get_object(user)
    photos = graph.get_connections(profile['id'], 'photos')

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
                    count += 1
                    try:
                        some_action(photo, page, img, tileWidth, temp)
                    except:
                        continue
                img += 1
            # Attempt to make a request to the next page of data, if it exists.
            photos = requests.get(photos['paging']['next']).json()    
        except KeyError:
            # When there are no more pages (['paging']['next']), break from the
            # loop and end the script.
            break
    return (temp)
print("Done!")
