#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np


# In[3]:


import pandas as pd


# In[4]:


from matplotlib import pyplot as plt


# In[6]:


#comparing income as a differenace between total revenue and cost of revenue over the years

x = [2019,2020,2021,2022]
total_revenue = [20156447, 24996056,29697844,31615550]
cost_of_revenue = [12440213,15276319,17332683,19168285]

gross_profit = [total_revenue_i - cost_of_revenue_i for total_revenue_i, cost_of_revenue_i in zip(total_revenue, cost_of_revenue)]

plt.plot(x,total_revenue,linestyle='dotted', marker = '.')
plt.plot(x,cost_of_revenue,linestyle='dotted', marker = '.')
plt.plot(x,gross_profit,linestyle='dotted', marker = '.')

print(gross_profit)

plt.legend(["Total Revenue","Cost of Revenue","Gross Profit"])
plt.xlabel("Year")
plt.ylabel("USD - in thousands")
plt.grid(True, linewidth=0.5)
plt.title("Netflix - Gross Profit")
x_ticks = np.arange(2019, 2025, 1)  
plt.xticks(x_ticks) 

plt.show()


# In[11]:


#comparing operating profit as a differance between operating income and operating expenses

x = [2019,2020,2021,2022]
operating_income = [2604254,4585289,6194509,5632831]
operating_expense = [5111980,5134448,6170652,6814434]

operating_profit = [operating_income_i - operating_expense_i for operating_income_i, operating_expense_i in zip(operating_income, operating_expense)]

plt.plot(x,operating_income,linestyle='dotted', marker = 'o')
plt.plot(x,operating_expense,linestyle='dotted', marker = 'o')
plt.plot(x,operating_profit,linestyle='dotted', marker = 'o')

print (operating_profit)


plt.legend(["Operating Income","Operating Expense","Operating Profit"])
plt.xlabel("Year")
plt.ylabel("USD - in thousands")
plt.grid(True, linewidth=0.5)
plt.title("Netflix - Operational Data")
x_ticks = np.arange(2019, 2025, 1)  
plt.xticks(x_ticks) 

plt.show()


# In[10]:


#calculating net interest income as a differance of interest income and interest expense

interest_income = np.array([84000,0,411214,337310])
interest_expense = np.array([626023,1385940,765620,706212])

netinterestincome = interest_income-interest_expense

print(netinterestincome)


# In[15]:


#Other incomes over the years

net_income_subcriptions = [1866916,2761395,5116228,4491924]


plt.plot(x,net_income_subcriptions,marker = '.')
plt.plot(x,netinterestincome,marker = '.')

plt.legend(["Net income from subscriptions","Net income from Interests"])
plt.xlabel("Year")
plt.ylabel("USD - in thousands")
plt.grid(True, linewidth=0.5)
plt.title("Netflix - Income")
x_ticks = np.arange(2019, 2025, 1) 
plt.xticks(x_ticks) 

plt.show()


# In[13]:


#Expressing net income as a differance between pretax income and tax provsion

pretax_income = np.array([5263929,5840103,3199349,2062231])
tax_provision = np.array([195315,437954,723875,772005])

Netincome = pretax_income-tax_provision

print(Netincome)

plt.plot(x,pretax_income,linestyle='dotted',marker = '.')
plt.plot(x,tax_provision,linestyle='dotted',marker = '.')
plt.plot(x,Netincome, marker = '.')

plt.legend(["Pretax Income","Tax Provision","Net Income"])
plt.xlabel("Year")
plt.ylabel("USD - in thousands")
plt.grid(True, linewidth=0.5)
plt.title("T - 2019 to 2022")
x_ticks = np.arange(2019, 2025, 1) 
plt.xticks(x_ticks) 


# In[14]:


#Finding number of outstanding shares from NetIncome and EPS
EPS = np.array([4.26,6.26,11.55,1], dtype=float)

no_of_outstanding_shares = np.round(Netincome / EPS).astype(int)

print(no_of_outstanding_shares)


# In[16]:


#Plotting number of outstanding shares

plt.plot(x,no_of_outstanding_shares,linestyle='dotted', marker = '.')

plt.xlabel("Year")
plt.ylabel("USD - in thousands")
plt.grid(True, linewidth=0.5)
plt.title("Number of Outstanding Shares - 2019 to 2022")
x_ticks = np.arange(2019, 2025, 1)  # Range from 2019 to 2022 with interval of 2
plt.xticks(x_ticks) 



# In[19]:


#Calculating interest expenditure as differance between EBIT and Pretax income

EBIT = np.array([2688254,4585289,6605723,5970141])

InterestExpense = EBIT - pretax_income

print(InterestExpense)

plt.bar(x,InterestExpense)
x_ticks = np.arange(2019, 2023, 1) 
plt.xticks(x_ticks)

plt.xlabel("Year")
plt.ylabel("Interest Expense")
plt.title("Interest Expense against Year")
plt.style.use('seaborn')
plt.show()


# In[18]:


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
plt.title("DA")
x_ticks = np.arange(2019, 2025, 1)  # Range from 2019 to 2022 with interval of 2
plt.xticks(x_ticks) 


# In[21]:


#Piechart of operating expenses 2022
views = [1572891,2530502,2711041]
labels = ['SGNA - G&A Expenses', 'SGNA - Selling and Marketing', 'R&D']

plt.pie(views,labels=labels , wedgeprops = {'width' : 0.3})

plt.title('Proportion of Operating Expenses 2022')
plt.axis('equal') 
plt.show()


# In[22]:


#Piechart of operating expenses 2021
views = [1351621,2545146,2273885]
labels = ['SGNA - G&A Expenses', 'SGNA - Selling and Marketing', 'R&D']

plt.pie(views,labels=labels , wedgeprops = {'width' : 0.3})

plt.title('Proportion of Operating Expenses 2021')
plt.axis('equal') 
plt.show()


# In[23]:


#Piechart of operating expenses 2020
views = [1076486,2228362,1829600]
labels = ['SGNA - G&A Expenses', 'SGNA - Selling and Marketing', 'R&D']

plt.pie(views,labels=labels , wedgeprops = {'width' : 0.3})

plt.title('Proportion of Operating Expenses 2020')
plt.axis('equal') 
plt.show()


# In[24]:


#Piechart of operating expenses 2019
views = [914369,2652462,1545149]
labels = ['SGNA - G&A Expenses', 'SGNA - Selling and Marketing', 'R&D']

plt.pie(views,labels=labels , wedgeprops = {'width' : 0.3})

plt.title('Proportion of Operating Expenses 2019')
plt.axis('equal') 
plt.show()


# In[ ]:




