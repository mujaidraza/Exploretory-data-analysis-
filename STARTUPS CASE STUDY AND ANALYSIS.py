#!/usr/bin/env python
# coding: utf-8

# In[1]:


#lest import the important libraries
import numpy as pn
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


#for interactivity
import ipywidgets as widgets
from ipywidgets import interact


# In[3]:


from ipywidgets import interact_manual


# In[4]:


#let READ THE DATASETS
data=pd.read_csv(r'D:\Data Analyst\EDA on Finance Data\startup_funding.csv')
data.columns=['SNO','Date','StartupName','IndustryVertical',
              'SubVertical','City','InvestorName','InvestorType','AmountInUSD','Remarks']


# In[5]:


data.head()


# In[6]:


data.columns


# In[7]:


#lest clean the data sets
def clean_string(x):
    return str(x).replace('\\x2\\xa0','').replace('\\\xc2\\\xa0','').replace('\\xc2\\xa0','')


# In[8]:


#lets apply the function to cleaning the datasets
for col in ['StartupName','IndustryVertical','SubVertical','City','InvestorType','AmountInUSD','Remarks','Date']:
    data[col]=data[col].apply(lambda x: clean_string(x))


# In[9]:


data.head()


# In[10]:


import warnings
warnings.filterwarnings('ignore')


# In[11]:


total=data.isnull().sum().sort_values(ascending=False)
percentage=((data.isnull().sum()/data.isnull().count())*100).sort_values(ascending=False)


# In[12]:


missing_data=pd.concat([total,percentage],axis=1, keys=['total','percentage'])
missing_data


# In[13]:


data['Remarks'].value_counts()


# In[14]:


data.drop('Remarks', axis=1, inplace=True)


# In[15]:


data.columns


# In[16]:


def clean_amount(x):
    x=" ".join([c for c in str(x) if c in ['0','1','2','3','4','5','6','7','8','9']])
    x=str(x).replace(","," ").replace("+"," ")
    x=str(x).lower().replace("undisclosed"," ")
    x=str(x).lower().replace("n/a"," ")
    x=str(x).lower().replace('unknown','')
    x=str(x).lower().replace('nan','')
    if x=='':
        x= '-999'
        return x


# In[17]:


data['AmountInUSD'].sort_values()


# In[18]:


#data['AmountInUSD']=data['AmountInUSD'].apply(lambda x: float( clean_amount(x)))


# In[19]:


#data['AmountInUSD'].plot(kind='line', color='black')
#plt.title('Distibution of AmountUSD')
#plo.show()


# In[20]:


data.columns


# In[21]:


data['Date'].value_counts().tail(50)


# In[22]:


data['Date'][data['Date']=='01/07/015']='05/07/2015'
data['Date'][data['Date']=='05/072018']='05/07/2018'
data['Date'][data['Date']=='\\xc2\\xa010/7/2015']='10/07/2015'


# In[23]:


#data['yearmonth']=(pd.to_datetime(data['Date'],
                   #format='%d/%m/%Y').dt.year*100)+(pd.to_datetime(data['Date'],format='%d/%m/%Y').dt.month)


# In[24]:


print('The max finddig : ', data['AmountInUSD'].dropna().sort_values().max())


# In[25]:


data['AmountInUSD'].dropna().sort_values()


# In[26]:


industries=data['SubVertical'].value_counts()[1:].head(12)
industries


# In[27]:


plt.rcParams['figure.figsize']=(15,5)
sns.barplot(industries.index, industries.values, palette='winter')
plt.xticks(rotation='vertical')
plt.show()


# In[28]:


#lets clean the dataset 
data['City']=data['City'].replace(['Bengaluru','nan'],['Bangalore','Bangalore'])


# In[29]:


city=data['City'].value_counts().head(10)
city


# In[30]:


sns.barplot(city.index, city.values, palette='Wistia')
plt.xticks(rotation='vertical')
plt.show()


# In[34]:


data.columns


# In[31]:


from wordcloud import WordCloud


# In[35]:


names=data['InvestorName'][~pd.isnull(data['InvestorName'])]


# In[36]:





# In[55]:


wordcloud=WordCloud(max_font_size=50,width=600,height=300, background_color='cyan').generate(''.join(names))
plt.figure(figsize=(15,6))
plt.imshow(wordcloud)

plt.axis('off')


# In[64]:


data['InvestorName'].value_counts().head(100)


# In[62]:


data['InvestorName'][data['InvestorName']=='Undisclosed investors']='Undisclosed Investors'
data['InvestorName'][data['InvestorName']=='undisclosed investors']='Undisclosed Investors'
data['InvestorName'][data['InvestorName']=='Undisclosed Investor']='Undisclosed Investors'
data['InvestorName'][data['InvestorName']=='Undisclosed']='Undisclosed Investors'
data['InvestorName'][data['InvestorName']=='nan']='Undisclosed Investors'
data['InvestorName'][data['InvestorName']=='undisclosed investor']='Undisclosed Investors'


# In[72]:


investor=data['InvestorName'].value_counts().head(10)


# In[76]:


sns.barplot(investor.index , investor.values, palette='cool')
plt.xticks(rotation='vertical')
plt.show()


# In[80]:


#lest see the  different type of funding for startups
data.columns


# In[84]:


data['InvestorType'].value_counts().head(10)


# In[85]:


data['InvestorType'][data['InvestorType']=='Seed\\nFunding']='Seed Funding '
data['InvestorType'][data['InvestorType']=='Seed/ Angel Funding ']='Seed Angel Funding '
data['InvestorType'][data['InvestorType']=='Seed / Angel Funding']='Seed Angel Funding '
data['InvestorType'][data['InvestorType']=='Seed\\nFunding  ']='Seed Funding '
data['InvestorType'][data['InvestorType']=='Seed/Angel Funding  ']='Seed Angel Funding '


# In[86]:


data['InvestorType'].value_counts().head(10)


# In[87]:


invest=data['InvestorType'].value_counts().head(10)


# In[90]:


sns.barplot(invest.index, invest.values, palette='cool')
plt.xticks(rotation='vertical')
plt.show()


# In[91]:


data.columns


# In[100]:


data['IndustryVertical'][data['IndustryVertical']=='nan']='Consumer Internet'


# In[101]:


investor=data['IndustryVertical'].value_counts().head(10)
investor


# In[102]:


sns.barplot(investor.index, investor.values, palette='summer')
plt.xticks(rotation='vertical')
plt.show()


# In[103]:


data.columns


# In[106]:


data['InvestorName'].value_counts().head(10)


# In[ ]:




