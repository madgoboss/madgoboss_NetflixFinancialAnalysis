#!/usr/bin/env python
# coding: utf-8

# In[10]:


import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


# In[11]:


x = [2019,2020,2021,2022]
total_assets = np.array([33975712,39280359,44584663,48594768])
total_liabilities = np.array([26393555,28215119,28735415,27817367])
total_equities = np.array([7582157,11065240,15849248,20777401])
                         
plt.plot(x,total_assests,linestyle='dotted', marker = '.')
plt.plot(x,total_liabilities,linestyle='dotted', marker = '.')
plt.plot(x,total_equities,linestyle='dotted', marker = '.')

plt.legend(["Total Assets","Total Liabilities","Total Equities"])
plt.xlabel("Year")
plt.ylabel("SGD")
plt.grid(True, linewidth=0.5)
plt.title("Balance Sheet - Netflix")
x_ticks = np.arange(2019, 2025, 1)  # Range from 2000 to 2022 with interval of 2
plt.xticks(x_ticks) 


# In[12]:


#asset liability principle

d = total_assets - total_liabilities - total_equities

print(d)


# In[14]:


#calculating net working capital

current_assets = np.array([6178504,9761580,8069825,9266473])
current_liabilities = np.array([ 6855696,7805785,8488966,7930974])

net_working_capital = current_assets - current_liabilities

print(net_working_capital)


# In[27]:


#tallying equity

stockholders_equity = np.array([20777401,15849248,11065240,7582157])
retained_earnings = np.array([17181296,12689372,7573144,4811749])
preferred_stock = np.array([4637601,4024561,3447698,2793929])
total_equities_new = np.array([20777401,15849248,11065240,7582157])
adjustments = np.array([-217306,-40495,44398,-23521])
treasury_stock = np.array([824190,824190,0,0])

e = retained_earnings + preferred_stock - total_equities_new + adjustments - treasury_stock

print(e)



# In[ ]:




