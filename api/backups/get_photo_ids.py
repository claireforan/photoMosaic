"""
A simple example script to get all photos on a user's timeline.
Originally created by Mitchell Stewart.
<https://gist.github.com/mylsb/10294040>
"""
import facebook
import requests
from PIL import Image
from io import BytesIO


def some_action(photo, p, i):
    #saves the photo in the folder 'photos' eg photos/0_0.jpeg
    
    response = requests.get(photo['source'])
    img = Image.open(BytesIO(response.content))
    img = img.resize ((tileWidth, tileWidth), Image.ANTIALIAS)
    img.save("photos/%i_%i.jpeg" %(p, i))

    return(photo['source'])

def get_facebook_images():
    # You'll need an access token here to do anything.  You can get a temporary one
    # here: https://developers.facebook.com/tools/explorer/
    access_token = 'EAACEdEose0cBAFw2yQcdkBRrt4CpXzetgC7tEZAyZBx1EvGe8eKHDet6sZC1I7ZBWR3y7V0KArLdDyo3K1MfsWL9GFN54q7gZAiOttT24q5yIsLO6P8OATPE6fvSng5GtTVQq40NQeuAoiZBf4alsHlJH3MTQRw8fZB9sQlhG77WQZDZD'
    # Look at my profile!
    user = 'me'

    graph = facebook.GraphAPI(access_token)
    profile = graph.get_object(user)
    photos = graph.get_connections(profile['id'], 'photos')

    # Wrap this block in a while loop so we can keep paginating requests until
    # finished.
    page = -1
    while True:
        page += 1  
        try:
            # Perform some action on each photo in the collection we receive from
            # Facebook.
            img = 0
            for photo in photos['data']:
                some_action(photo, page, img)
                img += 1

            # Attempt to make a request to the next page of data, if it exists.
            photos = requests.get(photos['paging']['next']).json()    
        except KeyError:
            # When there are no more pages (['paging']['next']), break from the
            # loop and end the script.
            break
    print("Done!")        
     
      



   
