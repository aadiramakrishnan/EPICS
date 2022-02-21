#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


df = pd.read_csv("Dep_World.csv")


# In[4]:


df.head()


# In[5]:


country = df['Entity']
age_15 = df['15-19 years old (%)']


# In[12]:


plt.bar(x=country,
 
        height=age_15)
plt.title('Percentage of 15-19 year old kids showing signs of depression in each region')


# In[11]:


plt.scatter(country, age_15)
plt.xlabel("Region")
plt.ylabel("15-19 year old")
plt.title('Scatter plot of 15-19 year old kids showing signs of depression in each region')


# In[18]:


age_20 = df['20-24 years old (%)']
age_25 = df['25-29 years old (%)']


# In[19]:


plt.bar(x=country,
 
        height=age_20)
plt.title('Percentage of 20-24 year old kids showing signs of depression in each region')


# In[20]:


plt.bar(x=country,
 
        height=age_25)
plt.title('Percentage of 25-29 year old kids showing signs of depression in each region')


# In[24]:


df2 = df[['Entity','10-14 years old (%)','15-19 years old (%)','20-24 years old (%)','25-29 years old (%)','50-69 years old (%)','All ages (%)']]


# In[25]:


df2.head()


# In[32]:


plt.bar(x=country,
 
        height=age_15)


# In[34]:


g = sns.pairplot(df2, kind="reg")


# In[35]:


plt.scatter(country, age_20)
plt.xlabel("Region")
plt.ylabel("20-24 year old")
plt.title('Scatter plot of 20-24 year old kids showing signs of depression in each region')


# In[36]:


plt.scatter(country, age_25)
plt.xlabel("Region")
plt.ylabel("25-29 year old")
plt.title('Scatter plot of 25-29 year old kids showing signs of depression in each region')


# In[ ]:




