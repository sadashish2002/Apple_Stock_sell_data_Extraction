#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install yfinance==0.1.67')
#!pip install pandas==1.3.3


# In[2]:


import yfinance as yf
import pandas as pd


# # Using the yfinance Library to Extract Stock Data¶

# ## Using the Ticker module we can create an object that will allow us to access functions to extract data. To do this we need to provide the ticker symbol for the stock, here the company is Apple and the ticker symbol is AAPL.

# In[3]:


apple = yf.Ticker("AAPL")


# *Using the attribute info we can extract information about the stock as a Python dictionary

# In[5]:


apple_info= apple.info
apple_info


# #### We can get the 'country' using the key country

# In[6]:


apple_info['country']


# # Extracting Share Price

# ### A share is the single smallest part of a company's stock that you can buy, the prices of these shares fluctuate over time. Using the history() method we can get the share price of the stock over a certain period of time. Using the period parameter we can set how far back from the present to get data. The options for period are 1 day (1d), 5d, 1 month (1mo) , 3mo, 6mo, 1 year (1y), 2y, 5y, 10y, ytd, and max.

# In[10]:


apple_share_price_data = apple.history(period="max")
apple_share_price_data #if u want to get all data then use this statement
apple_share_price_data.head() 


# #### We can reset the index of the DataFrame with the reset_index function. We also set the inplace paramter to True so the change takes place to the DataFrame itself.

# In[12]:


apple_share_price_data.reset_index(inplace=True)


# In[13]:


apple_share_price_data.plot(x="Date", y="Open")


# # Extracting Dividends
Dividends are the distribution of a companys profits to shareholders. In this case they are defined as an amount of money returned per share an investor owns. Using the variable dividends we can get a dataframe of the data. The period of the data is given by the period defined in the 'history` function.
# In[14]:


apple.dividends


# In[15]:


apple.dividends.plot()


# In[ ]:




