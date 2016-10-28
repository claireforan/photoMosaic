# Photomosaic in Python

##Apache2 server changes
VAR/WWW/HTML for server path to html

/etc/apache2/mods-enabled/deflate.conf : *added* `text/javascript`

**Aim**: To assign images to grid sections of larger image, sorted by closest average colour using the Assignment Problem.

There are two main areas to our project: processing the images and developing a model which will calculate the best matches between images and grid positions. 


**Image Processing**



**Numberjack Model and  Calculating Colour Distances**

- We have created a program that calculates the colour cost or _distances_ between two RGB values. This program uses a combinated weighted Euclidean distance function, where the weight factor depends on how big the 'red' component is. See [here] (http://www.compuphase.com/cmetric.htm).
- The output of this function is a cost matrix which forms the input of our Numberjack model.
- Our Numberjack model takes the cost matrix and calculates the cheapest path using the Assignment Problem. We then use a function `flatten` that flattens our cost matrix into a list containing the coordinates for which image should go to which cell position i.e. `[(0,1),(1,0),(2,2)]`.
- The output of this function is fed to the image processing.


**Things to do:**

- [ ] Optimise our model and programs.

- [ ] Research Min Cost Flow.

- [ ] Introduce a threshold for more accurate colour matches.

- [x] Develop a path/folder for mosaics to be created in.
