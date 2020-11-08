#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from arcgis.features import GeoAccessor, GeoSeriesAccessor
import arcpy


# In[2]:


#Reading Web Layers:
from arcgis import GIS
gis = GIS()
item = gis.content.get("85d0ca4ea1ca4b9abf0c51b9bd34de2e")
flayer = item.layers[0]

#create a Spatially Enabled DataFrame object (SEDF)
sdf = pd.DataFrame.spatial.from_layer(flayer)
sdf.head()


# In[3]:


#inspect the type of object   (In this case it's a dataframe)
type(sdf)


# In[4]:


#Reading Feature Layer Data
#retrieve an item from ArcGIS Online from a known ID value
known_item = gis.content.get("85d0ca4ea1ca4b9abf0c51b9bd34de2e")
known_item


# In[5]:


#obtain the first feature layer from the item
fl = known_item.layers[0]

#use the 'from_layer' static method in the 'spatial' namespace on the Pandas' DataFrame
sdf = pd.DataFrame.spatial.from_layer(fl)

#Return the first 5 records
sdf.head()


# In[6]:


# Filter feature layer records with a sql query. 
# See https://developers.arcgis.com/rest/services-reference/query-feature-service-layer-.htm

df = fl.query(where="AGE_45_54 < 1500").sdf


# In[7]:


for a,b,c,d in zip(df.columns[::4], df.columns[1::4], df.columns[2::4], df.columns[3::4]):
    print("{:<30}{:<30}{:<30}{:<}".format(a,b,c,d))


# In[8]:


#return a subset of records on just the first 5 records
df[['NAME', 'AGE_45_54', 'POP2010']].head()


# In[9]:


#Accessing local GIS data

#authenticate ArcGIS Online or Enterprise
#g2 = GIS("https://www.arcgis.com", "username", "password")

g2 = GIS("https://pythonapi.playground.esri.com/portal", "arcgis_python", "amazing_arcgis_123")


# In[10]:


sdf = pd.DataFrame.spatial.from_featureclass("C:\MissionsMap\SHP\ne_110m_populated_places.shp").sdf.tail()


# In[11]:


#Reading a Feature Class from FileGDB
sdf = pd.DataFrame.spatial.from_featureclass("C:\Users\m_ali\Desktop\Northeastern\GIS_Cartography\FinalProject\MissionsMap\CVCMissionsMap.gdb\CVC_MissionLocations")sdf.head()


# In[ ]:




