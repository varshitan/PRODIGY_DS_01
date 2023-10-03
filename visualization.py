import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#Loading Data
df = pd.read_csv("World Development Indiacator(2001-2022).csv")
df
df.info()
df.describe()
# data cleaning
df.duplicated().sum()
df.isnull().sum()
df = df.fillna(method = "ffill")
df.head()
df.isnull().sum()
# checking the attributes which effects the most
df['Country Name'].unique()
df['2001'].unique()
df['Indicator Name'].unique()
df['Indicator Code'].unique()
df.drop(['Indicator Name','Indicator Code','Country Code'],axis = 1, inplace = True)
#EDA
# This dataset represents year wise data from 2001 to 2022
colms = ['2001', '2002', '2003', '2004', '2005', '2006', '2007',
       '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016',
       '2017', '2018', '2019', '2020', '2021', '2022']
#Ploting barcharts

years = df.columns[1:]

total_values = df[years].sum()

plt.figure(figsize=(30,40))
plt.bar(years, total_values,color='green')
plt.xlabel('Year',size=40)
plt.ylabel('Total Vales',size=40)
plt.title('Total Values per Year', size=50)
plt.show()
country_by_2001 = df.sort_values(by='2001').head(10)
country_by_2001
country_by_2001_t = country_by_2001.set_index('Country Name').T
colors = [
    "#1f77b4",  # Blue
    "#ff7f0e",  # Orange
    "#2ca02c",  # Green
    "#d62728",  # Red
    "#9467bd",  # Purple
    "#8c564b",  # Brown
    "#e377c2",  # Pink
    "#7f7f7f",  # Gray
    "#bcbd22",  # Yellow
    "#17becf"   # Cyan
]

for country_name, data_values in country_by_2001_t.iterrows():
  fig = plt.figure(figsize=(12,6))
  sns.barplot(x=data_values.index,y=data_values.values, palette=colors)
  plt.xlabel('Countries')
  plt.ylabel('Data Values')
  plt.title(f"{country_name} - Data Values from 2001 to 2022")
  plt.xticks(rotation=90)
  plt.show()
  
# Importing Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#Loading Data
df = pd.read_csv("World Development Indiacator.csv")
df
#**Showcasing Data**
df.head()
df.tail()
df.shape
df.info()
df.describe()
df.columns
# **Performing Data Cleaning**
df.duplicated().sum()
df.isnull().sum()

df = df.fillna(method = "ffill")
df.head()
df.isnull().sum()
# **Which attribute effects most**
df['Country Name'].unique()
df['Country Code'].unique()
df['2001'].unique()
df['Indicator Name'].unique()
df['Indicator Code'].unique()
df.columns
df.drop(['Indicator Name','Indicator Code','Country Code'],axis = 1, inplace = True)
df.columns
# **EDA**
# This dataset represents year wise data from 2001 to 2022
colms = ['2001', '2002', '2003', '2004', '2005', '2006', '2007',
       '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016',
       '2017', '2018', '2019', '2020', '2021', '2022']
#Ploting barcharts

years = df.columns[1:]

total_values = df[years].sum()

plt.figure(figsize=(30,40))
plt.bar(years, total_values,color='green')
plt.xlabel('Year',size=40)
plt.ylabel('Total Vales',size=40)
plt.title('Total Values per Year', size=50)
plt.show()
country_by_2001 = df.sort_values(by='2001').head(10)
country_by_2001
country_by_2001_t = country_by_2001.set_index('Country Name').T
colors = [
    "#1f77b4",  # Blue
    "#ff7f0e",  # Orange
    "#2ca02c",  # Green
    "#d62728",  # Red
    "#9467bd",  # Purple
    "#8c564b",  # Brown
    "#e377c2",  # Pink
    "#7f7f7f",  # Gray
    "#bcbd22",  # Yellow
    "#17becf"   # Cyan
]

for country_name, data_values in country_by_2001_t.iterrows():
  fig = plt.figure(figsize=(12,6))
  sns.barplot(x=data_values.index,y=data_values.values, palette=colors)
  plt.xlabel('Countries')
  plt.ylabel('Data Values')
  plt.title(f"{country_name} - Data Values from 2001 to 2022")
  plt.xticks(rotation=90)
  plt.show()
#countries with the highest values for those indicators year by year, with a base year of 2001. Based on the data you've provided, here's the list of countries with the highest indicator values for each year:

#1.   2001 & 2002: Monaco
#2.   2003: St. Martin (French part) and Monaco
#3.   2004 - 2012: St. Martin (French part)
#4.   2013 - 2017: St. Maarten (Dutch part)
#5.   2018 - 2022: Turks and Caicos Islands
chosen_country = 'Monaco'

# Filter the data for the chosen country
country_data = df[df['Country Name'] == chosen_country]

# Extract the years and values for the chosen country
years = country_data.columns[1:]
values = country_data.iloc[0, 1:]

# Create a bar graph
plt.figure(figsize=(10, 6))
plt.bar(years, values)
plt.title(f'Indicator Values for {chosen_country}')
plt.xlabel('Year')
plt.ylabel('Indicator Value')
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()



