#!/usr/bin/env python
# coding: utf-8

# # Rasterio Training
# 
# 1. window a single band
# 2. display single band
# 3. window and display 3 tifs as a color composite
# 4. calculate the window from geographic lat lon to ixel offsets col_off and row_off
# 
# 
# ```python
# Window(col_off, row_off, width, height)
# ```
# 
# ## Hey
# https://geohackweek.github.io/raster/04-workingwithrasters/

# In[1]:


get_ipython().system('ls /mnt/rwanda/LC08/172/062/2014/LC081720622014060701T1-SC20181129202036')


# In[2]:


from datetime import datetime

import datacube
dc= datacube.Datacube()


# In[3]:


# AOI copied from bounding box map
extent = (30.209661,-2.218817,30.246396,-2.163926)

x = (extent[0],extent[2])
y = (extent[1],extent[3])

print (x,y)


# In[4]:


date_range = (
        datetime(2013,7,6),
        datetime(2013,7,7))

product = 'l8_rwanda'

dsets = dc.find_datasets(product=product,x = x, y = y,
             output_crs = 'epsg:32636', resolution = (-30,30), 
             time = date_range, measurements = ('red', 'green', 'blue','nir') )


# In[5]:


product = 'l8_rwanda'
ds = dc.load(product=product,x = x, y = y,
             output_crs = 'epsg:32636', resolution = (-30,30), 
             time = date_range, measurements = ('red', 'green', 'blue','nir') )


# ```python
# src.read(window, dest)
# _calc_offset2_impl(
# _calc_offset2
# _read_decimated
#     ```

# In[6]:


ds


# In[7]:


from noteLib import *
get_ipython().run_line_magic('matplotlib', 'inline')
for t in range(0,len(ds.time)):
    cnt=t
    figsize=[6,6]
    plot_labeled_rgb(ds, t, cnt, figsize=figsize)


# In[8]:


def return_path_row(file_path):
    a = file_path.split('_')
    print(a[2], a[3])
    return(a[2])


# In[9]:


myds = dsets[1]
redfile = myds.measurements['red']['path']

return_path_row(redfile)


# In[10]:


redfile


# In[11]:


import rasterio

print(dir(rasterio))
with rasterio.open(redfile) as src:
    w = src.read(1, window=rasterio.windows.Window(1172, 1376, 137, 204))

print(w.shape)


# In[12]:


import noteLib
#dir(noteLib)


# In[13]:


import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
fig1 = plt.figure(figsize=(8,8))
imgplot = plt.imshow(w)


# In[14]:


img_toshow = exposure.equalize_hist(w, mask = np.isfinite(w))

fig1 = plt.figure(figsize=(10,10))
imgplot = plt.imshow(img_toshow)


# In[15]:


import rasterio

print(dir(rasterio))
with rasterio.open(redfile) as src:
    w = src.read(1, window=rasterio.windows.Window(2320, 1172, 137, 204))

print(w.shape)



img_toshow = exposure.equalize_hist(w, mask = np.isfinite(w))

fig1 = plt.figure(figsize=(10,10))
imgplot = plt.imshow(img_toshow)


# # YAY!
# ## yay
# ### yay again

# In[16]:


with rasterio.open(redfile) as src:
    w = src.read(1)

print(w.shape)


# In[17]:


#fig1 = plt.figure(figsize=(8,8))
#imgplot = plt.imshow(w)


# In[18]:


#w.histogram()
type(w)


# In[19]:


from skimage import exposure

img_toshow = exposure.equalize_hist(w, mask = np.isfinite(w))


# In[20]:


fig1 = plt.figure(figsize=(10,10))
imgplot = plt.imshow(img_toshow)


# In[21]:


np.histogram(w)


# In[22]:


#plt.hist(w)


# In[23]:


#import cv2 as cv
#img = cv.imread(redfile)


# In[24]:


#fig1 = plt.figure(figsize=(8,8))
#imgplot = plt.imshow(img)


# In[25]:


#equ = cv.equalizeHist(img)


# If you're coming from the matrix algebra perspective, you can ignore the constants in the affine matrix and refer to the the six paramters as a, b, c, d, e, f. This is the ordering and notation used by the affine Python library.
# 
#     a = width of a pixel
#     b = row rotation (typically zero)
#     c = x-coordinate of the upper-left corner of the upper-left pixel
#     d = column rotation (typically zero)
#     e = height of a pixel (typically negative)
#     f = y-coordinate of the of the upper-left corner of the upper-left pixel
# 

# a = 30.0
# b = 0
# c = xul
# d = 0
# e = -30.0
# f = yul

# In[26]:


# The grid of raster values can be accessed as a numpy array and plotted:
with rasterio.open(redfile) as src:
   oviews = src.overviews(1) # list of overviews from biggest to smallest
   #oview = oviews[-1] # let's look at the smallest thumbnail
   oview = oviews[-2] # let's look at the 2nd smallest thumbnail

   print('Decimation factor= {}'.format(oview))
   # NOTE this is using a 'decimated read' (http://rasterio.readthedocs.io/en/latest/topics/resampling.html)
   thumbnail = src.read(1, out_shape=(1, int(src.height // oview), int(src.width // oview)))

print('array type: ',type(thumbnail))
print(thumbnail)

img_toshow = exposure.equalize_hist(thumbnail, mask = np.isfinite(thumbnail))

fig1 = plt.figure(figsize=(7,7))
plt.imshow(img_toshow)
plt.colorbar()
plt.title('Overview - Band 4 {}'.format(img_toshow.shape))
plt.xlabel('Column #')
plt.ylabel('Row #')


#  Convert BoundingBox to Window
# 
#  window_same = windows.from_bounds(*bbox,src.transform)
#  window_same
# 
#  Window(col_off=0.0, row_off=5150.0, width=7168.0, height=5830.0)
# 
# 

# In[27]:


dir(myds)


# In[28]:


myds.bounds


# In[29]:


myds.transform


# In[30]:


myds.extent


# In[31]:


myds.sources


# https://media.readthedocs.org/pdf/rasterio/stable/rasterio.pdf

# https://gonzmg88.github.io/blog/2018/11/11/RasterioExample
#     

# >>>
# x, y = (dataset.bounds.left + 100000, dataset.bounds.top - 50000)
# >>>
# row, col = dataset.index(x, y)
# >>>
# row, col
# (1666, 3333)
# >>>
# band_one[row, col]
# 7566

# In[32]:


extent = (30.209661,-2.218817,30.246396,-2.163926)

ul_lat = -2.218
ul_lon = 30.209661

ep = 'epsg:32636'

ulx,uly = ge_translate(ul_lat,ul_lon,epsg=ep)

print(ulx,uly)



# In[33]:


with rasterio.open(redfile) as src:
    row,col = src.index(ulx,uly)
    print(row,col)


# In[34]:


with rasterio.open(redfile) as src:
    w = src.read(1, window=rasterio.windows.Window(2320, 1172, 137, 204))

    #w = src.read(1, window=rasterio.windows.Window(col, row, 200, 200))

print(w.shape)



img_toshow = exposure.equalize_hist(w, mask = np.isfinite(w))

fig1 = plt.figure(figsize=(10,10))
imgplot = plt.imshow(img_toshow)


# In[35]:


Latitude= -2.1
Longitude= 30.0

lrx,lry = ge_translate(Latitude,Longitude,epsg=ep)

with rasterio.open(redfile) as src:
    row,col = src.index(lrx,lry)
    print(src.crs)
    print(row,col)


# In[36]:


xo, yo = src.transform * (0, 0)

xo,yo


# In[37]:


print(ulx,uly)


# In[38]:


print ((ulx - xo)/30)


# In[39]:


print((uly - yo)/30)


# In[40]:


with rasterio.open(redfile) as src:
    w = src.read(1, window=((1172, 1376), (2320, 2457)))


# In[41]:


print(w.shape)



img_toshow = exposure.equalize_hist(w, mask = np.isfinite(w))

fig1 = plt.figure(figsize=(10,10))
imgplot = plt.imshow(img_toshow)


# In[42]:


#TONY from geopoly - offx offy boundin_box 
offx = 189600.0 
offy = -239430.0

print((offy - yo)/-30)


# In[43]:


help(ge_untranslate)


# In[44]:


print(ep)

x = offx
y = offy
lat,lon = ge_untranslate(x, y, epsg=ep)

print(lat,lon)

help(ge_translate)

myx, myy = ge_translate(lat, lon, epsg=ep)

print(myx, myy)


# In[45]:


extent = (30.209661,-2.218817,30.246396,-2.163926)

ul_lat = -2.1639
ul_lon = 30.209661

ep = 'epsg:32636'

ulx,uly = ge_translate(ul_lat,ul_lon,epsg=ep)

print(ulx,uly)


# In[46]:


with rasterio.open(redfile) as src:
    row,col = src.index(ulx,uly)
    print(row,col)
    w = src.read(1, window=rasterio.windows.Window(col, row, 200, 200))


# In[47]:


print(w.shape)



img_toshow = exposure.equalize_hist(w, mask = np.isfinite(w))

fig1 = plt.figure(figsize=(10,10))
imgplot = plt.imshow(img_toshow)


# # TONY geobox,affine and crs  | 30.00, 0.00, 189600.00|
# | 0.00,-30.00,-239430.00|
# | 0.00, 0.00, 1.00| epsg:32636
