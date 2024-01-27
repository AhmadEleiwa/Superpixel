import numpy as np
from skimage.segmentation import slic
from skimage.segmentation import mark_boundaries
from skimage.io import imread, imshow

image = imread('Hassoun.jpg')

# slic is a superpixel function in sciki
# the n_segment refer to the number of segemnts
# the compactness refer to the shape of each segment
segments = slic(image, n_segments=10, compactness=40)

# this function used for make boundaris to segments on the image
segmented_image = mark_boundaries(image, segments)
imshow(segmented_image)
