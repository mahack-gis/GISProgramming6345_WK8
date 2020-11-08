#!/usr/bin/env python
# coding: utf-8

# In[1]:


from arcgis import GIS
gis = GIS()

#create an anonymous connection to ArcGIS Online and get a public item
item = gis.content.get("85d0ca4ea1ca4b9abf0c51b9bd34de2e")
flayer = item.layers[0]

#Specifiy a SQL query and get a subset of the original data as a DataFrame
df = flayer.query(where="AGE_45_54 < 1500").sdf

#Visualize the top 5 records
df.head()


# In[2]:


#create a map of the US
m1 = GIS().map("United States")
m1


# In[3]:


m1.zoom = 4
m1.center = [39, -98]


# In[4]:


df.spatial.plot(map_widget = m1)


# In[5]:


m2 = GIS().map('United States', zoomlevel = 4)
m2


# In[6]:


m2.center = [39, -98]
df.spatial.plot(map_widget = m2,
               renderer_type = 's',
               symbol_type = 'simple',
               symbol_style = 'd',  #d - is for diamonds
               colors = 'Reds_r',
               cstep = 50,
               outline_color = 'Blues',
               marker_size = 10)


# In[7]:


df.columns


# In[8]:


df[['ST', 'NAME']].head()


# In[9]:


gis = GIS()
m3 = gis.map("United States", zoomlevel = 4)
m3


# In[10]:


df.spatial.plot(map_widget = m3,
               renderer_type = 'u', #specify the unique value renderer using its notation 'u'
               col = 'ST')  #column to get unique values from


# In[11]:


item = gis.content.get("8444e275037549c1acab02d2626daaee")
flayer = item.layers[0]
df2 = flayer.query().sdf


# In[12]:


fset = flayer.query()


# In[13]:


from arcgis.geometry import Geometry
g = Geometry(fset.features[0].geometry)
g.as_arcpy


# In[14]:


#create an opacity visual variable based on a percent of dominant parties in registered citizens.
opacity_expression = ("var republican = $feature.MP06025a_B;var democrat = $feature.MP06024a_B;"
                      "var independent = $feature.MP06026a_B;var parties = [republican, democrat, independent];"
                      "var total = Sum(parties);var max = Max(parties);return (max / total) * 100;")
opacity_stops = [
    { "value": 33, "transparency": 0.05 * 255, "label": "< 33%" },
    { "value": 44, "transparency": 1.0 * 255, "label": "> 44%" }]


# In[15]:


#develop another Arcade expression to obtain the majority party in a given county.
arcade_expression = ("var republican = $feature.MP06025a_B;var democrat = $feature.MP06024a_B;"
                     "var independent = $feature.MP06026a_B;var parties = [republican, democrat, independent];"
                     "return Decode( Max(parties),republican, 'republican', democrat, 'democrat',independent, "
                     "'independent','n/a' );")
uv = [{"label":"Democrat","symbol":{"type":"esriSFS","color":[0,195,255,255],
                                    "outline":{"type":"esriSLS","color":[0,0,0,51],
                                               "width":0.5,"style":"esriSLSSolid"},
                                    "style":"esriSFSSolid"},"value":"democrat"},
      {"label":"Republican","symbol":{"type":"esriSFS","color":[255,0,46,255],"outline":{
          "type":"esriSLS","color":[0,0,0,51],"width":0.5,"style":"esriSLSSolid"},
                                      "style":"esriSFSSolid"},"value":"republican"},
      {"label":"Independent/other party","symbol":{"type":"esriSFS","color":[250,255,0,255],
                                                   "outline":{"type":"esriSLS","color":[0,0,0,51],
                                                              "width":0.5,"style":"esriSLSSolid"},
                                                   "style":"esriSFSSolid"},"value":"independent"}]


# In[16]:


gis = GIS()
m3_ua = gis.map('United States', zoomlevel = 4)
m3_ua


# In[17]:


#Provide the color scheme, and the arcade_expression to render the data in a dynamic/rich form.
df2.spatial.plot(colors='coolwarm',
                map_widget=m3_ua,
                renderer_type='u-a',  # 'u-a' stands for uniqe value with arcade expression
                unique_values=uv,
                opacity_stops=opacity_stops,
                opacity_expression=opacity_expression,
                arcade_expression=arcade_expression)


# In[18]:


#visualize the same major cities point dataset using its POPULATION column.
df[['ST', 'NAME', 'POPULATION']].head()


# In[19]:


m4 = gis.map('USA', zoomlevel = 4)
m4


# In[20]:


df.spatial.plot(map_widget=m4,
               renderer_type='c',  # for class breaks renderer
               method='esriClassifyNaturalBreaks',  # classification algorithm
               class_count=20,  # choose the number of classes
               col='POPULATION',  # numeric column to classify
               cmap='prism',  # color map to pick colors from for each class
               alpha=0.7  # specify opacity
               )


# In[21]:


#plotting a histogram of the same POPULATION column and try to match the colors. To get the class breaks for the above map, you can inspect the layer definition from MapView object as shown below:
dict(m4.layers[0].layer.layerDefinition.drawingInfo.renderer).keys()


# In[22]:


class_breaks = m4.layers[0].layer.layerDefinition.drawingInfo.renderer.classBreakInfos
print(len(class_breaks))


# In[23]:


#loop through each of the class breaks and obtain the min, max values and the colors for each class.
cbs_list = []
cmap_list = []
for cb in class_breaks:
    print(cb.description)  # print the class break labels
    cbs_list.append(cb.classMaxValue)
    cmap_list.append([x/255.0 for x in cb.symbol.color])


# In[24]:


#plot a histogram using the same breaks and colors.
import matplotlib.pyplot as plt

# build a histogram for the same class breaks
n, bins, patches = plt.hist(df['POPULATION'], bins=cbs_list)

# apply the same color for each class to match the map
idx = 0
for c, p in zip(bins, patches):
    plt.setp(p, 'facecolor', cmap_list[idx])
    idx+=1

plt.title('Histogram of POPULATION column')


# In[ ]:




