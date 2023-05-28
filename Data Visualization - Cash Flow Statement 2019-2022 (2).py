#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np


# In[3]:


import pandas as pd


# In[4]:


from matplotlib import pyplot as plt


# In[16]:


#comparing the different types of cashflow over the years

x = np.array([2019,2020,2021,2022])
y = np.array([-2887322,2427077,392610,2026257])
z = np.array([-387064,-505354,-1339853,-2076392])
a = np.array([4505662,1237311,-1149776,-664254])


plt.bar([d-0.1 for d in x],y,width=0.10,align='center')
plt.bar([d for d in x],z,width=0.10,align='center')
plt.bar([d+0.1 for d in x],a,width=0.10,align='center')

x_ticks = np.arange(2019, 2025, 1)  
plt.xticks(x_ticks)

plt.legend(["Operating Cashflow","Investing Cashflow","Financing Cashflow"])
plt.xlabel("Year")
plt.ylabel("USD - in thousands")
plt.title("Netflix Cashflows")
plt.style.use('seaborn')
plt.show()


# In[6]:


#Comapring Beginning and Ending Cash Position

b = np.array([5043786,8238870,6055111,5170582])
c = np.array([3812041,5043786,8238870,6055111])

plt.plot(x,b,marker = '.')
plt.plot(x,c,marker = '.')

plt.legend(["End Cash Position","Beginning Cash Position"])
plt.xlabel("Year")
plt.ylabel("USD - in thousands")
plt.grid(True, linewidth=0.5)
plt.title("Cash Position")
x_ticks = np.arange(2019, 2025, 1)  
plt.xticks(x_ticks) 

plt.show()


# In[7]:


x = [2019,2020,2021,2022]
operating_gain_losses = np.array([-45576,533278,-430661,-353111])
depreciation_amortization = np.array([9319826,10922622,12438779,14362814])
deferred_taxes = np.array([-94443,70066,199548,-166550])
change_in_working_capital = np.array([43043,-31873,-241977,-758087])
stock_compensations = np.array([405376,415180,403220,575452])
netincome_fromops = np.array([1866916,2761395,5116228,4491924])
non_cash_items = np.array([-14382464,-12243591,-17092527,-16126185])

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
x_ticks = np.arange(2019, 2025, 1)  
plt.xticks(x_ticks) 

plt.show()


# In[11]:


pretax_income = np.array([5263929,5840103,3199349,2062231])
tax_provision = np.array([195315,437954,723875,772005])

Netincome = pretax_income-tax_provision

operating_cash_flow_ratio = y/Netincome

print(operating_cash_flow_ratio)


# In[12]:


plt.bar(x,operating_cash_flow_ratio,width=0.40,align='center')

x_ticks = np.arange(2019, 2025, 1)  
plt.xticks(x_ticks)

plt.legend(["Operating Cashflow Ratio"])
plt.xlabel("Year")
plt.ylabel("USD - in thousands")
plt.title("Operating Cashflow Ratio against Year")
plt.style.use('seaborn')
plt.show()


# In[13]:


cash_flow_margin = operating_cash_flow_ratio * 100

print(cash_flow_margin)


# In[14]:


cost_of_revenue = [12440213,15276319,17332683,19168285]

FCF = y - cost_of_revenue

print(FCF)


# In[15]:


plt.bar(x,FCF,width=0.40,align='center')

x_ticks = np.arange(2019, 2025, 1)  
plt.xticks(x_ticks)

plt.legend(["Free Cash Flow"])
plt.xlabel("Year")
plt.ylabel("USD - in thousands")
plt.title("Free Cash Flow against Year")
plt.style.use('seaborn')
plt.show()


# In[ ]:




