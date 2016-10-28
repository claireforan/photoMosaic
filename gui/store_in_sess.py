#!/usr/bin/env python3

from cgi import FieldStorage, escape
import os
from cgitb import enable
enable()
from shelve import open
from http.cookies import SimpleCookie
form_data = FieldStorage()

if len(form_data) != 0:
        token = form_data.getfirst("token")
        cookie = SimpleCookie()
        cookie['token'] = token
        cookie['mode'] = 'facebook'
        mypath = '/var/www/html/tmp_fold/usr_' + token
        if not os.path.isdir(mypath):
                os.makedirs(mypath)
                os.chmod(mypath, 0o777)

        print(cookie)
        print("Content-Type: text/plain")
        print()
        print("good")
else:
        print("Content-Type: text/plain")
        print()
        print("problem")
