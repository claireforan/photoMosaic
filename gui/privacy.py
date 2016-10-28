#!/usr/bin/env python3

import os
from cgitb import enable

enable()
os.environ['http_proxy'] = 'http://4c.ucc.ie'
os.environ['https_proxy'] = 'http://4c.ucc.ie'

print('Content-Type: text/html')
print()
print("""
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<!--
Design by TEMPLATED
http://templated.co
Released for free under the Creative Commons Attribution License

Name       : RedMarket 
Description: A two-column, fixed-width design with dark color scheme.
Version    : 1.0
Released   : 20140101

-->
<html lang="en" xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>MosaicMake</title>
<meta name="keywords" content="" />
<meta name="description" content="" />
<link href="http://fonts.googleapis.com/css?family=Source+Sans+Pro:200,300,400,600,700,900" rel="stylesheet" />
<link href="../default.css" rel="stylesheet" type="text/css" media="all" />
<link href="../fonts.css" rel="stylesheet" type="text/css" media="all" />
<link href="../jigsaw.png" rel="icon" />

<!--[if IE 6]><link href="default_ie6.css" rel="stylesheet" type="text/css" /><![endif]-->

<script src="../back_to_top.js" type="text/javascript"></script>
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
<div id="wrapper">
	<br/>
	<div class="container">
		<div class="title">
			<h2>Privacy Policy</h2></div>

			<p>This Privacy Policy governs the manner in which MosaicMake collects, uses, maintains and discloses information collected from users (each, a "User") of the http://143.239.81.202 website ("Site").</p>

			<h3>Personal identification information</h3>
			<p>We may collect personal identification information from Users in a variety of ways, including, but not limited to, when Users visit our site, place an order, and in connection with other activities, services, features or resources we make available on our Site. Users may be asked for, as appropriate, email address, phone number. Users may, however, visit our Site anonymously. We will collect personal identification information from Users only if they voluntarily submit such information to us. Users can always refuse to supply personally identification information, except that it may prevent them from engaging in certain Site related activities.</p>

			<h3>Non-personal identification information</h3>
			<p>We may collect non-personal identification information about Users whenever they interact with our Site. Non-personal identification information may include the browser name, the type of computer and technical information about Users means of connection to our Site, such as the operating system and the Internet service providers utilized and other similar information.</p>

			<h3>Web browser cookies</h3>
			<p>Our Site may use "cookies" to enhance User experience. User's web browser places cookies on their hard drive for record-keeping purposes and sometimes to track information about them. User may choose to set their web browser to refuse cookies, or to alert you when cookies are being sent. If they do so, note that some parts of the Site may not function properly.</p>

			<h3>How we use collected information</h3>
			<p>MosaicMake may collect and use Users personal information for the following purposes:</p>
			<ul>
			  	<li>
			    	<i>To run and operate our Site</i><br/>
    				We may need your information display content on the Site correctly.
  				</li>
  				<li>
    				<i>To personalize user experience</i><br/>
    				We may use information in the aggregate to understand how our Users as a group use the services and resources provided on our Site.
  				</li>
			</ul>

			<h3>How we protect your information</h3>
			<p>We adopt appropriate data collection, storage and processing practices and security measures to protect against unauthorized access, alteration, disclosure or destruction of your personal information, username, password, transaction information and data stored on our Site.</p>

			<h3>Sharing your personal information</h3>
			<p>We do not sell, trade, or rent Users personal identification information to others. We may share generic aggregated demographic information not linked to any personal identification information regarding visitors and users with our business partners, trusted affiliates and advertisers for the purposes outlined above. </p>

			<h3>Third party websites</h3>
			<p>Users may find advertising or other content on our Site that link to the sites and services of our partners, suppliers, advertisers, sponsors, licensors and other third parties. We do not control the content or links that appear on these sites and are not responsible for the practices employed by websites linked to or from our Site. In addition, these sites or services, including their content and links, may be constantly changing. These sites and services may have their own privacy policies and customer service policies. Browsing and interaction on any other website, including websites which have a link to our Site, is subject to that website's own terms and policies.</p>

			<h3>Compliance with children's online privacy protection act</h3>	
			<p>Protecting the privacy of the very young is especially important. For that reason, we never collect or maintain information at our Site from those we actually know are under 13, and no part of our website is structured to attract anyone under 13.</p>

			<h3>Changes to this privacy policy</h3>
			<p>MosaicMake has the discretion to update this privacy policy at any time. When we do, we will post a notification on the main page of our Site. We encourage Users to frequently check this page for any changes to stay informed about how we are helping to protect the personal information we collect. You acknowledge and agree that it is your responsibility to review this privacy policy periodically and become aware of modifications.</p>

			<h3>Your acceptance of these terms</h3>
			<p>By using this Site, you signify your acceptance of this policy. If you do not agree to this policy, please do not use our Site. Your continued use of the Site following the posting of changes to this policy will be deemed your acceptance of those changes. This policy was generated using <a href="http://privacypolicies.com" target="_blank">www.privacypolicies.com</a></p>

			<h3>Contacting us</h3>
			<p>If you have any questions about this Privacy Policy, the practices of this site, or your dealings with this site, please contact us.</p>

			<p>This document was last updated on July 19, 2016</p>
	</div>
</div>
<div id="copyright" class="container">
	<p>&copy; Untitled. All rights reserved. | released under the <a href="http://templated.co/license">Creative Commons Attribution</a> license | Design by <a href="http://templated.co" rel="nofollow">TEMPLATED</a>.</p>
</div>
</body>
</html>
""")
