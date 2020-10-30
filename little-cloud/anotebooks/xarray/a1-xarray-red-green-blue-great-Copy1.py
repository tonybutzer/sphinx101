#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Xarray wip


# In[2]:


import datetime
import numpy
import xarray
import rasterio
from lilcubeLib.lc_api import Lilcube
from noteLib import ge_translate


# In[3]:


from lilcubeLib.lc_xarray import AOI_bounding_box, Xpart


# In[4]:


aoi = AOI_bounding_box((30.209661,-2.218817,30.246396,-2.163926))


# In[5]:


date_range = (datetime.datetime(2013,7,6), datetime.datetime(2013,7,7))
# date_range = (datetime(2013,7,6), datetime(2018,7,7))

es_index = 'datacube'
es_type = 'rwanda'

lc = Lilcube()

measurements = ('red','green','blue',)

# return a pandas data frame product id creation date and red
panda_df = lc.search(es_index, es_type, (aoi.ul_lat, aoi.ul_lon), (aoi.lr_lat, aoi.lr_lon),
             time = date_range, measurements = measurements )


# In[6]:


#redfile = panda_df['red'][0]
#xpart = Xpart(aoi.geobox,redfile)


# In[ ]:





# In[7]:


def return_aoi_window(ul,lr, file):
    with rasterio.open(file) as src:
        ep = 'epsg:32636'
        ulx,uly = ge_translate(ul[0],ul[1],epsg=ep)
        row1,col1 = src.index(ulx,uly)
        lrx,lry = ge_translate(lr[0],lr[1],epsg=ep)

        row2,col2 = src.index(lrx, lry)
        print(row1,col1)
        print(row2,col2)
        rows = (row1,row2)
        cols = (col1,col2)
        return rows, cols


# In[8]:


def read_data_from_geotiff(databuf, index, color, geobox, df):
    geoTiff = df.iloc[index][color]
    print(geoTiff)
    # Note that the blocksize of the image is 256 by 256, so we want xarray to use some multiple of that
    xchunk = 2048
    ychunk = 2048
    da = xarray.open_rasterio(geoTiff, chunks={'band': 1, 'x': xchunk, 'y': ychunk})
    # print(geobox)
    # print(dir(geobox))
    gextent = geobox.geographic_extent
    # print(dir(gextent))
    bb = gextent.boundingbox
    # print(bb)
    ul = (bb.top, bb.left)
    lr = (bb.bottom, bb.right)
    ep = 'epsg:32636'
    
    
    with rasterio.open(geoTiff) as src:
        print(src.crs)
        ulx,uly = ge_translate(ul[0],ul[1],epsg=ep)
        row1,col1 = src.index(ulx,uly)
        lrx,lry = ge_translate(lr[0],lr[1],epsg=ep)

        row2,col2 = src.index(lrx, lry)
        #print(row1,col1)
        #print(row2,col2)
        rows = (row1,row2)
        cols = (col1,col2)
        print(rows, cols)
    
    print(da)
    my_raster = da.sel(band=1)
   
    print(my_raster.shape)
    print(rows[0], rows[1])
    holding_tank = my_raster[rows[0]:rows[1], cols[0]:cols[1]]
    numpy.copyto(databuf,holding_tank)
    


# In[9]:


def build_the_xarray(geobox, measures, df):
    data = {}
    THE_XARRAY = xarray.Dataset(attrs={'crs': geobox.crs})
    
    print(THE_XARRAY)
    time_coords = []
    date_coords = []
    for idx, val in df.iterrows():
        key = val['date'] + '_' + val['path'] + '_' + val['row']
        print (key)
        time_coords.append(key)
        date_coords.append(val['date'])
    
    THE_XARRAY['datePR'] = time_coords
    THE_XARRAY['time'] = date_coords
    print(THE_XARRAY)
    
    #print(geobox.coordinates.items())
    
    for name, coord in geobox.coordinates.items():
            THE_XARRAY[name] = (name, coord.values, {'units': coord.units})
            print("GN=",name)
            print(name, len(coord.values))
            print(name, coord.values[0])
    print(THE_XARRAY)
    
    datePR_shape = (len(time_coords), )
    
    for color in measures:
        data[color] = numpy.full(datePR_shape + geobox.shape, '-9999', dtype='int16')

        print("color data.shape", color, data[color].shape)
    
        attrs = {
                    'nodata': '-9999',
                    'units': 'metres',
                    'crs': geobox.crs
                }

    #dims = 'datePR' + tuple(geobox.dimensions)
    
        dims = ('datePR', 'y', 'x')
    
        THE_XARRAY[color] = (dims, data[color], attrs)
        # we NOW have an EMPTY XARRAY
        print(THE_XARRAY)
    
        for index in range(0,len(time_coords)):
            read_data_from_geotiff(data[color][index], index, color, geobox, df)
    
        print(THE_XARRAY)
        
        
    return THE_XARRAY

    


# In[10]:


ds = build_the_xarray(aoi.geobox, measurements, panda_df)


# In[11]:


ds
ds2 = ds.sel(datePR=slice('2013-07-06_172_61', '2013-07-06_172_62'))

#ds.sel(datePR=slice('2013-07-06_172_61', '2013-07-06_172_62')).plot.imshow('x', 'y', col='time', col_wrap=4)


# In[12]:


ds2


# In[13]:


# dir(ds2)


# In[14]:


display_color='red'
ds2[display_color].plot.imshow('x', 'y', col='datePR', col_wrap=4, cmap='tab20')


# https://matplotlib.org/examples/color/colormaps_reference.html

# In[15]:


ds2[display_color].plot.imshow('x', 'y', col='datePR', col_wrap=4, cmap='prism')


# In[16]:


ds2[display_color].plot.imshow('x', 'y', col='datePR', col_wrap=4, cmap='flag')


# In[17]:


ds2[display_color].plot.imshow('x', 'y', col='datePR', col_wrap=4, cmap='gist_stern')


# In[18]:


ds2[display_color].plot.imshow('x', 'y', col='datePR', col_wrap=4, cmap='viridis')


# In[19]:


get_ipython().system('date')


# In[20]:


display_color='blue'
ds2[display_color].plot.imshow('x', 'y', col='datePR', col_wrap=4, cmap='flag')
ds2[display_color].plot.imshow('x', 'y', col='datePR', col_wrap=4, cmap='prism')


# In[21]:


display_color='red'
ds2[display_color].plot.imshow('x', 'y', col='datePR', col_wrap=4, cmap='flag')
ds2[display_color].plot.imshow('x', 'y', col='datePR', col_wrap=4, cmap='prism')


# In[22]:


display_color='green'
ds2[display_color].plot.imshow('x', 'y', col='datePR', col_wrap=4, cmap='flag')
ds2[display_color].plot.imshow('x', 'y', col='datePR', col_wrap=4, cmap='prism')


# In[23]:


from noteLib import *
get_ipython().run_line_magic('matplotlib', 'inline')
for t in range(0,len(ds2.datePR)):
    cnt=t
    figsize=[6,6]
    plot_labeled_rgb(ds2, t, cnt, figsize=figsize)


# In[ ]:




