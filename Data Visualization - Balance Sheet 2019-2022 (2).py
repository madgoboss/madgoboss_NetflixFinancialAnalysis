#!/usr/bin/env python
# coding: utf-8

# In[10]:


import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


# In[14]:


x = [2019,2020,2021,2022]
total_assets = np.array([33975712,39280359,44584663,48594768])
total_liabilities = np.array([26393555,28215119,28735415,27817367])
total_equities = np.array([7582157,11065240,15849248,20777401])
                         
plt.plot(x,total_assets,linestyle='dotted', marker = '.')
plt.plot(x,total_liabilities,linestyle='dotted', marker = '.')
plt.plot(x,total_equities,linestyle='dotted', marker = '.')

plt.legend(["Total Assets","Total Liabilities","Total Equities"])
plt.xlabel("Year")
plt.ylabel("USD - in thousands")
plt.grid(True, linewidth=0.5)
plt.title("Balance Sheet - Netflix")
x_ticks = np.arange(2019, 2025, 1)  
plt.xticks(x_ticks) 


# In[11]:


#asset liability principle

d = total_assets - total_liabilities - total_equities

print(d)


# In[17]:


#calculating net working capital

current_assets = np.array([6178504,9761580,8069825,9266473])
current_liabilities = np.array([ 6855696,7805785,8488966,7930974])

net_working_capital = current_assets - current_liabilities

print(net_working_capital)

plt.bar(x,net_working_capital)
x_ticks = np.arange(2019, 2023, 1) 
plt.xticks(x_ticks)

plt.xlabel("Year")
plt.ylabel("Net Working Capital")
plt.title("Net Working Capital against Year")
plt.style.use('seaborn')
plt.show()


# In[9]:


#tallying equity

stockholders_equity = np.array([20777401,15849248,11065240,7582157])
retained_earnings = np.array([17181296,12689372,7573144,4811749])
preferred_stock = np.array([4637601,4024561,3447698,2793929])
total_equities_new = np.array([20777401,15849248,11065240,7582157])
adjustments = np.array([-217306,-40495,44398,-23521])
treasury_stock = np.array([824190,824190,0,0])

e = retained_earnings + preferred_stock - total_equities_new + adjustments - treasury_stock

print(e)



# In[13]:


#calculating current ratio
current_assets = np.array([6178504,9761580,8069825,9266473])
current_liabilities = np.array([ 6855696,7805785,8488966,7930974])

current_ratio = current_assets / current_liabilities

print(current_ratio)


# In[19]:


x = [2019,2020,2021,2022]
net_ppe = np.array([565221,960183,1323453,1398257])
land = np.array([6125,50700,82381,85005])
buildings = np.array([33141,42717,48123,52106])
machinery = np.array([242875,255447,283213,738762])
other_properties = np.array([243565,283014,380452,0])
construction = np.array ([100521,298558,282248,235555])
leases = np.array([354999,524537,863342,1040570])
                        
plt.plot(x,net_ppe,linestyle='dotted', marker = '.')
plt.plot(x,land,linestyle='dotted', marker = '.')
plt.plot(x,buildings,linestyle='dotted', marker = '.')
plt.plot(x,machinery,linestyle='dotted', marker = '.')
plt.plot(x,other_properties,linestyle='dotted', marker = '.')
plt.plot(x,construction,linestyle='dotted', marker = '.')
plt.plot(x,leases,linestyle='dotted', marker = '.')

plt.legend(["Net PPE","Land & Improvments","Building & Improvements","Machinery Equipment","Other Properties","Construction in Progress","Leases"])
plt.xlabel("Year")
plt.ylabel("USD - in thousands")
plt.grid(True, linewidth=0.5)
plt.title("PPE and its components")
x_ticks = np.arange(2019, 2025, 1)  
plt.xticks(x_ticks) 


# In[33]:


total_debt = np.array([14759260,16308973,15392895,14353076])

plt.bar([d-0.15 for d in x],total_debt,width = 0.15,align='center')
plt.bar([d+0.15 for d in x],total_liabilities,width = 0.15,align='center')
x_ticks = np.arange(2019, 2024, 1) 
plt.xticks(x_ticks)

plt.xlabel("Year")
plt.ylabel("USD in thousands")
plt.title("Total Debt & Total Liabilities against Year")
plt.legend(["Total Debt","Total Liabilities"])
plt.show()


# In[ ]:




