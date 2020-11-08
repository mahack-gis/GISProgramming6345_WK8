#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')


# 
# # Basic pie chart
# 
# 
# Demo of a basic pie chart plus a few additional features.
# 
# In addition to the basic pie chart, this demo shows a few optional features:
# 
#     * slice labels
#     * auto-labeling the percentage
#     * offsetting a slice with "explode"
#     * drop-shadow
#     * custom start angle
# 
# Note about the custom start angle:
# 
# The default ``startangle`` is 0, which would start the "Frogs" slice on the
# positive x-axis. This example sets ``startangle = 90`` such that everything is
# rotated counter-clockwise by 90 degrees, and the frog slice starts on the
# positive y-axis.
# 

# In[18]:


import matplotlib.pyplot as plt

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Cookies N Cream', 'Vanilla', 'Mint Chocolate Chip', 'Strawberry', 'Chocolate'
sizes = [26, 35, 10, 8, 21]
explode = (0, 0.1, 0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()


# ------------
# 
# References
# """"""""""
# 
# The use of the following functions, methods, classes and modules is shown
# in this example:
# 
# 

# In[3]:


import matplotlib
matplotlib.axes.Axes.pie
matplotlib.pyplot.pie


# In[ ]:




