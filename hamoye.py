#!/usr/bin/env python
# coding: utf-8

# In[7]:


import numpy as np
import pandas as pd


# In[16]:


df = pd.read_csv('desktop/fuel_ferc1.csv', encoding="latin-1")


# In[10]:


dfh = pd.DataFrame(df)


# In[13]:


dfh


# In[17]:


my_tuppy = (1,2,5,8)


# In[18]:


my_tuppy[2] = 6






# In[19]:


S = [['him', 'sell'], [90, 28, 43]]


# In[20]:


S[0][1][1]


# In[21]:


lst = [[35, 'Portugal', 94], [33, 'Argentina', 93], [30 , 'Brazil', 92]]


# In[24]:


col = ['Age','Nationality','Overall']


# In[28]:



ds=pd.DataFrame(lst, column=['Age', 'Nationality', 'Overall'], index = [123])


# In[29]:


y = [(2, 4), (7, 8), (1, 5, 9)]

# Access element 8 using indexing
x = y[1][1]

print(x)


# In[ ]:




