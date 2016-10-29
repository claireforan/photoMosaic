# MosaicMake
A photo mosaic is an approximation of an image using a given set of images This problem was formulated from the work previously achieved on [domino portraits](http://pagesperso.g-scop.grenoble-inp.fr/~cambazah/page2/assets/domino_final.pdf) by a team of [Insight](https://www.insight-centre.org/) researchers. Photo mosaics have been generated most often using integer linear programming techniques that provide optimal solutions, but these can be slow and do not scale well to larger mosaics. In this project, we propose an approach that overcomes these limitations and efficiently provides high quality portraits.

## Introduction
Our initial proposal combines image processing using combinatorial optimization and constraint programming. Our problem was originally viewed as an assignment problem, however to provide a scalable model we accepted duplicate images giving a subsequent optimal solution and empirically, it can be shown that the results were both a reduction in search time and a high quality photo mosaic. 

## Cost Matrix
A set of images can be simplified into a constrained palette of RGB values which we used to produce a photo mosaic. Similarly, we break down the photo we wish to make a mosaic of into a list of RGB values. In order to find the optimal solution, a combined weighted Euclidean distance formula is used to calculate the colour cost or distances between two RGB values to create an optimal matching between images and tiles of the chosen photo.
The output of this function is a cost matrix which forms the input of our [Numberjack](http://numberjack.ucc.ie/) model. 

## Constraints Model
[Numberjack](http://numberjack.ucc.ie/) is a modelling package written in [Python](https://www.python.org/) for constraint programming. Our model takes the cost matrix and calculates the cheapest cost using the solver [SCIP](http://scip.zib.de/). Originally, it was based on an assignment problem however, as the size of the problem was increased, the search time grew exponentially. In order to overcome this limitation we allowed duplicates. 
Our model produces a boolean matrix, which is then flattened into a list of co-ordinates used by the program. The program slots the best matched image (taken from a list of images) against every other match referring to the main photo. 

## Image Processing
[Pillow](https://python-pillow.org/), a fork of Python, is an imaging library that provided us with the image manipulation tools to produce a high quality mosaic image. After experimenting, we concluded that blending the original photo with the mosaic image at a chosen opacity and using edge-enhancement resulted in  clearer definition and higher precision making of the photo mosaic.

## Evaluation
This approach provides optimal and higher quality solutions, however, a mosaic with a grid of 60x60, will take more time to produce rather than a 20x20. Since the run-time is exponential, we managed to speed up the image manipulation by using pre-made photos.

![Lion before](https://github.com/claireforan/photoMosaic/blob/master/lion1.png)

Figure 1: Original Photo 

![Lion after](https://github.com/claireforan/photoMosaic/blob/master/lion2.jpg)

Figure 2: Photo Mosaic using 1600 images (40x40)

## Where can you find it?
MosaicMake is hosted on `143.239.81.202`, a UCC server.

## Acknowledgments 
This publication has emanated from research conducted with the financial support of Science Foundation Ireland (SFI) under the SFI Scholarship Program.

### APIs
Facebook API: https://developers.facebook.com/docs/javascript

Flickr API: https://stuvel.eu/flickrapi
