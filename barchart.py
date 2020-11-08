#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')


# 
# # Grouped bar chart with labels
# 
# 
# This example shows a how to create a grouped bar chart and how to annotate
# bars with labels.
# 

# In[11]:


import matplotlib
import matplotlib.pyplot as plt
import numpy as np


labels = ['Summer', 'Winter', 'Spring', 'Fall']
high_means = [101, 68, 78, 92]
low_means = [77, 32, 56, 71]

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, high_means, width, label='High')
rects2 = ax.bar(x + width/2, low_means, width, label='Low')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Temps')
ax.set_title('High/Low Temps by Season in Georgia')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(rects1)
autolabel(rects2)

fig.tight_layout()

plt.show()


# ------------
# 
# References
# """"""""""
# 
# The use of the following functions, methods and classes is shown
# in this example:
# 
# 

# In[3]:


matplotlib.axes.Axes.bar
matplotlib.pyplot.bar
matplotlib.axes.Axes.annotate
matplotlib.pyplot.annotate


# In[ ]:




