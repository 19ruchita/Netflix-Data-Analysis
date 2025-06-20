#!/usr/bin/env python
# coding: utf-8

# ## Netflix Dataset

# ![1.png](attachment:1.png)

# -------

# In[1]:


# Importing the dataset
import pandas as pd
import streamlit as st
st.title("Netflix Data Analytics")

data = pd.read_csv(r"C:\Users\ROHIT GREWAL\Desktop\DSL\Videos\Data-Sets\8. Netflix Dataset.csv")                     # to import pandas library


# In[2]:


data

st.subheader("Show Type Distribution")
fig, ax = plt.subplots()
sns.countplot(data=df, x='type', ax=ax)
st.pyplot(fig)

# In[ ]:





# #### Getting some basic information about the dataset

# ### 1. head()

# In[3]:


data.head()                                     # to show top-5 records of the dataset


# ### 2. tail()

# In[4]:


data.tail()                                      # to show bottom-5 records of dataset


# ### 3. shape

# In[5]:


data.shape                                      # to show the No. of Rows and Columns


# ### 4. size

# In[6]:


data.size                                      # to show No. of total values(elements) in the dataset


# ### 5. columns

# In[7]:


data.columns                                   # to show each Column Name


# ### 7. dtypes

# In[8]:


data.dtypes                                    # to show the data-type of each column


# ### 8. info()

# In[9]:


data.info()                                   # To show indexes, columns, data-types of each column, memory at once


# ----

# ### Task.1. Is there any Duplicate Record in this dataset ? If yes, then remove the duplicate records.

# ### duplicate()

# In[10]:


data.head()


# In[11]:


data.shape


# In[12]:


data[data.duplicated()]                                         # To check row wise and detect the Duplicate rows  


# In[13]:


data.drop_duplicates(inplace = True)                                # To Remove the Duplicate rows permanently


# In[14]:


data[data.duplicated()]


# In[15]:


data.shape


# ----

# ### Task.2. Is there any Null Value present in any column ? Show with Heat-map.

# ### isnull()

# In[16]:


data.head()


# In[17]:


data.isnull()                                               # To show where Null value is present


# In[18]:


data.isnull().sum()                                               # To show the count of Null values in each column


# ### seaborn library (heat-map)

# In[19]:


import seaborn as sns                                               # To import Seaborn library


# In[20]:


sns.heatmap(data.isnull())                                               # Using heat-map to show null values count


# ----

# ----

# ### Q.1. For 'House of Cards', what is the Show Id and Who is the Director of this show ?

# ### isin()

# In[21]:


data.head()


# In[22]:


data[data['Title'].isin(['House of Cards'])]       #  To show all records of a particular item in any column


# ### str.contains()

# In[23]:


data[data['Title'].str.contains('House of Cards')]          #  To show all records of a particular string in any column


# ----

# ### Q.2. In which year highest number of the TV Shows & Movies were released ? Show with Bar Graph.

# ### dtypes

# In[24]:


data.dtypes


# ### to_datetime

# In[25]:


data['Date_N'] = pd.to_datetime(data['Release_Date'])


# In[26]:


data.head()


# In[27]:


data.dtypes


# In[ ]:





# ### dt.year.value_counts()

# In[28]:


data['Date_N'].dt.year.value_counts()                # It counts the occurrence of all individual Years in Date column.


# ### Bar Graph

# In[29]:


data['Date_N'].dt.year.value_counts().plot(kind='bar')


# ----

# ### Q.3. How many Movies & TV Shows are in the dataset ? Show with Bar Graph.

# ### groupby()

# In[30]:


data.head(2)


# In[31]:


data.groupby('Category').Category.count()                 # To group all unique items of a column and show their count


# ### countplot()

# In[32]:


sns.countplot(data['Category'])        # To show the count of all unique values of any column in the form of bar graph


# ----

# ### Q.4. Show all the Movies that were released in year 2000.

# ### Creating new column

# In[37]:


# data.head()
data.head(2)


# In[38]:


# data['Year'] = data['Date_N'].dt.year           # to create new Year column ; it will consider only year

data['Year'] = data['Date_N'].dt.year


# In[39]:


# data.head(2)

data.head(2)


# ### Filtering

# In[40]:


# data[ (data['Category']=='Movie') & (data['Year']==2020) ]

data[ (data['Category'] == 'Movie') & (data['Year']==2000) ]


# In[41]:


data[ (data['Category'] == 'Movie') & (data['Year']==2020) ]


# ----

# ### Q.5. Show only the Titles of all TV Shows that were released in India only.

# ### Filtering

# In[42]:


# data.head(2)

data.head(2)


# In[44]:


# data [ (data['Category'] == 'TV Show') & (data['Country'] == 'India') ] ['Title']

data[ (data['Category']=='TV Show') & (data['Country']=='India') ] ['Title']


# ----

# ### Q.6. Show Top 10 Directors, who gave the highest number of TV Shows & Movies to Netflix ?

# ### value_counts()

# In[45]:


# data['Director'].value_counts().head(10)

data.head(2)


# In[48]:


data['Director'].value_counts().head(10)


# ----

# #### Q.7. Show all the Records, where "Category is Movie and Type is Comedies" or "Country is United Kingdom".

# ### Filtering ( And, Or Operators )

# In[49]:


# data[(data['Category']=='Movie') & (data['Type']=='Comedies') ]

data.head(2)


# In[51]:


data[ (data['Category']=='Movie') & (data['Type']=='Comedies') ]


# In[52]:


# data[(data['Category']=='Movie') & (data['Type']=='Comedies') | (data['Country']=='United Kingdom')]

data[ (data['Category']=='Movie') & (data['Type']=='Comedies') | (data['Country']=='United Kingdom')]


# ----

# ### Q.8. In how many movies/shows, Tom Cruise was cast ?

# In[53]:


# data.head()

data.head(2)


# ### filtering

# In[55]:


# data[data['Cast']=='Tom Cruise']

data[data['Cast'] == 'Tom Cruise']


# ### str.contains()

# In[56]:


# data[data['Cast'].str.contains('Tom Cruise')]

data[data['Cast'].str.contains('Tom Cruise')]


# ### Creating new data-frame

# In[57]:


# data_new = data.dropna()                       # It drops the rows that contains all or any missing values.

data_new = data.dropna()


# In[58]:


# data_new.head(2)

data_new.head(2)


# In[59]:


# data_new[data_new['Cast'].str.contains('Tom Cruise')]

data_new[data_new['Cast'].str.contains('Tom Cruise')]


# ----

# ### Q.9. What are the different Ratings defined by Netflix ?

# ### nunique()

# In[60]:


# data.Rating.nunique()

data.head(2)


# In[61]:


data['Rating'].nunique()


# ### unique()

# In[62]:


# data.Rating.unique()

data['Rating'].unique()


# #### Q.9.1. How many Movies got the 'TV-14' rating, in Canada ?

# In[64]:


data.head(2)


# In[66]:


# data[(data['Category']=='Movie') & (data['Rating'] == 'TV-14')].shape

data[(data['Category']=='Movie') & (data['Rating']=='TV-14')].shape


# In[68]:


# data[(data['Category']=='Movie') & (data['Rating'] == 'TV-14') & (data['Country']=='Canada')].shape

data[(data['Category']=='Movie') & (data['Rating']=='TV-14') & (data['Country']=='Canada')].shape


# #### Q.9.2. How many TV Show got the 'R' rating, after year 2018 ?

# In[69]:


# data[(data['Category']=='TV Show') & (data['Rating'] == 'R')]

data.head(2)


# In[70]:


data[(data['Category']=='TV Show') & (data['Rating']=='R')]


# In[71]:


# data[(data['Category']=='TV Show') & (data['Rating'] == 'R') & (data['Year'] > 2018)]

data[(data['Category']=='TV Show') & (data['Rating']=='R') & (data['Year'] > 2018)]


# ----

# ### Q.10. What is the maximum duration of a Movie/Show on Netflix ?

# In[72]:


# data.head(2)

data.head(2)


# In[73]:


# data['Duration'].unique()

data.Duration.unique()


# In[74]:


# data.Duration.dtypes

data.Duration.dtypes


# ### str.split()

# In[75]:


data.head(2)


# In[76]:


# data[['Minutes','Unit']] = data['Duration'].str.split(' ', expand=True)

data[['Minutes', 'Unit']] = data['Duration'].str.split(' ', expand = True)


# In[77]:


# data.head(2)

data.head(2)


# ### max()

# In[79]:


# data.Minutes.max()

data['Minutes'].max()


# In[80]:


data['Minutes'].min()


# In[81]:


data['Minutes'].mean()


# In[82]:


data.dtypes


# ----

# ### Q.11. Which individual country has the Highest No. of TV Shows ?

# In[83]:


# data.head(2)

data.head(2)


# In[84]:


# data_tvshow = data[data['Category'] == 'TV Show']

data_tvshow = data[data['Category'] == 'TV Show']


# In[85]:


# data_tvshow.head(2)

data_tvshow.head(2)


# In[86]:


# data_tvshow.Country.value_counts()

data_tvshow.Country.value_counts()


# In[88]:


# data_tvshow.Country.value_counts().head(1)

data_tvshow.Country.value_counts().head(1)


# ----

# ### Q.12. How can we sort the dataset by Year ?

# In[89]:


# data.head(2)

data.head(2)


# In[90]:


# data.sort_values(by='Year').head(2)

data.sort_values(by = 'Year')


# In[92]:


# data.sort_values(by='Year', ascending=False).head(2)

data.sort_values(by = 'Year', ascending = False).head(10)


# ----

# ### Q.13. Find all the instances where : 

# ### Category is 'Movie' and Type is 'Dramas'

# ### or

# ###  Category is 'TV Show' & Type is 'Kids' TV'

# In[93]:


data.head(2)


# In[95]:


# data [(data['Category']=='Movie') & (data['Type']=='Dramas')].head(2)

data [ (data['Category']=='Movie') & (data['Type']=='Dramas') ].head(2)


# In[100]:


# data[(data['Category']=='TV Show') & (data['Type']=="Kids' TV")].head(2)

data [ (data['Category']=='TV Show') & (data['Type']== "Kids' TV") ]


# In[101]:


# data [(data['Category']=='Movie') & (data['Type']=='Dramas') | (data['Category']=='TV Show') & (data['Type']=="Kids' TV")].head(1)

data [ (data['Category']=='Movie') & (data['Type']=='Dramas') | (data['Category']=='TV Show') & (data['Type']== "Kids' TV") ]

