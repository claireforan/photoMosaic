#!/usr/bin/env python3

from cgitb import enable
enable()
from cgi import FieldStorage, escape
from http.cookies import SimpleCookie
from os import environ
import os
from PIL import Image
import base64


#os.environ['http_proxy']="http://4c.ucc.ie:80"
#os.environ['https_proxy']="http://4c.ucc.ie:80"

result = "problem"

cookie = SimpleCookie()
http_cookie_header = environ.get("HTTP_COOKIE")
if http_cookie_header:
        cookie.load(http_cookie_header)
        if 'token' in cookie:
                token = cookie['token'].value
                path = "/var/www/html/tmp_fold/usr_" + token + "/profile.png"
                form_data = FieldStorage()
                if len(form_data) != 0:
                        image = escape(form_data.getfirst("image", "").strip())
                        image = image.split(',')
                        image = image[1]
                        image = str.encode(photo)
                        with open( path , "wb") as fh:
                                fh.write(base64.decodestring(image))
                        im = Image.open(path)
                        im.convert("RGB").save(path)
                        result = "good"
print("Content-Type: text/plain")
print()
print(result)
