#!/usr/bin/env python3

from cgi import FieldStorage, escape
from cgitb import enable
enable()
from http.cookies import SimpleCookie
from os import environ
from shelve import open
import os

os.environ['http_proxy']="http://4c.ucc.ie:80"
os.environ['https_proxy']="http://4c.ucc.ie:80"

bigimg = ""
littleimgs = []
result = ""
message = ""
title = ""

form_data = FieldStorage()
if len(form_data) != 0:
        user_tags = form_data.getlist('tags')
        img_param = escape(form_data.getfirst('photos','').strip())
        opacity = escape(form_data.getfirst('opacity','').strip())
        premade = escape(form_data.getfirst('premade','').strip())
        output = opacity
        if int(opacity) < 0 or int(opacity) > 10:
                print("Location:http://143.239.81.202/cgi-bin/form.py")
        img_params = [20, 30, 40, 50, 60]
        if int(img_param) not in img_params:
                print("Location:http://143.239.81.202/cgi-bin/form.py")
        if premade != 'false' and premade != 'true':
                print("Location:http://143.239.81.202/cgi-bin/form.py")
print("Content-Type: text/html")
print()

print("""<!DOCTYPE html>
        <html>
                <head>
                        <link href="../default.css" rel="stylesheet" type="text/css" media="all" >
                        <link href="../fonts.css" rel="stylesheet" type="text/css" media="all" >
                        <link href="../loading.css" rel="stylesheet" type="text/css" media="all">
                        <link href="http://fonts.googleapis.com/css?family=Source+Sans+Pro:200,300,400,600,700,900" rel="stylesheet" />
                        <title>MosaicMake</title>
                        <script src="../loading.js"></script>
                        <script src="../back_to_top.js"></script>

                        <link rel="icon" href="../jigsaw.png">
                </head>
                <body>
                        <a href="#" class="back-to-top"><br>Back to Top</a>
                        <div id="header-wrapper" style="background: white; border-bottom: #cc0000;">
                                <div id="header" class="container" style="border-bottom: #cc0000;">
                                        <div id="logo">
                                                <h1 style=" color: white;"> <img src="../jigsaw.png" alt="jigsaw piece" height="25" width="25"> MosaicMake</h1>
                                        </div>
                                        <div id="menu">
                                                <ul>
                                                        <li class="active"><a href="http://143.239.81.202" accesskey="1" title="">Home</a></li>
                                                </ul>
                                        </div>
                                </div>
                        </div>
                        <div id="wrapper" style="background: white; padding: 1em; width: 100%; margin-left: auto; margin-right: auto; height: 50%;">
                                <div class = "loading_frame">
                                        <p>Please wait while your mosaic is being created!</p>
                                        <div class="jigsaw1">
                                                <span class="t"></span>
                                                <span class="r"></span>
                                                <span class="b"></span>
                                                <span class="l"></span>
                                        </div>
                                        <div class = "loading">
                                                <p id="d1">.</p>
                                                <p id="d2">.</p>
                                                <p id="d3">.</p>
                                                <p id="L">L</p><p id="o">o</p><p id="a">a</p><p id="d">d</p><p id="i">i</p><p id="n">n</p><p id="g">g</p>
                                                <p id="d4">.</p>
                                                <p id="d5">.</p>
                                                <p id="d6">.</p>
                                        </div>
                                </div>
                        </div> 
                        <img id="finished_img">
                        <div id="copyright" class="container">
                                <p>&copy; MosaicMake. All rights reserved. | released under the <a href="http://templated.co/license">Creative Commons Attribution</a> 
                                license | Design by <a href="http://templated.co" rel="nofollow">TEMPLATED</a>.</p>
                        </div>
                </body>
        </html>
""" )
