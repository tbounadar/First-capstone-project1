
# coding: utf-8

Mini project: EDA for Titanic dataset(since the dataset for my project is not very clean. I chose to work with a new one and answer the questions)


Can you count something interesting?
-Females survived more,
-People from class one survived more
-People who embarked from C survied more than Q.

Can you find trends (e.g. high, low, increasing, decreasing, anomalies)?
-Age is a normal distribution 
-Young people survived more than old and kids.


Can you make a bar plot or a histogram?
Bar plot for gender, class, fares and cabin


Can you compare two related quantities?
Fares vs survival, age vs survival


Can you make a scatterplot?
Age vs survival


Can you make a time-series plot?
No time column



# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Comment this if the data visualisations doesn't work on your side
get_ipython().run_line_magic('matplotlib', 'inline')

df = pd.read_csv("train.csv")
# Print the head
df.head()


# In[2]:


#Print the tail
df.tail()


# In[3]:


#Find out the columns types
df.dtypes


# In[4]:


# print the mean, min,max,and std
df.describe()


# In[5]:


# Print the set information
df.info()


# In[6]:


#Print the columns
df.columns


# In[7]:


#Count the colmuns
df.count()


# In[8]:


df


# In[9]:


#Find out missing values and their percentage per column
df.isnull().sum()/df.count()[0]

We see many missing values in the Cabin and Age columns
19% missing values in Age and 79% in Cabin
# In[10]:


df.count()[0]


# In[11]:


df = df.dropna()


# In[12]:


df.Age = df.Age.astype(int)


# In[40]:


# Group by age and survived colmns
asur = pd.DataFrame(df.groupby(['Age'])['Survived'].sum())
asur.head()


# In[32]:


# Group by age and survived colmns
df.groupby(['Survived','Sex'])['Survived'].count()


# In[31]:


#Plot age
df.Age.hist()


# In[16]:


sns.countplot(x='Survived', data=df);


# In[17]:


df.count()


# In[18]:


# Nearly 67% of the people survived
print(df.Survived.sum()/df.Survived.count())


# In[19]:


# Survivals by gender: Females were the most rescued
df.groupby(['Survived','Sex'])['Survived'].count()


# In[60]:


# Survivals by Embarked
df.groupby(['Survived','Embarked'])['Embarked'].count()


# In[61]:


print("Ratio of survived / not for C and Q are")
print(48/17, 74/42)
print("People who emabarked from C survived more than people who embarked from Q")


# In[ ]:


# sns.catplot(x='Sex', col='Survived', kind='count', data=df);
# Seabor no longer surpports catplot function


# In[ ]:


# import seaborn as sns
# sns.set(style="ticks")
# exercise = sns.load_dataset("exercise")
# exercise


# In[22]:


df2= pd.DataFrame({'lab':['A', 'B', 'C'], 'val':[10, 30, 20]})
ax = df2.plot.bar(x='lab', y='val', rot=0)


# In[23]:


#Plot age and Survived columns
asur = asur.reset_index()
ax = asur.plot.bar(x='Age', y='Survived', rot=0)


# In[39]:


asur.head()


# In[30]:


#plot age and survived columns
plt.scatter(asur['Age'], asur['Survived'])


# In[24]:


#Group by class and survived columns
classsur = pd.DataFrame(df.groupby(['Pclass'])['Survived'].sum())
classsur


# In[25]:


# Plot the class and the survived columns
classsur = classsur.reset_index()
ax = classsur.plot.bar(x='Pclass', y='Survived', rot=0)


# In[26]:


# correlation between survivals and the Fares they paid: There is no correlation
faresur = pd.DataFrame(df.groupby(['Fare'])['Survived'].sum())
faresur = faresur.reset_index()
faresur
faresur['Fare'].corr(faresur['Survived'])


# In[27]:


# scotterplot for Fare and Survived
plt.scatter(faresur['Fare'], faresur['Survived'])


# In[62]:


#Exploring colleration between age and the survivals
agesur = pd.DataFrame(df.groupby(['Age'])['Survived'].sum())
agesur = agesur.reset_index()
agesur
agesur['Age'].corr(faresur['Survived'])


# In[ ]:


# There is no correclation between age and the survivals!


# In[59]:


df.head()


# In[38]:


# Getting rid of the missing values
dfc=df.dropna()
dfc


# In[46]:


# Number of survivals per Cabin 

dfcab = pd.DataFrame(dfc.groupby(['Cabin'])['Survived'].sum())
dfcab.head()
dfcab.sort_values(by='Survived',ascending=False).head()

The cabin B96 B98 survived the most - we need to explore why?

# In[47]:


# Plot Cabin and Survived
dfcab = dfcab.reset_index()
ax = dfcab.plot.bar(x='Cabin', y='Survived', rot=0)


# In[58]:


#ClassClass one survived more
dfcl = pd.DataFrame(dfc.groupby(['Pclass'])['Survived', 'Pclass'].sum())
dfcl.head()
dfcl.sort_values(by='Survived',ascending=False)
dfcl['perc'] = dfcl.Survived / dfcl.Pclass
dfcl

