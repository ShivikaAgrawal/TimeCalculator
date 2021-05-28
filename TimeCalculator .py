#!/usr/bin/env python
# coding: utf-8

# In[19]:


import pytz, datetime  ##importing libraries
year = int(input())
month = int(input())
day = int(input())
hours = int(input())
minutes= int(input())


# In[10]:


#converting into timestamp


# In[20]:


curr_date=datetime.datetime(year,month,day,hours,minutes)


# In[ ]:


#To get time of that city


# In[16]:


cairo_tz=pytz.timezone('Africa/cairo')
london_tz=pytz.timezone('utc')
Newdelhi_tz=pytz.timezone('Asia/kolkata')
Sydney_tz=pytz.timezone('Australia/sydney') 


# In[17]:


cairo_time=pytz.utc.localize(curr_date).astimezone(cairo_tz) 
london_time=pytz.utc.localize(curr_date).astimezone(london_tz)
Newdelhi_time=pytz.utc.localize(curr_date).astimezone(Newdelhi_tz)
Sydney_time=pytz.utc.localize(curr_date).astimezone(Sydney_tz)


# In[12]:


#print Timestamp of particular city in ISO format


# In[21]:


print("Cairo Time is",cairo_time.isoformat())  
print("London Time is",london_time.isoformat())
print("New Delhi Time is",Newdelhi_time.isoformat())
print("Sydney Time is",Sydney_time.isoformat())


# In[ ]:




