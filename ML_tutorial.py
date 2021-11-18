#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[6]:


titanic=pd.read_csv('dataset/titanic.csv') #directing to the csv file


# In[7]:


titanic #while running gives first five rows and last five rows


# In[10]:


titanic.head() #.head() default gives first five rows


# In[12]:


titanic.head(n=10) #assigning n=10 to get first 10 rows


# In[16]:


titanic.tail() #default gives last 5 rows


# In[17]:


titanic.tail(n=10) #gives last 10 rows


# In[18]:


titanic.columns #to see coloumn names


# In[21]:


titanic.index #to get row index


# In[24]:


titanic.shape #gives number of rows and coloumns


# In[26]:


#extracting a single column, Give coloumn name as string
survived_extr = titanic['survived']
print(survived_extr)


# In[ ]:




