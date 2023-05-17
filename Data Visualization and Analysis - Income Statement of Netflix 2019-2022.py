#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


import pandas as pd


# In[3]:


from matplotlib import pyplot as plt


# In[8]:


#comparing income as a differenace between total revenue and cost of revenue over the years

x = [2019,2020,2021,2022]
y = [20156447, 24996056,29697844,31615550]
z = [12440213,15276319,17332683,19168285]

a = [y_i - z_i for y_i, z_i in zip(y, z)]

plt.plot(x,y,linestyle='dotted', marker = '.')
plt.plot(x,z,linestyle='dotted', marker = '.')
plt.plot(x,a,linestyle='dotted', marker = '.')


plt.legend(["Total Revenue","Cost of Revenue","Income"])
plt.xlabel("Year")
plt.ylabel("USD - in thousands")
plt.grid(True, linewidth=0.5)
plt.title("Netflix - Income")
x_ticks = np.arange(2019, 2025, 1)  # Range from 2019 to 2022 with interval of 2
plt.xticks(x_ticks) 

plt.show()


# In[16]:


#comparing gross profit as a differance between operating income and operating expenses

x = [2019,2020,2021,2022]
b = [2604254,4585289,6194509,5632831]
c = [5111980,5134448,6170652,6814434]

d = [b_i - c_i for b_i, c_i in zip(b, c)]

plt.plot(x,b,linestyle='dotted', marker = 'o')
plt.plot(x,c,linestyle='dotted', marker = 'o')
plt.plot(x,d,linestyle='dotted', marker = 'o')


plt.legend(["Operating Income","Operating Expense","Gross Profit"])
plt.xlabel("Year")
plt.ylabel("USD - in thousands")
plt.grid(True, linewidth=0.5)
plt.title("Netflix - Income")
x_ticks = np.arange(2019, 2025, 1)  # Range from 2019 to 2022 with interval of 2
plt.xticks(x_ticks) 

plt.show()


# In[22]:


#calculating net interest income as a differance of interest income and interest expense

e = np.array([84000,0,411214,337310])
f = np.array([626023,1385940,765620,706212])

netinterestincome = e-f

print(netinterestincome)


# In[43]:


#Other incomes over the years

g = [5263929,5840103,3199349,2062231]
f = [1866916,2761395,5116228,4491924]


plt.plot(x,f,marker = '.')
plt.plot(x,netinterestincome,marker = '.')

plt.legend(["Net income from subscriptions","Net income from Interests"])
plt.xlabel("Year")
plt.ylabel("USD - in thousands")
plt.grid(True, linewidth=0.5)
plt.title("Netflix - Income")
x_ticks = np.arange(2019, 2025, 1)  # Range from 2019 to 2022 with interval of 2
plt.xticks(x_ticks) 

plt.show()


# In[44]:


#Expressing net income as a differance between pretax income and tax provsion

g = np.array([5263929,5840103,3199349,2062231])
h = np.array([195315,437954,723875,772005])

Netincome = g-h

print(Netincome)

plt.plot(x,g,linestyle='dotted',marker = '.')
plt.plot(x,h,linestyle='dotted',marker = '.')
plt.plot(x,Netincome, marker = '.')

plt.legend(["Pretax Income","Tax Provision","Net Income"])
plt.xlabel("Year")
plt.ylabel("USD - in thousands")
plt.grid(True, linewidth=0.5)
plt.title("Netflix's Net Income - 2019 to 2022")
x_ticks = np.arange(2019, 2025, 1)  # Range from 2019 to 2022 with interval of 2
plt.xticks(x_ticks) 


# In[45]:


#Finding number of outstanding shares from NetIncome and EPS
EPS = np.array([4.26,6.26,11.55,1], dtype=float)
Netincome = g-h

i = np.round(Netincome / EPS).astype(int)

print(i)


# In[46]:


#Plotting number of outstanding shares

plt.plot(x,i,linestyle='dotted', marker = '.')

plt.xlabel("Year")
plt.ylabel("USD - in thousands")
plt.grid(True, linewidth=0.5)
plt.title("Number of Outstanding Shares - 2019 to 2022")
x_ticks = np.arange(2019, 2025, 1)  # Range from 2019 to 2022 with interval of 2
plt.xticks(x_ticks) 



# In[54]:


#Calculating interest expenditure as differance between EBIT and Pretax income

EBIT = np.array([2688254,4585289,6605723,5970141])

InterestExpense = EBIT - g

print(InterestExpense)


# In[51]:


#Comparing depreciation and amortization; expenses of the fixed assest spread over its ueful life

EBITDA = np.array([12008080,15507911,19044502,20332955])
EBIT = np.array([2688254,4585289,6605723,5970141])

DA = EBITDA - EBIT 

print(DA)

plt.plot(x,EBITDA,linestyle='dotted',marker = '.')
plt.plot(x,EBIT,linestyle='dotted',marker = '.')
plt.plot(x,DA, marker = '.')

plt.legend(["EBITDA","EBIT","DA"])
plt.xlabel("Year")
plt.ylabel("USD - in thousands")
plt.grid(True, linewidth=0.5)
plt.title("Netflix's Net Income - 2019 to 2022")
x_ticks = np.arange(2019, 2025, 1)  # Range from 2019 to 2022 with interval of 2
plt.xticks(x_ticks) 


# In[59]:


#Piechart of operating expenses 2022
views = [1572891,2530502,2711041]
labels = ['SGNA - G&A Expenses', 'SGNA - Selling and Marketing', 'R&D']

plt.pie(views,labels=labels , wedgeprops = {'width' : 0.3})

plt.title('Proportion of Operating Expenses 2022')
plt.axis('equal') 
plt.show()


# In[58]:


#Piechart of operating expenses 2021
views = [1351621,2545146,2273885]
labels = ['SGNA - G&A Expenses', 'SGNA - Selling and Marketing', 'R&D']

plt.pie(views,labels=labels , wedgeprops = {'width' : 0.3})

plt.title('Proportion of Operating Expenses 2021')
plt.axis('equal') 
plt.show()


# In[56]:


#Piechart of operating expenses 2020
views = [1076486,2228362,1829600]
labels = ['SGNA - G&A Expenses', 'SGNA - Selling and Marketing', 'R&D']

plt.pie(views,labels=labels , wedgeprops = {'width' : 0.3})

plt.title('Proportion of Operating Expenses 2020')
plt.axis('equal') 
plt.show()


# In[55]:


#Piechart of operating expenses 2019
views = [914369,2652462,1545149]
labels = ['SGNA - G&A Expenses', 'SGNA - Selling and Marketing', 'R&D']

plt.pie(views,labels=labels , wedgeprops = {'width' : 0.3})

plt.title('Proportion of Operating Expenses 2019')
plt.axis('equal') 
plt.show()

