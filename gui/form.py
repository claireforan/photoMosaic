#!/usr/bin/env python3

from cgitb import enable
enable()
from cgi import FieldStorage, escape
from http.cookies import SimpleCookie
from os import environ
import requests
import os
from io import BytesIO
from PIL import Image
import base64

os.environ['http_proxy']="http://4c.ucc.ie:80"
os.environ['https_proxy']="http://4c.ucc.ie:80"

cookie = SimpleCookie()
http_cookie_header = environ.get("HTTP_COOKIE")
if http_cookie_header:
        cookie.load(http_cookie_header)
        if 'up_token' in cookie:
                up_token = cookie['up_token'].value
                form_data = FieldStorage()
        elif 'token' in cookie:
                up_token = cookie['token'].value
                form_data = FieldStorage()

if len(form_data) != 0:
        photo = form_data.getfirst('url', '').strip()
        old_photo = photo
        photo = photo.split(',')
        photo = photo[1]
        photo = str.encode(photo)
        with open("/var/www/html/tmp_fold/usr_" + up_token + "/profile.png", "wb") as fh:
                fh.write(base64.decodestring(photo))
        im = Image.open("/var/www/html/tmp_fold/usr_" + up_token + "/profile.png")
        im.convert("RGB").save("/var/www/html/tmp_fold/usr_" + up_token + "/profile.png")

print("Content-Type: text/html")
print()

print("""
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
        <head>
                <style>
                        #myTags > * {
                                color: #CC0000;
                        }
                </style>
                <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
                <title>MosaicMake</title>
                <meta name="keywords" content="" />
                <meta name="description" content="" />
                <link href="http://fonts.googleapis.com/css?family=Source+Sans+Pro:200,300,400,600,700,900" rel="stylesheet" />
                <link href="../default.css" rel="stylesheet" type="text/css" media="all" />
                <link href="../fonts.css" rel="stylesheet" type="text/css" media="all" />
                <link rel="icon" href="../jigsaw.png">
                <!-- tag stuff -->
                <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.5.2/jquery.min.js" type="text/javascript" charset="utf-8"></script>
                <script src="https://ajax.googleapis.com/ajax/libs/jqueryui/1.8.12/jquery-ui.min.js" type="text/javascript" charset="utf-8"></script>
                <script src="http://aehlke.github.io/tag-it/js/tag-it.js" type="text/javascript" charset="utf-8"></script>
                <link rel="stylesheet" type="text/css" href="http://ajax.googleapis.com/ajax/libs/jqueryui/1/themes/flick/jquery-ui.css">
                <link href="http://aehlke.github.io/tag-it/css/jquery.tagit.css" rel="stylesheet" type="text/css">
                <!--[if IE 6]><link href="default_ie6.css" rel="stylesheet" type="text/css" /><![endif]-->
                <script src="../back_to_top.js" type="text/javascript"></script>
                <script type="text/javascript">

                        function showTags(){
                                var tags = document.getElementById('myTags'); 
                                tags.style.visibility = 'visible';
                                
                        }

                        function hideTags(){
                                var tags = document.getElementById('myTags');
                                tags.style.visibility = 'hidden';
                        }

                        function fillSpan(value){
                                var span = document.getElementById('span');
                                var option = value;
                                if (option === '20' || option === '40' || option === '30') {
                                        span.innerHTML = "Your mosaic will be ready quickly but might not be as good as you'd like!"

                                } else if (option === '50'){
                                        span.innerHTML = "This is the recommended number of photos for quality and speed!"
                                } else if (option === '60'){
                                        span.innerHTML = "Your mosaic will be high quality but might take a while to load!"
                                } else {
                                        span.innerHTML = ""
                                }
                        }
                </script>
        </head>
        <body>
                <a href="#" class="back-to-top"><br>Back to Top</a>
                <div id="header-wrapper" style="height: 35%;">
                        <div id="header" class="container">
                                <div id="logo">
                                        <h1 style=" color: white;"> <img src="../jigsaw.png" alt="jigsaw piece" height="25" width="25">  MosaicMake</h1>
                                </div>
                                <div id="menu">
                                        <ul>
                                                <li class="active"><a href="http://143.239.81.202" accesskey="1" title="">Home</a></li>
                                        </ul>
                                </div>
                        </div>
                </div>
                <script type="text/javascript">
    $(document).ready(function() {
        $("#myTags").tagit();
    });
                </script>
                <div id="wrapper" style='padding-top: 1em; padding-bottom: 2em;'>
                        <br>
                        <div class="container" style='border: 1px solid black; border-radius: .5em; padding: 1em; font-size: 17px;'>
                                <form action="loading.py" method="get">
                                        <label for="photos">Choose the number of photos in your mosaic:  </label>
                                        <select name="photos" onchange='fillSpan(this.value)' required>
                                        <option value="20">20x20 (400)</option>
                                        <option value="30">30x30 (900)</option>
                                        <option value="40">40x40 (1600)</option>
                                        <option value="50">50x50 (2500)</option>
                                        <option value="60">60x60 (3600)</option>
                                        </select><br />
                                        <span id='span' style='display: inline-block; padding-top: .5em;'></span>
                                        <br><br><label for="myTags" style='padding-bottom: .5em;'>Choose by tag which type of images will make up your mosaic:  </label>
                                        <br><br />
                                        <label for="pictures">Use photos from flickr</label>
                                        <input type='radio' id='pictures' name="premade" onclick='showTags()' value="false">
                                        <label for="premade">     Use our pre-selected photos</label>
                                        <input type="radio" id="premade" name="premade" onclick='hideTags()' value="true" checked>
                                        <br /><br />
                                        <ul id="myTags" style="visibility: hidden;">
                                                <!-- Existing list items will be pre-added to the tags -->
                                                <li>Sea</li>
                                                <li>Flower</li>
                                        </ul>
                                        <label for="opacity">Choose the level of definition: </label>
                                        <br><br />
                                        <input type="range" id="opacity" name="opacity" min="0" max="10">
                                        <br><br />
                                        <input type="submit" value="MosaicMake"><br><br>
                                </form>

                        </div>
                </div>
                <div id="copyright" class="container">
                        <p>&copy; MosaicMake. All rights reserved. | released under the <a href="http://templated.co/license">Creative Commons Attribution</a> license | Design by <a href="http://templated.co" rel="nofollow">TEMPLATED</a>.</p>
                </div>
        </body>
</html>
"""  )
