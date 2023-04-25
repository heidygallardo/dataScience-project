#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import math 
import scipy.stats as stats
import seaborn as sb


# In[2]:


data = pd.read_csv("C:/Users/galla/OneDrive/Documents/DataScience/archive/US_youtube_trending_data.csv")


# In[3]:


data


# In[4]:


data.head()


# In[5]:


data.info()


# In[6]:


print(data.isnull().sum())


# In[9]:


nan_descriptions = data[data['description'].isna()]
nan_descriptions.head()


# In[10]:


data['description'] = data['description'].fillna(value="")


# In[11]:


print(data.isnull().sum())


# In[ ]:




