#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Importing essential libraries for EDA
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import random


# In[3]:


#creating categories
category=['Food','Travel','Fashion','Fitness','Music','Culture','Family','Health']
#Generating data for EDA as a dictionary
dict={'Date':pd.date_range('2000-09-29',periods=500),
     'Category':[random.choice(category) for i in range(500)],
     'No_of_likes':np.random.randint(0,10000,size=500) 
                 }


# In[4]:


#Storing the dictionary into a dataframe
sm_data=pd.DataFrame(dict)


# In[5]:


sm_data.head()


# In[6]:


sm_data.tail()


# In[7]:


#counting the data
sm_data.count()


# sm_data.describe

# In[8]:


#data dimension
sm_data.shape


# In[9]:


#deleting non available data
sm_data_new=sm_data.dropna()


# In[10]:


#checking if any duplicates are present
print(sm_data_new.duplicated())


# In[11]:


#deleting duplicates
sm_data_new.drop_duplicates(inplace=True)


# In[12]:


#checking the datatypes
sm_data_new.dtypes


# In[13]:


#change the 'Date' column datatype to datetime
pd.to_datetime(sm_data_new['Date'])


# In[32]:


sm_data_new.dtypes


# In[14]:


# changing the datatype of 'No_likes' to numeric
pd.to_numeric(sm_data_new['No_of_likes'])


# In[15]:


#plotting the 'No_likes' column as histogram
sns.histplot(sm_data_new['No_of_likes'])
plt.show()


# In[16]:


#creating a boxplot of the Category data against No_likes data
sns.boxplot(x=sm_data_new['Category'],y=sm_data_new['No_of_likes'])
plt.show()


# In[21]:


sm_data_new.groupby('Date').mean()


# In[ ]:




