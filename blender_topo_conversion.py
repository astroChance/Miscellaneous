"""
Takes the GeoTiff tar file downloaded from OpenTopography.com
and converts to a .png file that is slightly more user-friendly
in Blender. The result is a black and white image that can be 
used as a height (displacement) attribute in Blender
"""


import tarfile
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os

##--------------------
## USER INPUT

## path to your tar file
tar_path = "./test_file.tar.gz"




##--------------------
## UNPACK THE TAR FILE
tar_file = tarfile.open(tar_path)
tar_dir = os.path.dirname(tar_path)
tar_file.extractall(tar_dir, filter="tar")

### This assumes you only downloaded the a single geotiff image
### If you downloaded multiple products, the indexing [0] may fail
tar_filename = tar_file.getnames()[0]

tar_file.close()


##--------------------
## SAVE AS 

## Open the image
img = Image.open(os.path.join((tar_dir), tar_filename))

## PIL can be weird about conversion, so go through
## a numpy array to make life eaier
img_array = np.array(img)

## Save as black and white
file_name = tar_filename.split(".")[0]
png_filename = os.path.join((tar_dir), file_name) + ".png"
plt.imsave(png_filename, img_array, cmap="grey")