#!/usr/bin/env python
# coding: utf-8

# In[11]:


import numpy as np


# In[12]:


import pandas as pd


# In[13]:


from matplotlib import pyplot as plt


# In[14]:


#comparing the different types of cashflow over the years

x = [2019,2020,2021,2022]
y = [-2887322,2427077,392610,2026257]
z = [-387064,-505354,-1339853,-2076392]
a = [4505662,1237311,-1149776,-664254]


plt.bar([a-0.1 for a in x],y,width=0.10,align='center')
plt.bar([a for a in x],z,width=0.10,align='center')
plt.bar([a+0.1 for a in x],y,width=0.10,align='center')

x_ticks = np.arange(2019, 2025, 1)  # Range from 2019 to 2022 with interval of 2
plt.xticks(x_ticks)

plt.legend(["Operating Cashflow","Investing Cashflow","Financing Cashflow"])
plt.xlabel("Year")
plt.ylabel("USD - in thousands")
plt.title("Netflix Cashflows")
plt.style.use('seaborn')
plt.show()


# In[15]:


#Comapring Beginning and Ending Cash Position

b = [5043786,8238870,6055111,5170582]
c = [3812041,5043786,8238870,6055111]

plt.plot(x,b,marker = '.')
plt.plot(x,c,marker = '.')

plt.legend(["End Cash Position","Beginning Cash Position"])
plt.xlabel("Year")
plt.ylabel("USD - in thousands")
plt.grid(True, linewidth=0.5)
plt.title("Netflix Cashflows")
x_ticks = np.arange(2019, 2025, 1)  # Range from 2019 to 2022 with interval of 2
plt.xticks(x_ticks) 

plt.show()


# In[24]:


x = [2019,2020,2021,2022]
operating_gain_losses = [-45576,533278,-430661,-353111]
depreciation_amortization = [9319826,10922622,12438779,14362814]
deferred_taxes = [-94443,70066,199548,-166550]
change_in_working_capital = [43043,-31873,-241977,-758087]
stock_compensations = [405376,415180,403220,575452]
netincome_fromops = [1866916,2761395,5116228,4491924]
non_cash_items = [-14382464,-12243591,-17092527,-16126185]

plt.plot(x,operating_gain_losses, marker = '.')
plt.plot(x,depreciation_amortization, marker = '.')
plt.plot(x,deferred_taxes, marker = '.')
plt.plot(x,change_in_working_capital, marker = '.')
plt.plot(x,stock_compensations, marker = '.')
plt.plot(x,netincome_fromops, marker = '.')
plt.plot(x,non_cash_items, marker = '.')

plt.legend(["Operating Gains and Losses","Depreciation&Amortization","Deferred Taxes","Change in Working Capital", "Stock Compensations","Net Income from Ops","Non Cash Items"])
plt.xlabel("Year")
plt.ylabel("SGD")
plt.grid(True, linewidth=0.5)
plt.title("Components of Operating Cash Flow")
x_ticks = np.arange(2019, 2025, 1)  # Range from 2000 to 2022 with interval of 2
plt.xticks(x_ticks) 

plt.show()


# In[ ]:




