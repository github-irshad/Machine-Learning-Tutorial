#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np


# In[4]:


pd.Series([0.1,0.2,0.3,1]) #Creating a series


# In[5]:


dic = {'abc':'123',1:'E',2:'John',5:'Marvel'} #creating a dictionary
pd.Series(dic) #Dictionary into a series
#Keys are using as row index


# In[6]:


#creating index labels
ser1 = pd.Series(5,index=[1,2,3,4,5]) #A scalar for 1 to 5 indices
ser1


# In[7]:


ser2 = pd.Series({1:'123',2:'E',3:'John',4:'Marvel'},index=[1,2,3,4]) #making subset using explicit labels
ser2 


# In[8]:


ser_read = pd.read_csv('dataset/Marks_list.csv')
ser_read


# In[9]:


ser_read['Student_Name']


# # Dataframe Construction

# In[10]:


state_capitals = {'KA':'Bang','KL':'TVM','TN':'Chennai','AP':'Hyderabad'}
state_lang = {'KA':'Kannada','KL':'Malayalm','TN':'Tamil','AP':'Telugu'}
state_CL = pd.DataFrame({'Capitals':state_capitals,'Lang':state_lang}) #dataframe construction 
#Dict key becomes coloumn hedaing and value become data
state_CL


# In[11]:


#list into dataframe
dlist = {'a':[5,3,2,5],'b':[6,2,7,9],'c':[4,62,2,1]}
df = pd.DataFrame(dlist)


# In[12]:


df


# In[13]:


df_np = pd.DataFrame(np.random.randn(4,3),index=['a','b','c','d'],columns=['one','two','three'])
df_np


# #  Indexing and Properies

# In[14]:


#how to index
ind_a = pd.Index([1,2,3,4,5])
ind_a


# In[15]:


ind_b=pd.Index([1,3,5,7,9])
ind_b


# In[20]:


ind_a|ind_b


# In[21]:


ind_a&ind_b


# In[22]:


ind_a.difference(ind_b)


# In[23]:


ind_a ^ ind_b #symmetric difference


# In[ ]:




